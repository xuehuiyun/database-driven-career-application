from flask import Flask, render_template,jsonify,request
from database import load_jobs_from_db, load_job_from_db, add_information_to_db
app = Flask(__name__)

@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html',jobs=jobs)
@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)
  
@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found",404
  return render_template('jobpage.html',job=job)
@app.route("/job/<id>/apply")
def apply_to_job(id):
  data = request.args
  #store the data in the database
  #display an ackonelwdgement
  #send an email
  return render_template('application_submitted.html',
                         application=data) 
@app.route('/event.html')
def event():
    return render_template('event.html')
@app.route('/register.html')
def register():
  return render_template('register.html')
@app.route("/register",methods=['post'])
def apply_user_register():
  data = request.form
  add_information_to_db(data)
  return render_template('register_form.html',
                        register=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
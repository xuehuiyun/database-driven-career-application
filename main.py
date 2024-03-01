from flask import Flask, render_template,jsonify,request
from database import load_dogs_from_db, add_information_to_db, load_dog_from_db
app = Flask(__name__)

@app.route('/')
def hello_world():
    dogs = load_dogs_from_db()
    return render_template('home.html', dogs=dogs)
@app.route('/api/dogs')
def list_dogs():
    dogs = load_dogs_from_db()
    return jsonify(dogs)


@app.route("/dog/<id>")
def show_dog(id):
  dog = load_dog_from_db(id)
  if not dog:
    return "Not Found",404
  return render_template('dogpage.html',dog=dog)
  
@app.route("/job/<id>/apply")
def apply_to_job(id):
  data = request.args
  
  return render_template('application_submitted.html',
                         application=data) 
@app.route('/event.html')
def event():
    return render_template('event.html')
@app.route('/about.html')
def about():
    return render_template('about.html')
@app.route('/register.html')
def register():
  return render_template('register.html')
@app.route("/register",methods=['post'])
def apply_user_register():
  data = request.form
  #store the data in the database
  #display an ackonelwdgement
  #send an email
  add_information_to_db(data)
  return render_template('register_form.html',
                        register=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
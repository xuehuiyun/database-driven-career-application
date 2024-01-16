from flask import Flask, render_template,jsonify
app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'title': 'Frontend Engineer',
    'location': ' Seattle',
    'salary':'$100,000'
  },
  {
    'id': 2,
    'title': 'Backend Engineer',
    'location': ' Los Angeles',
    'salary':'$100,000'
  },
  {
    'id': 3,
    'title': 'Fullstack Engineer',
    'location': ' San Jose',
    'salary':'$120,000'
  },
  {
    'id': 4,
    'title': 'Frontend Engineer Intern',
    'location': ' Remote'
  },
  {
    'id': 5,
    'title': 'Data Analyst',
    'location': ' New York',
    'salary':'$80,000'
  },
]
@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS)
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
@app.route('/event.html')
def event():
    return render_template('event.html')
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
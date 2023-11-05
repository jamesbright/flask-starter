from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'title': 'Software Engineer',
    'location': 'San Francisco',
    'salary': '$100,000',
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
    'date': 'June 1, 2018',
    'url': 'https://www.example.com/job/1',
    'company': 'Example Company1',
  },
  {
    'id': 1,
    'title': 'Software Engineer',
    'location': 'San Francisco',
    'salary': '$100,000',
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
    'date': 'June 1, 2018',
    'url': 'https://www.example.com/job/1',
    'company': 'Example Company1',
  },
  {
    'id': 1,
    'title': 'Software Engineer',
    'location': 'San Francisco',
    'salary': '$100,000',
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
    'date': 'June 1, 2018',
    'url': 'https://www.example.com/job/1',
    'company': 'Example Company1',
  },
    
]

@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

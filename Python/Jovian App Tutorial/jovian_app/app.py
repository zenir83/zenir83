from flask import Flask, render_template, jsonify, request, url_for
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def home(): 
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs,
                           company_name = 'Koningsoever')
@app.route("/opleidingen")
def opleidingen():
    return render_template('opleidingen.html')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)

    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job = job)

@app.route("/api/job/<id>")
def show_job_json(id):
    job = load_job_from_db(id)
    return jsonify(job)

@app.route("/job/<id>/apply", methods=['post'])

def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', 
                         application=data,
                         job=job)

if __name__== "__main__":
    app.run(host='0.0.0.0', debug=True)
    

    ############################
    #TODO admin loginpage
    # Allow admins to mark appications as accepted/rejected
    # Create a user interface to check application status
    #############################
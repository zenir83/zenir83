from sqlalchemy import create_engine, text

# DEFINE THE DATABASE CREDENTIALS Should be secret!
user = 'root'
password = 'Kauwgomsok83!'
host = '127.0.0.1'
port = 3306
database = 'jovian_app'
 
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


engine = get_connection()

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from vacatures"))
    vacatures = []
    for row in result.all():
      vacatures.append(dict(row._mapping))
    return vacatures

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
       text(f"SELECT * FROM vacatures WHERE id={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return row

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO sollicitaties (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, 
                 job_id=job_id, 
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])
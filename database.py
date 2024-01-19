from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(
  db_connection_string,
  connect_args={
      "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
      }
  }
)
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      row_dict = row._asdict()
      jobs.append(row_dict)
    return jobs

def load_job_from_db(id):
   with engine.connect() as conn:
     result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :job_id"),
      {"job_id": id}
     )
     rows = result.all()
     if len(rows) == 0:
       return None
     else:
       return dict(rows[0]._asdict())
    # print("type(result):", type(result))
    # result_all = result.all()
    # print("type(result.all()):", type(result_all))
    # first_result = result_all[0]
    # print("type(first_result):", type(first_result))
    # first_result_dict = first_result._asdict()
    # print("type(first_result_dict):", type(first_result_dict))
    # print(first_result_dict)
      
    
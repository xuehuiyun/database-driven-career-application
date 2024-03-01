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
def load_dogs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from dogs"))
    dogs = []
    for row in result.all():
      row_dict = row._asdict()
      dogs.append(row_dict)
    return dogs

def load_dog_from_db(id):
  with engine.connect() as conn:
      result = conn.execute(
          text("SELECT * FROM dogs WHERE id = :dog_id"),
          {"dog_id": id}
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
def add_information_to_db(data):
  with engine.connect() as conn:
      query = text("""
      INSERT INTO register(full_name, user_name, password, email, education, work_experience, resume_url) 
      VALUES (:full_name, :user_name, :password, :email, :education, :work_experience, :resume_url)
      """)
      params = {
      'full_name': data['full_name'],
      'user_name': data['user_name'],
      'password': data['password'],
      'email': data['email'],
      'education': data['education'],
      'work_experience': data['work_experience'],
      'resume_url': data['URL']
      }
    # Execute the query with the parameters
      conn.execute(query, params)

  


from dotenv import load_dotenv
import os
load_dotenv()

db_user = os.getenv('MY_SQL_USER')
db_password = os.getenv('MY_SQL_PASSWORD')
db_host = os.getenv('MY_SQL_HOST')


print(db_user)
print(db_password)
print(db_host)
print(os.getenv('MY_SQL_DB'))
print(os.getenv('MY_SQL_PORT'))


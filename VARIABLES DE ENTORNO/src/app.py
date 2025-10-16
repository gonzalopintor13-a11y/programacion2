from decouple import config

print(config('MY_SQL_HOST'))
print(config('MY_SQL_USER'))
print(config('MY_SQL_PASSWORD'))
print(config('MY_SQL_DB'))
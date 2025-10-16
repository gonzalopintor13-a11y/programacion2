from dotenv import dotenv_values

settings = dotenv_values(".env")
print(settings)#devuelve un diccionario

print(settings['MY_SQL_HOST'])


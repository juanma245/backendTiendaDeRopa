import psycopg2


try:
    connection = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = '4rqu1t3ctur4',
    database = 'probadorVirtual'
    )
except Exception as ex:
    print(ex)
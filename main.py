import psycopg2

username = 'postgres'
password = 'postgres'
database = 'lab2_Kostiuk'
host = 'localhost'
port = '5432'


query_1 = '''
select years.year_value, count(years.year_value) from 
films inner join years on films.year_id = years.year_id
group by years.year_value
'''

query_2 = '''
select trim(genres.genre_name), count(genres.genre_name) from
genres inner join films on genres.genre_id = films.genre_id
group by genres.genre_name
'''

query_3 = '''
select trim(directors.director_name), count(directors.director_name) from 
films inner join directors on films.director_id = directors.director_id
group by directors.director_name
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with con:

    cur = con.cursor()

    print('QUERY 1:')
    cur.execute(query_1)
    for row in cur:
      print(row)

    print('\nQUERY 2:')
    cur.execute(query_2)
    for row in cur:
      print(row)

    print('\nQUERY 3:')
    cur.execute(query_3)
    for row in cur:
      print(row)
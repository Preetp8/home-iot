import psycopg2

connect = psycopg2.connect(
    database = "Team1DB",
    user = "Team1",
    password = "team1",
    host = "localhost",
    port = '138.26.48.8:5432'
)

cursor_obj = connect.cursor()
result = cursor_obj.fetchall()
import psycopg2

# ORM

# Connect to the database
conn = psycopg2.connect(
    database="sample",
    user="postgres",
    password="postgrespw",
    host="localhost",
    port="32768"
)

cur = conn.cursor()

# Get the user input
user_id = input("Enter the user ID: ")

# Create a SQL query with the user input
sql_query = "SELECT * FROM users WHERE id = {}".format(user_id)

cur.execute(sql_query)

records = cur.fetchall()

print(records)
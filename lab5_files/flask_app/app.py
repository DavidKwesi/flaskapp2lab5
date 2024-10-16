from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host="redis", port=6379)

mysql_url = os.getenv('MYSQL_URL')
conn = mysql.connector.connect(
    host="mysql",
    user="mysql_user",
    password="mysql_password",
    database="mydatabase"
) 

@app.route("/")
def home():
    count = r.incr("hits")
    return f"This page has been visited {count} times."
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS visit_count (count INT)")
    cursor.execute("INSERT INTO visit_count (count) VALUES (%s)", (count,))
    conn.commit()
    cursor.close()



if __name__ == "__main__":
    app.run(host="0.0.0.0")


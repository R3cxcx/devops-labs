from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Read variables from environment
    app_message = os.getenv("APP_MESSAGE", "Default message")
    db_password = os.getenv("DB_PASSWORD", "No password set")

    return f"""
    <h1>{app_message}</h1>
    <p>Database password: {db_password}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

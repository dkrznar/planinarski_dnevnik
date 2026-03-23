from flask import Flask
import database

app = Flask(__name__)
app.secret_key = "planinarenje"

if __name__ == "__main__":
  app.run(debug = True, host = '0.0.0.0')
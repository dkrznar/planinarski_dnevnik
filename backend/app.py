from flask import Flask, redirect
import database
from routes.izleti_routes import izlet_bp

app = Flask(__name__)
app.secret_key = "planinarenje"

app.register_blueprint(izlet_bp)

@app.route('/')
def index():
  return redirect('/izleti')

if __name__ == "__main__":
  app.run(debug = True, host = '0.0.0.0')
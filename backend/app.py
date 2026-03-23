from flask import Flask, redirect
import database
from routes.planina_routes import planina_bp
from routes.vrh_routes import vrh_bp
from routes.izleti_routes import izlet_bp

app = Flask(__name__)
app.secret_key = "planinarenje"

app.register_blueprint(planina_bp)
app.register_blueprint(vrh_bp)
app.register_blueprint(izlet_bp)

@app.route('/')
def index():
  return redirect('/izleti')

if __name__ == "__main__":
  app.run(debug = True, host = '0.0.0.0')
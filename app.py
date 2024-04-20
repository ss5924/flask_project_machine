from flask import Flask
from business_location import business_location_bp
from vendor import vendor_bp
from machine import machine_bp
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root1234@localhost:3306/term_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(vendor_bp)
app.register_blueprint(business_location_bp)
app.register_blueprint(machine_bp)

db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # host='0.0.0.0',

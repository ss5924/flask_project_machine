from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# 모델 정의
class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor_name = db.Column(db.String(64))
    vendor_address = db.Column(db.String(512))
    vendor_fax = db.Column(db.String(64))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class BusinessLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_location_name = db.Column(db.String(64))
    business_location_address = db.Column(db.String(512))
    business_location_type = db.Column(db.String(64))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


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


class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_location_id = db.Column(db.Integer, db.ForeignKey('business_location.id'))
    machine_name = db.Column(db.String(64))
    machine_type = db.Column(db.String(32))
    manufacturer = db.Column(db.String(64))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # business_location = db.relationship('BusinessLocation', backref=db.backref('machines', lazy=True))
    business_location = db.relationship('BusinessLocation', backref=db.backref('machines', lazy='joined'))


"""
*** lazy 옵션 ***
 
select (기본값): 관계에 접근할 때마다 관련 객체를 별도의 쿼리로 로드
joined: 관련 객체를 로드할 때 조인을 사용하여 관계를 가진 모든 데이터를 단일 쿼리로 로드
subquery: 관련 객체를 로드할 때 서브쿼리를 사용
dynamic: 관계를 위한 특별한 쿼리 객체를 생성하며, 실제로 접근하기 전까지는 쿼리를 실행하지 않음

"""

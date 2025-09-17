
from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    transmission = db.Column(db.String(20))
    vehicle_type = db.Column(db.String(20))  # Carro ou Moto
    daily_rate = db.Column(db.Float, nullable=False)
    people_capacity = db.Column(db.Integer)
    image_url = db.Column(db.String(200))
    last_revision = db.Column(db.String(20))
    next_revision = db.Column(db.String(20))
    last_inspection = db.Column(db.String(20))

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    vehicle_id = db.Column(db.Integer)
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    total_price = db.Column(db.Float)

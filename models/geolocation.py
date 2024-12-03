from app import db 

class Geolocation(db.Model):
    __tablename__ = 'geolocation'
    
    geolocation_zip_code_prefix = db.Column(db.Integer, primary_key=True)
    geolocation_lat = db.Column(db.Float, nullable=False)
    geolocation_lng = db.Column(db.Float, nullable=False)
    geolocation_city = db.Column(db.String(50), nullable=False)
    geolocation_state = db.Column(db.String(50), nullable=False)

from flask import Blueprint
from models.geolocation import Geolocation
from app import db

geolocation_bp = Blueprint('geolocation', __name__)

@geolocation_bp.route('/geolocation', methods=['GET'])
def get_geolocation():
    # Perform the query on the Geolocation model
    t = db.session.query(Geolocation).with_entities(
        Geolocation.geolocation_zip_code_prefix,
        Geolocation.geolocation_lat,
        Geolocation.geolocation_lng,
        Geolocation.geolocation_city,
        Geolocation.geolocation_state
    )
    
    # Prepare the response
    ls = []
    for v in t:
        te = {
            "zip_code_prefix": v.geolocation_zip_code_prefix,
            "lat": v.geolocation_lat,
            "lng": v.geolocation_lng,
            "city": v.geolocation_city,
            "state": v.geolocation_state
        }
        ls.append(te)
    
    return ls

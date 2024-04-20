from flask import Blueprint, jsonify, request
from models import db, BusinessLocation

business_location_bp = Blueprint('business_location', __name__)


@business_location_bp.route('/business_location', methods=['POST'])
def add_business_location():
    data = request.get_json()
    new_location = BusinessLocation(
        business_location_name=data['business_location_name'],
        business_location_address=data['business_location_address'],
        business_location_type=data['business_location_type']
    )
    db.session.add(new_location)
    db.session.commit()
    return jsonify({'message': 'Business location created successfully'}), 201


@business_location_bp.route('/business_location/<int:id>', methods=['GET'])
def get_business_location(id):
    location = BusinessLocation.query.get(id)
    if not location:
        return jsonify({'message': 'Business location not found'}), 404
    result = {
        'business_location_name': location.business_location_name,
        'business_location_address': location.business_location_address,
        'business_location_type': location.business_location_type
    }
    return jsonify(result)


@business_location_bp.route('/business_location/<int:id>', methods=['PUT'])
def update_business_location(id):
    location = BusinessLocation.query.get(id)
    if not location:
        return jsonify({'message': 'Business location not found'}), 404
    data = request.get_json()
    location.business_location_name = data.get('business_location_name', location.business_location_name)
    location.business_location_address = data.get('business_location_address', location.business_location_address)
    location.business_location_type = data.get('business_location_type', location.business_location_type)
    db.session.commit()
    return jsonify({'message': 'Business location updated successfully'})


@business_location_bp.route('/business_location/<int:id>', methods=['DELETE'])
def delete_business_location(id):
    location = BusinessLocation.query.get(id)
    if not location:
        return jsonify({'message': 'Business location not found'}), 404
    db.session.delete(location)
    db.session.commit()
    return jsonify({'message': 'Business location deleted successfully'})

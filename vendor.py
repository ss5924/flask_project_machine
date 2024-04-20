from flask import Blueprint, jsonify, request
from models import db, Vendor

vendor_bp = Blueprint('vendor', __name__)


@vendor_bp.route('/vendor', methods=['POST'])
def add_vendor():
    data = request.get_json()
    new_vendor = Vendor(vendor_name=data['vendor_name'], vendor_address=data['vendor_address'],
                        vendor_fax=data['vendor_fax'])
    db.session.add(new_vendor)
    db.session.commit()
    return jsonify({'message': 'Vendor created successfully'}), 201


@vendor_bp.route('/vendor/<int:id>', methods=['GET'])
def get_vendor(id):
    vendor = Vendor.query.get(id)
    if not vendor:
        return jsonify({'message': 'No vendor found'}), 404
    return jsonify(
        {'vendor_name': vendor.vendor_name, 'vendor_address': vendor.vendor_address, 'vendor_fax': vendor.vendor_fax})


@vendor_bp.route('/vendor/<int:id>', methods=['PUT'])
def update_vendor(id):
    vendor = Vendor.query.get(id)
    if not vendor:
        return jsonify({'message': 'No vendor found'}), 404
    data = request.get_json()
    vendor.vendor_name = data.get('vendor_name', vendor.vendor_name)
    vendor.vendor_address = data.get('vendor_address', vendor.vendor_address)
    vendor.vendor_fax = data.get('vendor_fax', vendor.vendor_fax)
    db.session.commit()
    return jsonify({'message': 'Vendor updated successfully'})


@vendor_bp.route('/vendor/<int:id>', methods=['DELETE'])
def delete_vendor(id):
    vendor = Vendor.query.get(id)
    if not vendor:
        return jsonify({'message': 'No vendor found'}), 404
    db.session.delete(vendor)
    db.session.commit()
    return jsonify({'message': 'Vendor deleted successfully'})

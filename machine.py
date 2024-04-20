from flask import Blueprint, jsonify, request
from models import db, Machine

machine_bp = Blueprint('machine', __name__)


@machine_bp.route('/machine', methods=['POST'])
def add_machine():
    data = request.get_json()
    new_machine = Machine(
        business_location_id=data['business_location_id'],
        machine_name=data['machine_name'],
        machine_type=data['machine_type'],
        manufacturer=data['manufacturer']
    )
    db.session.add(new_machine)
    db.session.commit()
    return jsonify({'message': 'Machine created successfully'}), 201


@machine_bp.route('/machine/<int:id>', methods=['GET'])
def get_machine(id):
    machine = Machine.query.get(id)
    if not machine:
        return jsonify({'message': 'Machine not found'}), 404
    result = {
        'machine_name': machine.machine_name,
        'machine_type': machine.machine_type,
        'manufacturer': machine.manufacturer,
        'business_location': {
            'id': machine.business_location.id,
            'business_location_name': machine.business_location.business_location_name,
            'business_location_address': machine.business_location.business_location_address,
            'business_location_type': machine.business_location.business_location_type
        }
    }
    return jsonify(result)


@machine_bp.route('/machine/<int:id>', methods=['PUT'])
def update_machine(id):
    machine = Machine.query.get(id)
    if not machine:
        return jsonify({'message': 'Machine not found'}), 404
    data = request.get_json()
    machine.business_location_id = data.get('business_location_id', machine.business_location_id)
    machine.machine_name = data.get('machine_name', machine.machine_name)
    machine.machine_type = data.get('machine_type', machine.machine_type)
    machine.manufacturer = data.get('manufacturer', machine.manufacturer)
    db.session.commit()
    return jsonify({'message': 'Machine updated successfully'})


@machine_bp.route('/machine/<int:id>', methods=['DELETE'])
def delete_machine(id):
    machine = Machine.query.get(id)
    if not machine:
        return jsonify({'message': 'Machine not found'}), 404
    db.session.delete(machine)
    db.session.commit()
    return jsonify({'message': 'Machine deleted successfully'})

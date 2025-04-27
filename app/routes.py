from flask import Blueprint, jsonify, request
from .models import Incident
from .database import db
from sqlalchemy.exc import SQLAlchemyError

# Create main blueprint for root route
main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def root():
    return jsonify({
        "message": "Backend of Incident-log-api",
        "status": "success",
        "endpoints": {
            "incidents": "/incidents",
            "create_incident": "/incidents (POST)",
            "get_incident": "/incidents/<id>",
            "delete_incident": "/incidents/<id> (DELETE)"
        }
    }), 200

# Create incidents blueprint
incidents_bp = Blueprint('incidents', __name__, url_prefix='/incidents')

VALID_SEVERITIES = ["Low", "Medium", "High"]

@incidents_bp.route('', methods=['GET'])
def get_incidents():
    try:
        incidents = Incident.query.all()
        return jsonify([{
            "id": i.id,
            "title": i.title,
            "description": i.description,
            "severity": i.severity,
            "reported_at": i.reported_at.isoformat()
        } for i in incidents]), 200
    except SQLAlchemyError:
        return jsonify({"error": "Database error occurred"}), 500

@incidents_bp.route('', methods=['POST'])
def create_incident():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        title = data.get('title')
        description = data.get('description')
        severity = data.get('severity')

        if not title or not description:
            return jsonify({"error": "Title and description are required"}), 400
        
        if severity not in VALID_SEVERITIES:
            return jsonify({"error": f"Severity must be one of: {', '.join(VALID_SEVERITIES)}"}), 400

        new_incident = Incident(title=title, description=description, severity=severity)
        db.session.add(new_incident)
        db.session.commit()

        return jsonify({
            "id": new_incident.id,
            "title": new_incident.title,
            "description": new_incident.description,
            "severity": new_incident.severity,
            "reported_at": new_incident.reported_at.isoformat()
        }), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Failed to create incident"}), 500

@incidents_bp.route('/<int:id>', methods=['GET'])
def get_incident(id):
    try:
        incident = Incident.query.get(id)
        if not incident:
            return jsonify({"error": f"Incident with id {id} not found"}), 404
        
        return jsonify({
            "id": incident.id,
            "title": incident.title,
            "description": incident.description,
            "severity": incident.severity,
            "reported_at": incident.reported_at.isoformat()
        }), 200
    except SQLAlchemyError:
        return jsonify({"error": "Database error occurred"}), 500

@incidents_bp.route('/<int:id>', methods=['DELETE'])
def delete_incident(id):
    try:
        incident = Incident.query.get(id)
        if not incident:
            return jsonify({"error": f"Incident with id {id} not found"}), 404

        db.session.delete(incident)
        db.session.commit()
        return '', 204
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Failed to delete incident"}), 500

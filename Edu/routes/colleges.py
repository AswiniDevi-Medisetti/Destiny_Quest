from flask import Blueprint, request, jsonify
from models.colleges import CollegeModel

colleges_bp = Blueprint('colleges', __name__)

def init_colleges_routes(app, mongo):
    college_model = CollegeModel(mongo)
    
    @colleges_bp.route('/api/colleges', methods=['GET'])
    def get_all_colleges():
        """Get all colleges"""
        try:
            colleges = college_model.get_all_colleges()
            
            # Convert ObjectId to string
            for college in colleges:
                college['_id'] = str(college['_id'])
            
            return jsonify({
                'success': True,
                'colleges': colleges
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    @colleges_bp.route('/api/colleges/<college_type>', methods=['GET'])
    def get_colleges_by_type(college_type):
        """Get colleges by type"""
        try:
            colleges = college_model.get_colleges_by_type(college_type)
            
            # Convert ObjectId to string
            for college in colleges:
                college['_id'] = str(college['_id'])
            
            return jsonify({
                'success': True,
                'type': college_type,
                'colleges': colleges
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    @colleges_bp.route('/api/college/<college_id>', methods=['GET'])
    def get_college_details(college_id):
        """Get detailed information about a specific college"""
        try:
            college = college_model.get_college_details(college_id)
            
            if not college:
                return jsonify({
                    'success': False,
                    'error': 'College not found'
                }), 404
            
            # Convert ObjectId to string
            college['_id'] = str(college['_id'])
            if 'courses' in college:
                for course in college['courses']:
                    course['_id'] = str(course['_id'])
            
            return jsonify({
                'success': True,
                'college': college
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    return colleges_bp
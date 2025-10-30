from flask import Blueprint, request, jsonify
from models.resources import ResourceModel

resources_bp = Blueprint('resources', __name__)

def init_resources_routes(app, mongo):
    resource_model = ResourceModel(mongo)
    
    @resources_bp.route('/api/resources/course/<course_id>', methods=['GET'])
    def get_course_resources(course_id):
        """Get all resources for a course"""
        try:
            resources = resource_model.get_resources_by_course(course_id)
            
            # Convert ObjectId to string
            for resource in resources:
                resource['_id'] = str(resource['_id'])
                resource['course_id'] = str(resource['course_id'])
            
            return jsonify({
                'success': True,
                'course_id': course_id,
                'resources': resources
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    @resources_bp.route('/api/resource/<resource_id>/view', methods=['POST'])
    def increment_resource_views(resource_id):
        """Increment resource view count"""
        try:
            result = resource_model.increment_view_count(resource_id)
            
            if result.modified_count == 0:
                return jsonify({
                    'success': False,
                    'error': 'Resource not found'
                }), 404
            
            return jsonify({
                'success': True,
                'message': 'View count updated'
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    return resources_bp
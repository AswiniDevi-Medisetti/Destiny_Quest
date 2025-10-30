from flask import Blueprint, request, jsonify
from models.courses import CourseModel
from bson import ObjectId

courses_bp = Blueprint('courses', __name__)

def init_courses_routes(app, mongo):
    course_model = CourseModel(mongo)
    
    @courses_bp.route('/api/stages', methods=['GET'])
    def get_stages():
        """Get all educational stages"""
        try:
            stages = course_model.get_all_stages()
            return jsonify({
                'success': True,
                'stages': stages
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    @courses_bp.route('/api/courses/<stage>', methods=['GET'])
    def get_courses_by_stage(stage):
        """Get courses by educational stage"""
        try:
            courses = course_model.get_courses_by_stage(stage)
            
            # Convert ObjectId to string for JSON serialization
            for course in courses:
                course['_id'] = str(course['_id'])
                if 'colleges' in course:
                    for college in course['colleges']:
                        college['_id'] = str(college['_id'])
                if 'resources' in course:
                    for resource in course['resources']:
                        resource['_id'] = str(resource['_id'])
            
            return jsonify({
                'success': True,
                'stage': stage,
                'courses': courses
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    @courses_bp.route('/api/course/<course_id>', methods=['GET'])
    def get_course_details(course_id):
        """Get detailed information about a specific course"""
        try:
            course = course_model.get_course_details(course_id)
            
            if not course:
                return jsonify({
                    'success': False,
                    'error': 'Course not found'
                }), 404
            
            # Convert ObjectId to string
            course['_id'] = str(course['_id'])
            if 'colleges' in course:
                for college in course['colleges']:
                    college['_id'] = str(college['_id'])
            if 'resources' in course:
                for resource in course['resources']:
                    resource['_id'] = str(resource['_id'])
            
            return jsonify({
                'success': True,
                'course': course
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    @courses_bp.route('/api/courses/search', methods=['GET'])
    def search_courses():
        """Search courses"""
        try:
            query = request.args.get('q', '')
            if not query:
                return jsonify({
                    'success': False,
                    'error': 'Query parameter is required'
                }), 400
            
            courses = course_model.search_courses(query)
            
            # Convert ObjectId to string
            for course in courses:
                course['_id'] = str(course['_id'])
            
            return jsonify({
                'success': True,
                'query': query,
                'courses': courses
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    return courses_bp
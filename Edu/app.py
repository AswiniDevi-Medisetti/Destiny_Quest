from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '4f5d8e3a9c2b1f7e6d8a0c4e9b2f5d8e3a9c2b1f7e6d8a0c4e9b2f5d8e3a9c2'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/destiny_quest'

# Initialize MongoDB
mongo = PyMongo(app)

def is_database_connected():
    """Check if MongoDB is connected"""
    try:
        mongo.db.list_collection_names()
        return True
    except Exception:
        return False

# Course Model Functions
def get_all_stages():
    try:
        return list(mongo.db.courses.distinct("stage"))
    except Exception as e:
        print(f"Error getting stages: {e}")
        return []

def get_courses_by_stage(stage):
    try:
        pipeline = [
            {"$match": {"stage": stage}},
            {"$lookup": {
                "from": "colleges",
                "localField": "college_ids",
                "foreignField": "_id",
                "as": "colleges"
            }},
            {"$lookup": {
                "from": "resources",
                "localField": "resource_ids",
                "foreignField": "_id",
                "as": "resources"
            }}
        ]
        courses = list(mongo.db.courses.aggregate(pipeline))
        
        # Convert ObjectId to string for JSON serialization
        for course in courses:
            course['_id'] = str(course['_id'])
            if 'colleges' in course:
                for college in course['colleges']:
                    college['_id'] = str(college['_id'])
            if 'resources' in course:
                for resource in course['resources']:
                    resource['_id'] = str(resource['_id'])
        
        return courses
    except Exception as e:
        print(f"Error getting courses for stage {stage}: {e}")
        return []

def get_course_details(course_id):
    try:
        pipeline = [
            {"$match": {"_id": ObjectId(course_id)}},
            {"$lookup": {
                "from": "colleges",
                "localField": "college_ids",
                "foreignField": "_id",
                "as": "colleges"
            }},
            {"$lookup": {
                "from": "resources",
                "localField": "resource_ids",
                "foreignField": "_id",
                "as": "resources"
            }}
        ]
        result = list(mongo.db.courses.aggregate(pipeline))
        
        if result:
            course = result[0]
            course['_id'] = str(course['_id'])
            if 'colleges' in course:
                for college in course['colleges']:
                    college['_id'] = str(college['_id'])
            if 'resources' in course:
                for resource in course['resources']:
                    resource['_id'] = str(resource['_id'])
            return course
        return None
    except Exception as e:
        print(f"Error getting course details: {e}")
        return None

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    try:
        database_status = 'connected' if is_database_connected() else 'disconnected'
        return jsonify({
            'status': 'healthy',
            'database': database_status
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500

@app.route('/api/stages')
def get_stages():
    try:
        stages = get_all_stages()
        return jsonify({
            'success': True,
            'stages': stages
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/courses/<stage>')
def get_courses_by_stage_route(stage):
    try:
        courses = get_courses_by_stage(stage)
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

@app.route('/api/course/<course_id>')
def get_course_details_route(course_id):
    try:
        course = get_course_details(course_id)
        if not course:
            return jsonify({
                'success': False,
                'error': 'Course not found'
            }), 404
        
        return jsonify({
            'success': True,
            'course': course
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/search/courses')
def search_courses():
    try:
        query = request.args.get('q', '')
        if not query:
            return jsonify({
                'success': False,
                'error': 'Query parameter is required'
            }), 400
        
        courses = list(mongo.db.courses.find({
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"description": {"$regex": query, "$options": "i"}},
                {"subjects": {"$regex": query, "$options": "i"}}
            ]
        }))
        
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

def initialize_database():
    """Initialize database with sample data if empty"""
    try:
        if mongo.db.courses.count_documents({}) == 0:
            print("Database is empty. Inserting sample data...")
            from sample_data import insert_sample_data
            insert_sample_data()
            print("Sample data inserted successfully!")
        else:
            print("Database already contains data.")
    except Exception as e:
        print(f"Error initializing database: {e}")

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("Created templates directory")
    
    # Initialize database
    with app.app_context():
        initialize_database()
    
    print("Starting Destiny Quest application...")
    print("Access the application at: http://localhost:5000")
    app.run(debug=False, host='0.0.0.0', port=5000)
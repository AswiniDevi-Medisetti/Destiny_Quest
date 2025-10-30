from flask_pymongo import PyMongo
from bson import ObjectId
from datetime import datetime

class CourseModel:
    def __init__(self, mongo):
        self.mongo = mongo
        self.courses = mongo.db.courses
        self.colleges = mongo.db.colleges
        self.resources = mongo.db.resources

    def get_all_stages(self):
        """Get all educational stages"""
        return list(self.courses.distinct("stage"))

    def get_courses_by_stage(self, stage):
        """Get all courses for a specific educational stage"""
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
        return list(self.courses.aggregate(pipeline))

    def get_course_details(self, course_id):
        """Get complete details for a specific course"""
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
        result = list(self.courses.aggregate(pipeline))
        return result[0] if result else None

    def search_courses(self, query):
        """Search courses by name, description, or subjects"""
        return list(self.courses.find({
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"description": {"$regex": query, "$options": "i"}},
                {"subjects": {"$regex": query, "$options": "i"}}
            ]
        }))

    def add_course(self, course_data):
        """Add a new course to the database"""
        course_data['created_at'] = datetime.utcnow()
        course_data['updated_at'] = datetime.utcnow()
        result = self.courses.insert_one(course_data)
        return str(result.inserted_id)

    def update_course(self, course_id, update_data):
        """Update course information"""
        update_data['updated_at'] = datetime.utcnow()
        return self.courses.update_one(
            {"_id": ObjectId(course_id)},
            {"$set": update_data}
        )

    def delete_course(self, course_id):
        """Delete a course from the database"""
        return self.courses.delete_one({"_id": ObjectId(course_id)})
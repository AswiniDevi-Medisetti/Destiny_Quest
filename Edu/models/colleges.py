from bson import ObjectId
from datetime import datetime

class CollegeModel:
    def __init__(self, mongo):
        self.mongo = mongo
        self.colleges = mongo.db.colleges

    def get_all_colleges(self):
        """Get all colleges"""
        return list(self.colleges.find())

    def get_colleges_by_type(self, college_type):
        """Get colleges by type (government/private)"""
        return list(self.colleges.find({"type": college_type}))

    def get_colleges_by_course(self, course_id):
        """Get colleges offering a specific course"""
        return list(self.colleges.find({"course_ids": ObjectId(course_id)}))

    def get_college_details(self, college_id):
        """Get complete details for a specific college"""
        pipeline = [
            {"$match": {"_id": ObjectId(college_id)}},
            {"$lookup": {
                "from": "courses",
                "localField": "course_ids",
                "foreignField": "_id",
                "as": "courses"
            }}
        ]
        result = list(self.colleges.aggregate(pipeline))
        return result[0] if result else None

    def search_colleges(self, query):
        """Search colleges by name, location, or courses"""
        return list(self.colleges.find({
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"location": {"$regex": query, "$options": "i"}},
                {"courses_offered": {"$regex": query, "$options": "i"}}
            ]
        }))

    def add_college(self, college_data):
        """Add a new college to the database"""
        college_data['created_at'] = datetime.utcnow()
        college_data['updated_at'] = datetime.utcnow()
        result = self.colleges.insert_one(college_data)
        return str(result.inserted_id)
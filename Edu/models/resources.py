from bson import ObjectId
from datetime import datetime

class ResourceModel:
    def __init__(self, mongo):
        self.mongo = mongo
        self.resources = mongo.db.resources

    def get_resources_by_course(self, course_id):
        """Get all resources for a specific course"""
        return list(self.resources.find({"course_id": ObjectId(course_id)}))

    def get_resources_by_type(self, resource_type):
        """Get resources by type (youtube, article, etc.)"""
        return list(self.resources.find({"type": resource_type}))

    def add_resource(self, resource_data):
        """Add a new resource"""
        resource_data['created_at'] = datetime.utcnow()
        result = self.resources.insert_one(resource_data)
        return str(result.inserted_id)

    def increment_view_count(self, resource_id):
        """Increment view count for a resource"""
        return self.resources.update_one(
            {"_id": ObjectId(resource_id)},
            {"$inc": {"view_count": 1}}
        )
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

def insert_sample_data():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client.destiny_quest
        
        # Clear existing data
        db.courses.delete_many({})
        db.colleges.delete_many({})
        db.resources.delete_many({})
        
        print("Cleared existing data...")
        
        # Sample courses data
        courses = [
            {
                "name": "Science (MPC)",
                "stage": "after10th",
                "description": "Mathematics, Physics, Chemistry stream for engineering and technical fields",
                "duration": "2 years",
                "subjects": ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"],
                "career_opportunities": ["Engineering", "Architecture", "Research", "Data Science"],
                "entrance_exams": ["JEE Main", "JEE Advanced", "BITSAT", "VITEEE"],
                "avg_fees": "₹20,000 - ₹1,00,000 per year",
                "market_demand": "High",
                "created_at": datetime.utcnow()
            },
            {
                "name": "Medical (BiPC)",
                "stage": "after10th",
                "description": "Biology, Physics, Chemistry stream for medical and life sciences",
                "duration": "2 years",
                "subjects": ["Biology", "Physics", "Chemistry", "English", "Mathematics"],
                "career_opportunities": ["Doctor", "Dentist", "Pharmacist", "Biotechnologist"],
                "entrance_exams": ["NEET", "AIIMS", "JIPMER"],
                "avg_fees": "₹30,000 - ₹1,50,000 per year",
                "market_demand": "High",
                "created_at": datetime.utcnow()
            },
            {
                "name": "Commerce",
                "stage": "after10th",
                "description": "Commerce stream for business, finance, and accounting careers",
                "duration": "2 years",
                "subjects": ["Accountancy", "Business Studies", "Economics", "Mathematics", "English"],
                "career_opportunities": ["Chartered Accountant", "Company Secretary", "Business Manager", "Banking"],
                "entrance_exams": ["CUET", "University Entrance Tests"],
                "avg_fees": "₹15,000 - ₹80,000 per year",
                "market_demand": "High",
                "created_at": datetime.utcnow()
            },
            {
                "name": "Engineering - Computer Science",
                "stage": "after12th",
                "description": "Bachelor of Technology in Computer Science and Engineering",
                "duration": "4 years",
                "subjects": ["Programming", "Data Structures", "Algorithms", "Database Management", "Web Development"],
                "career_opportunities": ["Software Engineer", "Data Scientist", "Web Developer", "AI Engineer"],
                "entrance_exams": ["JEE Main", "JEE Advanced", "BITSAT", "State CETs"],
                "avg_fees": "₹1,00,000 - ₹5,00,000 per year",
                "market_demand": "Very High",
                "created_at": datetime.utcnow()
            }
        ]
        
        # Insert courses and get their IDs
        course_ids = []
        for course in courses:
            result = db.courses.insert_one(course)
            course_ids.append(result.inserted_id)
        
        print(f"Inserted {len(course_ids)} courses")
        
        # Sample colleges data
        colleges = [
            {
                "name": "Narayana Junior College",
                "type": "private",
                "location": "Hyderabad, Telangana",
                "courses_offered": ["Science (MPC)", "Medical (BiPC)", "Commerce"],
                "fees_range": "₹50,000 - ₹1,20,000 per year",
                "facilities": ["Library", "Laboratories", "Hostel", "Sports"],
                "placement_support": True,
                "website": "https://www.narayanagroup.com",
                "contact_email": "info@narayanagroup.com",
                "phone": "+91-40-12345678",
                "course_ids": course_ids[:3],
                "created_at": datetime.utcnow()
            },
            {
                "name": "Sri Chaitanya Junior College",
                "type": "private",
                "location": "Hyderabad, Telangana",
                "courses_offered": ["Science (MPC)", "Medical (BiPC)", "Commerce", "Arts"],
                "fees_range": "₹40,000 - ₹1,00,000 per year",
                "facilities": ["Digital Classrooms", "Labs", "Hostel", "Transport"],
                "placement_support": True,
                "website": "https://srichaitanya.net",
                "contact_email": "info@srichaitanya.net",
                "phone": "+91-40-87654321",
                "course_ids": course_ids[:3],
                "created_at": datetime.utcnow()
            }
        ]
        
        college_ids = []
        for college in colleges:
            result = db.colleges.insert_one(college)
            college_ids.append(result.inserted_id)
        
        print(f"Inserted {len(college_ids)} colleges")
        
        # Sample resources data
        resources = [
            {
                "title": "Complete Physics Tutorial for 11th Grade",
                "type": "youtube",
                "url": "https://youtube.com/playlist?list=PLABC123",
                "description": "Comprehensive physics course covering all chapters",
                "duration": "45 hours",
                "views": 15000,
                "rating": 4.8,
                "course_id": course_ids[0],
                "chapters": ["Units and Measurements", "Motion", "Laws of Motion", "Work and Energy"],
                "created_at": datetime.utcnow()
            },
            {
                "title": "Chemistry Fundamentals Guide",
                "type": "article",
                "url": "https://example.com/chemistry-guide",
                "description": "Detailed article on basic chemistry concepts",
                "author": "Dr. Science",
                "course_id": course_ids[0],
                "reading_time": "15 minutes",
                "created_at": datetime.utcnow()
            }
        ]
        
        resource_ids = []
        for resource in resources:
            result = db.resources.insert_one(resource)
            resource_ids.append(result.inserted_id)
        
        print(f"Inserted {len(resource_ids)} resources")
        
        # Update courses with college and resource IDs
        db.courses.update_one(
            {"_id": course_ids[0]},
            {"$set": {
                "college_ids": college_ids,
                "resource_ids": resource_ids
            }}
        )
        
        db.courses.update_one(
            {"_id": course_ids[1]},
            {"$set": {
                "college_ids": college_ids,
                "resource_ids": []
            }}
        )
        
        db.courses.update_one(
            {"_id": course_ids[2]},
            {"$set": {
                "college_ids": college_ids,
                "resource_ids": []
            }}
        )
        
        db.courses.update_one(
            {"_id": course_ids[3]},
            {"$set": {
                "college_ids": [],
                "resource_ids": []
            }}
        )
        
        print("Sample data inserted successfully!")
        return True
        
    except Exception as e:
        print(f"Error inserting sample data: {e}")
        return False

if __name__ == "__main__":
    insert_sample_data()
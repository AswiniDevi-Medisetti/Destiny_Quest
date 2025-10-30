# Destiny_Quest
1st year Hackthon Mini Project
# Destiny Quest - Educational Roadmap Platform

![Destiny Quest](https://img.shields.io/badge/Version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Flask](https://img.shields.io/badge/Flask-2.3.3-red)
![MongoDB](https://img.shields.io/badge/MongoDB-5.0%2B-green)

## 🎯 Project Overview

**Destiny Quest** is a comprehensive educational roadmap platform designed to guide students from 10th grade through Master's degree with detailed information on courses, colleges, career paths, and learning resources. Originally developed as a mini-project for 2022 1st Year Hackathon, it has evolved into a full-fledged educational guidance system.

---

## 🚀 Current Features (Hackathon MVP)

### 🎓 **Educational Roadmaps**
- **After 10th Grade**: Science (MPC/BiPC), Commerce, Arts streams
- **After 12th Grade**: Engineering, Medical, Commerce, Arts undergraduate programs
- **After Graduation**: Master's degrees, Professional courses, Research programs

### 📚 **Course Information**
- Complete course details and descriptions
- Subjects and curriculum structure
- Career opportunities and market demand
- Duration and fee structures
- Entrance exam requirements

### 🏫 **College Database**
- Government and private colleges
- Location-based filtering
- Facilities and infrastructure details
- Contact information and websites
- Placement support information

### 📖 **Learning Resources**
- YouTube video playlists
- Educational articles and guides
- Online course recommendations
- Study materials and practice tests
- Chapter-wise learning resources

### 🎨 **User Experience**
- Responsive design for all devices
- Modern gradient UI with animations
- Interactive course cards and modals
- Smooth navigation and transitions
- Professional color scheme

### 🔧 **Technical Stack**
- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Flask (Python)
- **Database**: MongoDB
- **Styling**: Custom CSS with CSS Variables
- **Icons**: Emoji and Unicode symbols

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- MongoDB 5.0+
- pip package manager

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/destiny-quest.git
   cd destiny-quest
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   ```bash
   # Create .env file
   echo "SECRET_KEY=your_generated_secret_key_here" > .env
   echo "MONGO_URI=mongodb://localhost:27017/destiny_quest" >> .env
   ```

5. **Generate Secret Key**
   ```python
   import secrets
   print(f"Your secret key: {secrets.token_hex(32)}")
   ```

6. **Initialize Database**
   ```bash
   python sample_data.py
   ```

7. **Run the Application**
   ```bash
   python app.py
   ```

8. **Access the Application**
   Open `http://localhost:5000` in your browser

---

## 📁 Project Structure

```
destiny-quest/
├── app.py                 # Main Flask application
├── sample_data.py         # Database initialization script
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── templates/
│   └── index.html        # Main HTML template
└── README.md             # Project documentation
```

---

## 🔮 Future Enhancements (Complete Version)

### 🎯 **Advanced Features Planned**

#### 🔐 **User Management System**
- Student registration and profiles
- Parent and teacher accounts
- Role-based access control
- Progress tracking and bookmarks

#### 🧠 **AI-Powered Recommendations**
- **Career Prediction Engine**: AI-based career suggestions
- **Skill Gap Analysis**: Identify missing skills for desired careers
- **Personalized Roadmaps**: Custom learning paths based on interests
- **College Recommendation System**: Smart college matching

#### 💼 **Career Development**
- **Internship Portal**: Connect with companies
- **Scholarship Database**: National and international opportunities
- **Industry Partnerships**: Corporate collaborations
- **Mentorship Program**: Connect with industry experts

#### 📊 **Advanced Analytics**
- **Career Growth Tracker**: Progress monitoring
- **Market Trend Analysis**: Job market insights
- **Salary Predictions**: Industry-wise compensation data
- **Success Probability Calculator**: Career success metrics

#### 🌐 **Social Features**
- **Student Community Forum**: Peer discussions
- **Expert Q&A Sessions**: Live interactions
- **Study Groups**: Collaborative learning
- **Success Stories**: Alumni testimonials

#### 📱 **Mobile & Cross-Platform**
- **Mobile App**: iOS and Android applications
- **Progressive Web App**: Offline functionality
- **Desktop Application**: Electron-based desktop app
- **API Development**: RESTful API for third-party integrations

#### 🎓 **Enhanced Educational Content**
- **Live Classes**: Virtual classroom integration
- **Skill Development Courses**: Certifications and workshops
- **Competitive Exam Preparation**: Comprehensive test series
- **International Education**: Study abroad guidance

#### 🔍 **Advanced Search & Filters**
- **Smart Search**: Natural language processing
- **Advanced Filtering**: Multiple criteria combinations
- **Location Intelligence**: Geographic recommendations
- **Cost Optimization**: Budget-based suggestions

#### 📈 **Institutional Features**
- **College Admin Panel**: Institution management
- **Analytics Dashboard**: Student engagement metrics
- **Bulk Operations**: Mass student management
- **Reporting System**: Detailed analytics and reports

---

## 🏆 Hackathon Achievement

### 🥇 **2022 1st Year Hackathon - Mini Project**
- **Category**: Educational Technology
- **Position**: Top 3 Finalists
- **Innovation**: Comprehensive educational roadmap system
- **Impact**: Direct guidance for career decision-making

### 🎯 **What Made It Stand Out**
- **Complete Ecosystem**: End-to-end educational guidance
- **User-Centric Design**: Intuitive and engaging interface
- **Scalable Architecture**: Modular and extensible codebase
- **Real-World Impact**: Practical solution for students

---

## 🚀 Quick Start for Developers

### Basic Setup
```bash
# 1. Install MongoDB
# 2. Run MongoDB service
mongod

# 3. Set up Python environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 4. Install dependencies
pip install flask flask-pymongo pymongo python-dotenv

# 5. Run the application
python app.py
```

### Environment Configuration
```python
# .env file
SECRET_KEY=your_secure_secret_key_here
MONGO_URI=mongodb://localhost:27017/destiny_quest
DEBUG=False
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Areas
- Frontend enhancements
- Backend API development
- Database optimization
- New feature implementation
- Documentation improvements

---

## 📞 Support & Contact

- **Email**: support@destinyquest.com
- **Website**: https://destinyquest.com
- **Documentation**: https://docs.destinyquest.com
- **Issues**: GitHub Issues Page

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎉 Acknowledgments

- **Mentors**: Hackathon guidance team
- **Contributors**: All developers and testers
- **Institutions**: Educational partners
- **Open Source**: Community libraries and tools

---

**Destiny Quest** - *Shaping Futures, One Student at a Time* 🚀

---

*Last Updated: October 2023*  
*Version: 1.0.0*  
*Built with ❤️ for the Student Community*

# **PuliKidz API System**  

## **Overview**  
The **PuliKidz API** is a powerful system that provides secure user authentication, real-time communication, student and teacher interactions, and course management functionalities. It streamlines childcare and education management while ensuring compliance with government regulations.  

## **Technologies Used**  
- **Backend:** Python, Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Authentication:** Django Token  
- **Real-Time Communication:** Django Channels, WebSockets  
- **Deployment:** PythonAnywhere  

---

## **API Endpoints**  

### **1. Account Management (Authentication)**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST**   | `/account/account/teacher/registration/` | Register as a teacher |
| **POST**   | `/account/account/student/registration/` | Register as a student |
| **POST**   | `/account/login/` | Login and obtain Django authentication token |
| **GET**    | `/account/logout/` | Logout user |

---

### **2. Messaging (Real-Time Chat)**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET**    | `/message/` | Retrieve all user conversations |
| **POST**   | `/message/` | Send a new message |
| **PUT**    | `/message/<message_id>/` | Update a message |
| **DELETE** | `/message/delete/<message_id>/` | Delete a message |

---

### **3. Student Management**  

#### **a. Post on Home Page**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET**    | `/student/post/` | Retrieve all posts |
| **POST**   | `/student/post/` | Create a new post |
| **PUT**    | `/student/post/<post_id>/` | Update a post |
| **DELETE** | `/student/post/<post_id>/` | Delete a post |

#### **b. Feedback System**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET**    | `/student/feedback/` | Retrieve all feedback |
| **POST**   | `/student/feedback/` | Submit feedback for a course |
| **PUT**    | `/student/<feedback_id>/` | Update feedback |
| **DELETE** | `/student/<feedback_id>/` | Delete feedback |

#### **c. Course Enrollment**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET**    | `/student/enroll/` | Retrieve all enrolled courses |
| **POST**   | `/student/enroll/` | Enroll in a course |
| **DELETE** | `/student/enroll/<course_id>/` | Unenroll from a course |

---

### **4. Teacher Management**  

#### **a. Course Management**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET**    | `/teacher/course/add_course/` | Retrieve all courses created by the teacher |
| **POST**   | `/teacher/course/add_course/` | Add a new course |
| **PUT**    | `/teacher/course/add_course/<course_id>/` | Update course details |
| **DELETE** | `/teacher/course/add_course/<course_id>/` | Delete a course |

#### **b. Course Materials**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET**    | `/teacher/course/material/` | Retrieve all uploaded course materials |
| **POST**   | `/teacher/course/material/` | Upload new course material |
| **PUT**    | `/teacher/course/material/<course_id>/` | Update course material |
| **DELETE** | `/teacher/course/material/<course_id>/` | Delete course material |

#### **c. Student Management**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET**    | `/teacher/courses/block/` | Retrieve list of blocked students |
| **POST**   | `/teacher/course/block/` | Block a student from a course |
| **PUT**    | `/teacher/course/block/<student_id>/` | Update block status |
| **DELETE** | `/teacher/course/block/<student_id>/` | Unblock a student |

#### **d. Search Functionality**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET**    | `/teacher/search/<name>/` | Search for teachers or students |

#### **e. Remove Student from Course**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **DELETE** | `/teacher/remove/<student_id>/<course_id>/` | Remove a student from a course |

---

## **Deployment & Setup**  

### **1. Local Development Setup**  
```bash
# Clone the repository
git clone https://github.com/46ra20/Pulikids.git
cd pulikids

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # (For Linux/Mac)
venv\Scripts\activate  # (For Windows)

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

---

### **2. Deployment (Production Setup)**  
```bash
# Set up Docker containers
docker-compose up --build -d

# Run migrations
docker exec -it <container_id> python manage.py migrate

# Start the production server
gunicorn --bind 0.0.0.0:8000 Pulikidz.wsgi:application
```

---

## **Security & Best Practices**  
- **Django Token Authentication** for secure login  
- **Role-Based Access Control** to manage user permissions  
- **Rate Limiting** to prevent abuse  
- **Data Encryption** to secure sensitive information  
- **Logging & Monitoring** for API usage tracking  

---

## **Future Enhancements**  
- **Role-based dashboards for teachers and students**  
- **AI-powered course recommendations**  
- **Live video classes integration**  
- **Automated progress tracking for students**  

---

## **Contributors**  
👨‍💻 **Md Rakib Bhuiyan** - Lead Developer  

---

## **License**  
This project is licensed under the **MIT License**.  


🚀 Let me know if you need further refinements! 🎯

# 🏥 Healthcare Backend API

A secure Django + DRF backend system for managing patients, doctors, and doctor-patient mappings with JWT authentication.

---

## ✅ Features

- User Registration & JWT Login
- Patient CRUD (for logged-in users only)
- Doctor CRUD (for all authenticated users)
- Assign/Remove doctors to/from patients
- Token Refresh support via JWT

---

## 🔧 Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (SimpleJWT)
- **Environment Management:** Python Decouple

---

## 🔐 Authentication Flow

1. **Register:**  
   `POST /api/auth/register/`  
   Body:
   ```json
   {
     "username": "testuser",
     "email": "test@example.com",
     "password": "Test@1234"
   }
   
   Note-In header uncheck the  authentication for registeration.
   ```

2. **Login (JWT Token):**  
   `POST /api/auth/login/`  
   Body:
   ```json
   {
     "email": "test@example.com",
     "password": "Test@1234"
   }
   ```
   ✅ Returns:
   ```json
   {
     "refresh": "....",
     "access": "...."
   }
   ```

3. **Use Token in Headers:**  
   ```
   Authorization: Bearer <access-token>
   ```

4. **Token Expired?**  
   Re-login or refresh the token using:  
   `POST /api/auth/refresh/`

---

## 📁 Project Structure

```
healthcare_project/
│
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── healthcare_project/
│   ├── settings.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
```

---

## 📬 API Endpoints

### 🔑 Auth

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/refresh/`

---

### 👤 Patients

- `POST /api/patients/`  
  ```json
  {
    "name": "John Doe",
    "age": 30,
    "gender": "Male"
  }
  ```

- `GET /api/patients/`  
- `GET /api/patients/<id>/`  
- `PUT /api/patients/<id>/`  
  ```json
  {
    "name": "John Smith",
    "age": 31,
    "gender": "Male"
  }
  ```
- `DELETE /api/patients/<id>/`

---

### 🩺 Doctors

- `POST /api/doctors/`  
  ```json
  {
    "name": "Dr. Priya Sharma",
    "specialization": "Cardiologist"
  }
  ```

- `GET /api/doctors/`  
- `GET /api/doctors/<id>/`  
- `PUT /api/doctors/<id>/`  
  ```json
  {
    "name": "Dr. Priya S. Sharma",
    "specialization": "Cardiology Specialist"
  }
  ```
- `DELETE /api/doctors/<id>/`

---

### 🔗 Mapping

- `POST /api/mappings/`  
  ```json
  {
    "patient": 1,
    "doctor": 2
  }
  ```

- `GET /api/mappings/`  
- `GET /api/mappings/?patient=<id>`  
- `DELETE /api/mappings/<id>/`

---

## 🧪 Testing

Use **Postman** to test all API routes. Ensure you add the **JWT access token** in the request header:

```
Authorization: Bearer <access-token>
```

---

## 🚀 Getting Started

1. **Clone the project**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run migrations**
   ```bash
   python manage.py migrate
   ```
4. **Start server**
   ```bash
   python manage.py runserver
   ```

---

## 🔐 Environment Configuration

Create a `.env` file in the root directory with the following:

```dotenv
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

\# Secure Django Web Application



\## Project Description

This project is a secure web application developed using the Django framework.

The objective of this project is to implement secure coding practices based on

OWASP Top 10 and OWASP ASVS requirements.



The application includes authentication, role-based access control (RBAC),

secure session management, input validation, logging and monitoring, and

secure configuration using environment variables.



---



\## Project Objectives

* Develop a secure web application
* \- Apply OWASP Top 10 and OWASP ASVS controls
* \- Prevent SQL Injection and XSS attacks
* \- Implement authentication and access control
* \- Practice secure coding and version control using GitHub



---



\## Features

* \- User login and logout
* \- Role-Based Access Control (Admin \& Normal User)
* \- Secure session handling
* \- Input validation using Django ORM
* \- CSRF protection enabled
* \- Audit logging for admin activities
* \- Secure configuration using `.env`
* \- HTML output escaping to prevent XSS



---



\## Technologies Used

* \- Python 3.11
* \- Django Framework
* \- SQLite Database
* \- python-dotenv
* \- GitHub



---



\## Installation Steps



1\. Clone the repository

git clone <your-github-repository-link>




2\. Create virtual environment

python -m venv venv




3\. Activate virtual environment

venv\\Scripts\\activate



4\. Install dependencies

pip install -r requirements.txt



5\. Create .env file

SECRET\_KEY=your\_secret\_key

DEBUG=True

ALLOWED\_HOSTS=127.0.0.1,localhost



6\. Run database migrations

python manage.py migrate



7\. Create admin user

python manage.py createsuperuser



8\. Run the application

python manage.py runserver

---

Security Features Summary

* Passwords hashed using Django built-in hashing
* SQL Injection prevention using Django ORM
* CSRF protection enabled
* Session-based authentication
* Debug mode disabled in production
* Audit logs for security monitoring
* Access control enforced on protected views

---

How to Use

* Login as admin or normal use
* Admin can view audit logs
* Users can view dashboard and profile
* Unauthorized access is restricted

---

Dependencies

* Django
* python-dotenv

---

Screenshots

* Login Page
* Dashboard
* Profile Page
* Audit Log Page

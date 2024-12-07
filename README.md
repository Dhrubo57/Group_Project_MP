# Movers & Packers Management System  

This is a web-based application designed to streamline the management of moving and packing services. The system includes a customer-facing interface for service requests and queries, as well as an admin panel for managing services, bookings, and customer interactions. Developed as part of a university software development course, this project aims to enhance efficiency in the moving and packing industry.
## Features  

### Home Page  
1. **Services**:  
   - Displays a list of services such as home shifting, car shifting, etc., with a short description.  

2. **About Us**:  
   - Contains a brief overview of the company and its values.  

3. **Request Quote Form**:  
   - Users can fill out their name, email, phone number, pick-up location, destination, shifting date, and item details to request services.  

4. **Contact Us**:  
   - Includes company contact details and a query form for customer inquiries.  

5. **Admin Login**:  
   - Secure login system for admins to access the admin panel.

### Admin Panel  
1. **Dashboard**:  
   - Displays a summary of total services, queries, and bookings.  

2. **Services Management**:  
   - Add and manage services (edit or delete).  

3. **Bookings Management**:  
   - **New Bookings**: View and accept/reject new service requests.  
   - **Old Bookings**: Manage previously accepted bookings.  

4. **Queries Management**:  
   - **Unread Queries**: View new customer questions.  
   - **Read Queries**: Manage previously viewed queries.  

5. **Search Functionality**:  
   - Search bookings by customer name or contact number.  

6. **Reports**:  
   - Generate reports for bookings and queries within specific date ranges.  

7. **Admin Password Change**:  
   - Allows admin to update their password securely.
## Installation and Usage  

### Prerequisites  
- Python 3.9 or higher  
- Django 3.2 or higher  
- SQLite3 (default with Django)

### Installation Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/movers-packers-management.git
   cd movers-packers-management
   pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
## Built With  
- **Front-End**: HTML, CSS, JavaScript  
- **Framework**: Python Django 
- **Database**: SQLite3 (default with Django)  
 

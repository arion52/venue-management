# Automated Venue Booking and Occupancy Monitoring System  

## Overview  
This software is designed to optimize venue management in academic institutions by automating booking processes and monitoring occupancy in real-time. By integrating **infrared sensor technology**, a robust **Django backend**, and a **Flutter mobile app**, the system provides a seamless and transparent user experience while enhancing operational efficiency.  
[Frontend](https://github.com/arion52/venue-management-flutter)
---

## Features  
### Core Functionality  
- **Real-Time Occupancy Monitoring**  
  - Tracks the number of people in a venue using infrared sensors.  
  - Updates venue availability dynamically.  

- **Automated Venue Booking**  
  - Enables users to book venues through a user-friendly mobile app.  
  - Prevents double-booking with real-time updates.  

- **Mobile Notifications**  
  - Provides instant confirmations, cancellations, and updates for bookings.  

### Key Components  
- **Infrared Sensors**  
  - Tracks foot traffic at venue entry/exit points for precise occupancy data.  

- **Django Backend**  
  - Manages booking data and user authentication.  
  - Provides RESTful APIs for real-time communication with the mobile app.  

- **Flutter Mobile App**  
  - Cross-platform app for real-time venue availability and booking.  
  - Intuitive interface with support for notifications.  

- **PostgreSQL Database**  
  - High-performance database for secure storage of user, venue, and booking data.  

---

## Technology Stack  
- **Backend**: Python, Django, Django REST Framework  
- **Frontend**: Flutter (for Android & iOS)  
- **Database**: PostgreSQL  
- **Hardware**: Arduino UNO R3, Infrared Sensors  

---

## System Architecture  

1. **Infrared Sensors**  
   - Sensors installed at entry/exit points collect foot traffic data.  
   - Data is transmitted to the backend via Wi-Fi for processing.  

2. **Backend**  
   - Processes booking requests and synchronizes data between sensors and the mobile app.  
   - Ensures secure authentication and efficient API communication.  

3. **Mobile Application**  
   - Fetches real-time venue availability and booking information via APIs.  
   - Displays user-friendly interfaces for seamless interaction.  

---

## Installation  

### Backend Setup  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/your-username/venue-booking-system.git  
   ```  
2. Navigate to the backend directory:  
   ```bash  
   cd backend  
   ```  
3. Create a virtual environment and activate it:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # For Linux/Mac  
   venv\Scripts\activate     # For Windows  
   ```  
4. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
5. Run migrations and start the server:  
   ```bash  
   python manage.py migrate  
   python manage.py runserver  
   ```  

### Mobile App Setup  
1. Navigate to the mobile app directory:  
   ```bash  
   cd mobile_app  
   ```  
2. Install Flutter dependencies:  
   ```bash  
   flutter pub get  
   ```  
3. Run the app on an emulator or connected device:  
   ```bash  
   flutter run  
   ```  

---

## Usage  
1. **Admins**:  
   - Configure venues and monitor occupancy data through the admin panel.  
   - Receive real-time insights on venue usage.  

2. **Users**:  
   - Book venues using the mobile app.  
   - View live updates on venue availability.  

---

## Future Enhancements  
- **AI Integration**:  
  - Predictive booking and smart suggestions based on usage patterns.  
  - Dynamic pricing models for peak demand management.  

- **IoT Integration**:  
  - Monitoring environmental parameters (e.g., temperature, lighting).  
  - Tracking equipment availability for event readiness.  

- **Advanced Reporting**:  
  - Detailed usage analytics and custom dashboards for administrators.  

---

## Contributing  
We welcome contributions to enhance the system!  
1. Fork the repository.  
2. Create a feature branch.  
3. Commit changes and submit a pull request.  

---

## License  
This project is licensed under the [MIT License](LICENSE).  

---

## Contact  
For queries or support, contact:  
**Bargav Krishna K H, Karthikeyan Arun, Manju Varshikha S, Aarthi G**  
Email: support@venue-booking.com

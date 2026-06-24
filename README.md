# ✈️ Flight Booking System

![Banner](screenshots/banner.png)

## 📖 Overview

The Flight Booking System is a web-based application developed using **Python Flask** and **SQLite**. The system allows users to register, log in, search available flights, book tickets, and generate booking confirmations.

This project demonstrates CRUD operations, database management, user authentication, session handling, and dynamic web page rendering using Flask.

---

## 🚀 Features

### User Module

* User Registration
* User Login
* User Logout
* Session Management

### Flight Module

* Add New Flights
* Store Flight Details in Database
* Search Flights by Source and Destination

### Booking Module

* Book Flight Tickets
* Generate Booking Confirmation
* View Ticket Details

### Database Module

* SQLite Database Integration
* Automatic Table Creation

---

## 🖼️ Screenshots

### Login Page
src="login.png"

### Registration Page

![Registration Page](screenshots/register.png)

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Add Flight Page

![Add Flight](screenshots/add_flight.png)

### Search Flights

![Search Flights](screenshots/search.png)

### Flight Booking

![Flight Booking](screenshots/book.png)

### Ticket Generation

![Ticket](screenshots/ticket.png)

---

## 🛠️ Technologies Used

| Technology | Purpose             |
| ---------- | ------------------- |
| Python     | Backend Development |
| Flask      | Web Framework       |
| SQLite3    | Database            |
| HTML       | Frontend Structure  |
| CSS        | Styling             |
| Jinja2     | Template Engine     |

---

## 📂 Project Structure

```text
FlightBookingSystem/
│
├── app.py
├── database.db
├── README.md
│
├── screenshots/
│   ├── banner.png
│   ├── login.png
│   ├── register.png
│   ├── dashboard.png
│   ├── add_flight.png
│   ├── search.png
│   ├── book.png
│   └── ticket.png
│
└── templates/
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── add_flight.html
    ├── search.html
    ├── book.html
    └── ticket.html
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/flight-booking-system.git
cd flight-booking-system
```

### Install Dependencies

```bash
pip install flask
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 🗄️ Database Schema

### Users Table

| Column   | Type    |
| -------- | ------- |
| id       | INTEGER |
| username | TEXT    |
| password | TEXT    |

### Flights Table

| Column      | Type    |
| ----------- | ------- |
| id          | INTEGER |
| name        | TEXT    |
| source      | TEXT    |
| destination | TEXT    |
| departure   | TEXT    |
| arrival     | TEXT    |
| price       | INTEGER |
| date        | TEXT    |

### Bookings Table

| Column    | Type    |
| --------- | ------- |
| id        | INTEGER |
| passenger | TEXT    |
| flight    | TEXT    |
| route     | TEXT    |
| price     | INTEGER |

---

## 🌐 Application Routes

| Route        | Method    | Description       |
| ------------ | --------- | ----------------- |
| /            | GET, POST | User Login        |
| /register    | GET, POST | User Registration |
| /dashboard   | GET       | Dashboard         |
| /add_flight  | GET, POST | Add Flight        |
| /search      | GET, POST | Search Flights    |
| /book/<id>   | GET, POST | Book Flight       |
| /ticket/<id> | GET       | View Ticket       |
| /logout      | GET       | Logout            |

---

## 🔒 Security Improvements

Current version stores passwords in plain text.

Recommended enhancements:

* Password Hashing (Werkzeug)
* CSRF Protection
* Input Validation
* Admin Authentication
* Role-Based Access Control

---

## 🎯 Future Enhancements

* Admin Panel
* Flight Cancellation
* Seat Selection
* Payment Gateway Integration
* Email Notifications
* PDF Ticket Download
* Responsive UI Design
* Flight Status Tracking
* Multi-user Booking Support

---

## 👨‍💻 Author

**Karan Singh Kushwaha**

B.Tech Information Technology

Arya College of Engineering & IT, Kukas


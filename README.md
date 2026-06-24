# ✈️ Flight Booking System

A simple Flight Booking System built using **Python Flask** and **SQLite**. This web application allows users to register, log in, search flights, book tickets, and view booking details.

## Features

* User Registration
* User Login & Logout
* Add New Flights
* Search Flights by Source and Destination
* Book Flight Tickets
* Generate Booking Tickets
* SQLite Database Integration
* Session Management

## Technologies Used

* Python 3
* Flask
* SQLite3
* HTML
* CSS
* Jinja2 Templates

## Project Structure

```
FlightBookingSystem/
│
├── app.py
├── database.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_flight.html
│   ├── search.html
│   ├── book.html
│   └── ticket.html
│
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone 
```

### 2. Install Required Packages

```bash
pip install flask
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open Browser

Visit:

```
http://127.0.0.1:5000
```

## Database Tables

### Users

| Column   | Type    |
| -------- | ------- |
| id       | INTEGER |
| username | TEXT    |
| password | TEXT    |

### Flights

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

### Bookings

| Column    | Type    |
| --------- | ------- |
| id        | INTEGER |
| passenger | TEXT    |
| flight    | TEXT    |
| route     | TEXT    |
| price     | INTEGER |

## Application Routes

| Route        | Description    |
| ------------ | -------------- |
| /            | Login Page     |
| /register    | Register User  |
| /dashboard   | Dashboard      |
| /add_flight  | Add Flight     |
| /search      | Search Flights |
| /book/<id>   | Book Flight    |
| /ticket/<id> | View Ticket    |
| /logout      | Logout User    |

## Security Notice

This project stores passwords in plain text for educational purposes only.

For production applications:

* Use password hashing (Werkzeug/Bcrypt)
* Enable CSRF protection
* Add input validation
* Use environment variables for secret keys

## Future Improvements

* Admin Panel
* Flight Cancellation
* Seat Selection
* Payment Gateway Integration
* Email Ticket Generation
* PDF Ticket Download
* Responsive UI Design

## Author

Karan Singh Kushwaha

Arya College of Engineering & IT, Kukas


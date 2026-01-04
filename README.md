This repository contains a PARTIAL VERSION of a Parking Management Application
developed using Python, Kivy, and SQLite.

The purpose of this repository is to demonstrate system design, user
authentication, database integration, and GUI development skills.
This is NOT the complete or final version of the project.


--------------------
PROJECT DESCRIPTION
--------------------

The Parking Management Application is a multi-screen desktop application that
allows users to register, log in, and interact with a visual parking system.
The application focuses on clean architecture, modular design, and secure
handling of user data.

The project was developed as a learning and engineering exercise and reflects
practical experience with software architecture, state management, and
database-backed applications.


--------------------
FEATURES INCLUDED IN THIS REPOSITORY
--------------------

USER AUTHENTICATION
- User registration with email and password
- Secure password storage using SHA-256 hashing
- Login verification using a local SQLite database
- Prevention of duplicate user accounts
- Login-protected access to certain application pages

DATABASE INTEGRATION
- Automatic creation of an SQLite database on first run
- Persistent storage of registered users
- Separate utility script for viewing database contents

GRAPHICAL USER INTERFACE (GUI)
- Built using the Kivy framework
- Multiple screens managed via ScreenManager
- Smooth screen transitions (FadeTransition)
- Modular separation between UI (.kv) and logic (.py)

PARKING SYSTEM (VISUAL)
- Custom ParkingSpot component implemented as a Kivy Button
- Color-based state indication:
  - Green: Available parking spot
  - Red: Occupied parking spot
- Multiple parking detail pages
- Interactive parking spot toggling

NAVIGATION & STATE MANAGEMENT
- Centralized application control using Kivy App class
- Login state tracking within the application
- Conditional access to parking features based on login status


--------------------
FILES INCLUDED IN THIS REPOSITORY
--------------------

- main.py
  Contains the core application logic, screen management,
  database handling, and authentication system.

- parkingapp.kv
  Defines the graphical layout of all screens and UI components.

- view_users.py
  Utility script for debugging and viewing registered users
  stored in the SQLite database.

- users.db
  SQLite database file (automatically generated on first run).

- README.md
  General project documentation for GitHub.


--------------------
LIMITATIONS OF THIS VERSION
--------------------

This repository represents only a PART of the full project.

The following features are NOT included or are incomplete:
- Persistent storage of parking spot occupancy
- Parking reservation system
- Logout functionality
- Admin or management dashboard
- Real-world parking location data
- Mobile deployment
- Advanced security features

These limitations are intentional, as this repository is intended to
showcase core concepts rather than a finished commercial product.


--------------------
FUTURE IMPROVEMENTS
--------------------

Planned or possible future extensions include:
- Database persistence for parking spot states
- User-specific parking reservations
- Time-based parking tracking
- Admin control panel
- Enhanced UI/UX
- Mobile platform support
- Integration with real-time or sensor-based data


--------------------
PURPOSE OF THIS REPOSITORY
--------------------

This repository is intended for:
- Educational use
- Demonstration of programming and system design skills
- Portfolio or academic application support
- Code review and learning reference

It should not be considered a production-ready system.


# Event Registration System

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This is a simple event registration system built with Django. Users can create events, register for events, and manage their registrations. The system also provides API endpoints for listing events, retrieving event details, user registration for events, and fetching user's registered events.

## Features

- Event creation with title, description, date, time, and location.
- User registration and authentication.
- Event registration with a limit on available slots.
- User dashboard to manage event registrations.
- Admin panel for managing events and user registrations.
- Basic search functionality for events.
- API endpoints for event-related operations.

## Requirements

- Python (3.6 and above)
- Django
- Django REST Framework

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/event-registration-system.git
   cd event-registration-system
   
 ##  
python -m venv env

On Windows:
.\venv\Scripts\activate
On macOS and Linux:
source venv/bin/activate

## Install dependencies:
pip install -r requirements.txt

## Configuration
cp .env.example .env

## Running the Application
python manage.py migrate
python manage.py runserver

## Usage 
Create events using the "Create Event" link.
Register for events using the "Register Event" link.
Search for events using the search bar.
View and manage your registrations on the dashboard.

## API Endpoints
List of all events: /api/events/
Details of a specific event: /api/events/<event_id>/
User registration for an event: /api/register/
User's registered events: /api/user_registrations/

## Documentation
Swagger UI: /swagger/
ReDoc: /redoc/
DRF Docs: /api/docs/

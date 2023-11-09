# Employee_Records

### This is a django application that manages employee records by allowing the user to Add new employees, update employee information, view and delete employees.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create and Activate a Virtual Environment](#2-create-and-activate-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Configure the Database](#4-configure-the-database)
  - [5. Apply Migrations](#5-Run-Tests)
  - [6. Run Tests](#5-apply-migrations)
- [Run the Project](#run-the-project)

## Requirements

- Python (latest version)
- Django (latest version)
- MySQL Server 

## Setup

### 1. Clone the Repository
    git clone git@github.com:snelisile-m/Employee_Records.git
    cd Employee_Records

### 2. Create and Activate a Virtual Environment(on linux)
    source venv/bin/activate

### 3. Install Dependencies
    pip install -r requirements.txt


### 4. Configure the Database
- Open your_project/settings.py.
- Locate the DATABASES setting.
- Update the configuration based on your database.

### 5. Apply Migrations
    python3 manage.py makemigrations
    python3 manage.py migrate

### 6. Run Tests
    python3 manage.py test employee_register

## Run the Project
    python manage.py runserver
    http://127.0.0.1:8000/show
Description

This project implements a user data management system using Python and Flask. Users can be viewed, added, updated, or deleted through a simple terminal menu. The Flask server runs in the background for optional API access, enabling easy CRUD operations without opening a browser or Postman.

Features

View all users

View a single user by ID

Add a new user

Update an existing user

Delete a user

Simple terminal-based menu interface

Flask server running in the background for optional API access

Tools Used

Python

Flask

Command-line interface

How to Run

Save the Python code as flask_app.py.

Open a terminal and navigate to the folder containing the file.

Run the Flask server and menu system:

python flask_app.py


Follow the menu options in the terminal to manage users.

Sample Menu
==== User Management Menu ====
1. View all users
2. View a user
3. Add a new user
4. Update a user
5. Delete a user
6. Exit

Usage

Enter the number corresponding to the action you want to perform.

For adding or updating a user, follow the prompts to input name and age.

Users are stored in memory, so data will reset when the program stops.

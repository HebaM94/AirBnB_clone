<h1 align="center"> Project: AirBnB clone - The console </h1>

## Project Description:
This Project is a copy of the AirBnB Web Application.

## Command Interpreter Description:
The Command Interpreter serves as the primary interface for interacting with the Airbnb Clone application.

### How to start it:
- Clone the repository to your local machine.
- Navigate to the project directory.
- Run the command ./console.py to start the Command Interpreter.

### How to use it:
- Using commands to interact with the application:
- create: Creates a new instance of a specified class and saves it to the JSON file.
- show: Displays the details of a specific instance based on its class name and ID.
- destroy: Deletes a specified instance from the JSON file.
- all: Displays a list of all instances or all instances of a specified class.
- update: Updates the attributes of a specified instance.

### Examples:
- To create a new user: create User
- To display details of a user with ID 246: show User 246
- To delete a user with ID 246: destroy User 246
- To display all instances of the User class: all User
- To update the email attribute of a user with ID 246: update User 246 email "new_email@example.com"
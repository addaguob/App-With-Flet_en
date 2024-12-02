# App-With-Flet

## Description

The project was developed to study and practice programming in Python, MySQL database manipulation and Flet for creating graphical interfaces. The idea was to create an application that would allow managing user registration, customers, products, sales and controlling the stock in a simple and efficient way.

## Features

- User Authentication: The system has a login screen for administrator user authentication.
- User Registration: Allows creating users.
- Customer Control: Allows registering and editing customer information.
- Product Management: Allows registering, editing and excluding products from the stock.
- Sales Registration: Allows registering sales, associating the customers and products involved.
- Stock Control: Keeps the product stock updated based on the sales made.

## Technologies Used

- Python
- MySQL
- Flet (graphical interface)

## Screens:

Login:

![Login](Screens/Login.PNG)

Home Screen:

![Home Screen](Screens/Home.PNG)

Sales:

![Sales](Screens/Sales.PNG)

Products:

![Products](Screens/Products.PNG)

Clients:

![Clients](Screens/Customers.PNG)

User Registration:

![User Registration](Screens/Users.PNG)

## To test:

To run the application, make sure you have Python and MySQL installed on your system. In addition, it is recommended to create a virtual environment to isolate the project's dependencies.

1. Clone the repository to your local machine:

   - git clone https://github.com/HelioCard/App-With-Flet.git
   - cd App-With-Flet

2. Install the project dependencies:

   - pip install -r requirements.txt

3. Access the MySQL. Create your database (schema) and execute the script from the "database_scripts" folder to create the tables. There are two options:

   - create_tables - structure_only.sql (only table creation);
   - create_tables - structure_and_some_data.sql (table creation and insertion of some test data)

4. Run the main.py file. Enter any text in the "User" and "Password" fields and click "Login" to open the initial database configuration screen. Enter your connection details and click "Save". The following screens only open on the first run, when there has been no configuration yet:

![Database Configuration](Screens/Config_DB.PNG)

5. Once again, enter any text in the "User" and "Password" fields and click "Login" to open the administrator registration screen. Fill in and click "Register":

![First Administrator Creation](Screens/Config_Admin.PNG)

6. Log in.

The project was developed for educational purposes and to develop skills in Python, MySQL, and Flet. Feel free to explore the code and adapt it to your needs. If you have any questions or suggestions, please contact me: helio.card@yahoo.com.br

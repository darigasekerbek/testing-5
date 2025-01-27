# testing-5

Flight Booking Automation with Page Object Model (POM)
Overview
This project demonstrates how to automate a flight booking process using the Page Object Model (POM) design pattern in Selenium. The goal is to structure the automation code in a way that separates page-specific interactions from the test logic, making it easier to maintain and extend.

Project Structure
The project is organized as follows:

Page Classes: Each page of the web application (e.g., HomePage, FlightSelectionPage, BookingPage, ConfirmationPage) has its own class. These classes contain:

Locators for the elements on the page.
Methods to interact with the elements, such as clicking buttons, filling out forms, and retrieving information.
Test Class: This contains the actual test logic, which interacts with the page classes to simulate the user journey (e.g., selecting a flight, entering booking details, and confirming the booking).

Driver Management: A separate class manages the WebDriver instance, ensuring the browser is correctly initialized and closed for each test run.

Features
Page Object Model (POM) design pattern for better organization and reusability.
Automated testing for booking a flight using a demo application.
Modular and maintainable code structure.
Technologies Used
Selenium WebDriver: For browser automation.
Python: Programming language.
pytest: Testing framework.
Prerequisites
To run this project, you will need the following:

Python installed on your system.

Selenium WebDriver for Python:

You can install it via pip:
Копировать
Редактировать
pip install selenium
pytest installed for running the tests:

Копировать
Редактировать
pip install pytest
A compatible browser (e.g., Chrome or Firefox) and the corresponding WebDriver (e.g., ChromeDriver or GeckoDriver).

How to Run
Clone or download the project files.

Install the required dependencies:

Копировать
Редактировать
pip install -r requirements.txt
Run the tests using pytest:

Копировать
Редактировать
pytest
The test will launch a browser window, simulate a flight booking process, and then close the browser after the test is complete.

Example Workflow
The automation test follows these steps:

Navigate to the flight booking website.
Select the departure and destination cities.
Search for flights and select one.
Fill out the booking details (name, address, credit card, etc.).
Confirm the booking and print the confirmation message.
Video Explanation
To understand how the project works and how the Page Object Model is implemented, check out this video:

Video: How Page Object Model works in Flight Booking Automation

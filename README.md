# Task 1: Selenium Automation - Login Test

## Project Overview

This project demonstrates an automated login test using **Selenium WebDriver**, with **pytest** for test execution and **openpyxl** for reading test data from an Excel file. The script is designed to test the login functionality of a website using multiple sets of credentials stored in an Excel sheet.

The **Page Object Model (POM)** is not implemented here, as the focus is on login functionality and handling dynamic elements using Selenium and pytest.

## Key Features

- **Automated Login Test**: The script performs automated login on a website (https://jut.su) using user credentials.
- **Data-Driven Testing**: Test data (usernames and passwords) are stored in an Excel file (`testdata.xlsx`) and used for parameterized testing via **pytest**.
- **WebDriver Setup**: Automatically installs and manages ChromeDriver using **webdriver_manager**.
- **Headless Browser**: The test runs in headless mode, meaning no browser window is opened during test execution.

## Technologies & Tools

- **Selenium WebDriver**: For web automation.
- **Python**: Programming language used for the script.
- **pytest**: Testing framework to run the test cases.
- **openpyxl**: For reading data from Excel files.
- **webdriver_manager**: For automatic installation of the ChromeDriver.

Conclusion
This automation script tests the login functionality of the website by using multiple sets of credentials from an Excel file. The use of pytest for parameterized testing makes it easy to scale the tests with additional data. The script is designed to run in headless mode, so it doesn't require a visible browser window during execution.


# Task-2. Flight Booking Automation: Page Object Model (POM) Implementation

## Project Overview

This repository demonstrates an automated solution for booking flights using **Selenium WebDriver** and the **Page Object Model (POM)** design pattern. The goal is to improve the readability, maintainability, and scalability of automated tests by separating page interactions and test logic.

## Key Features

- **Page Object Model (POM)**: Implements the design pattern that organizes web page classes to abstract web element interactions.
- **Modular Test Structure**: Page classes handle web elements and interactions, making the test cases concise and reusable.
- **Automated Flight Booking**: Includes the process of selecting flights, booking, and confirming reservations.
- **Driver Management**: A dedicated manager handles WebDriver initialization and termination for each test.

## Technologies & Tools

- **Selenium WebDriver**: A tool to automate web browser interactions.
- **Python**: The programming language used for test script development.
- **pytest**: A testing framework to run the test cases and generate reports.
- **WebDriver (ChromeDriver/GeckoDriver)**: WebDriver executables for browser automation.

Conclusion
The Page Object Model (POM) design pattern is used to separate page-specific interactions from the test logic, improving test readability and maintainability. This structure makes it easy to scale the test suite by adding new tests and pages.


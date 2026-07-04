# Selenium Test Automation Portfolio

This project is a Python-based Selenium test automation framework for testing the SauceDemo web application.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- pytest-html
- Chrome WebDriver

## Features

- Automated login tests
- Inventory page tests
- Cart tests
- End-to-end checkout test
- Page Object Model structure
- Reusable Pytest fixture
- Centralized test data in config file
- HTML test report
- Screenshots on test failure

## Project Structure

```text
test-automation-portfolio/
├── config/
│   └── settings.py
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── overview_page.py
│   └── complete_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── reports/
├── screenshots/
├── utils/
│   └── logger.py
├── pytest.ini
└── requirements.txt

## How to Install

```text
python -m venv venv

## Windows PowerShell

```text
.\venv\Scripts\Activate.ps1

## Install dependencies

```text
pip install -r requirements.txt

## How to Run Tests

```text
pytest

## Generate HTML Report

The framework automatically generates an HTML report:

reports/report.html
Test Scenarios Covered
Valid login
Invalid login
Add product to cart
Remove product from cart
Verify product in cart
Complete checkout flow
Future Improvements
Add Playwright version of the framework
Add GitHub Actions CI/CD
Add cross-browser execution
Add more negative checkout tests
Add API testing examples
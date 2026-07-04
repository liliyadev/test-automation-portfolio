# 🚀 Selenium Test Automation Portfolio

A Python-based Selenium Test Automation Framework built using **Pytest** and the **Page Object Model (POM)** to automate end-to-end testing of the SauceDemo web application.

This project demonstrates industry best practices for building a scalable, maintainable, and reusable UI automation framework.

---

## 📌 Technologies Used

- Python 3.11
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- pytest-html
- Chrome WebDriver
- Git & GitHub

---

## ✨ Framework Features

- ✅ Automated Login Tests
- ✅ Inventory Page Tests
- ✅ Shopping Cart Tests
- ✅ End-to-End Checkout Flow
- ✅ Page Object Model Design Pattern
- ✅ Reusable Pytest Fixtures
- ✅ Centralized Configuration (`settings.py`)
- ✅ HTML Test Reports
- ✅ Automatic Screenshots on Test Failure
- ✅ Organized Project Structure

---

# 📁 Project Structure

```text
test-automation-portfolio/
│
├── config/
│   └── settings.py
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── overview_page.py
│   └── complete_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/
│   └── logger.py
│
├── config/
│   └── settings.py
│
├── reports/
├── screenshots/
│
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/liliyadev/test-automation-portfolio.git
cd test-automation-portfolio
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

## 3. Activate the virtual environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Git Bash

```bash
source venv/Scripts/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Tests

Run the complete test suite:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

Run tests with verbose output:

```bash
pytest -v
```

---

# 📊 HTML Test Report

The framework automatically generates an HTML report after every test execution.

Location:

```text
reports/report.html
```

Open the report in your browser to view:

- Test Results
- Execution Time
- Environment Information
- Failure Details
- Stack Traces

---

# 📸 Screenshots on Failure

If a test fails, a screenshot is automatically captured and saved to:

```text
screenshots/
```

This helps identify the application state at the moment of failure and simplifies debugging.

---

# ✅ Test Scenarios Covered

### Login

- Valid Login
- Invalid Login

### Inventory

- Add Backpack to Cart
- Remove Backpack from Cart

### Cart

- Verify Product in Cart

### Checkout

- Complete End-to-End Checkout

---

# 💡 Design Principles

This framework follows several automation best practices:

- Page Object Model (POM)
- Separation of Test Logic and UI Locators
- Reusable Fixtures
- Centralized Configuration
- Modular Framework Design
- Easy Maintenance and Scalability

---

# 🚀 Future Improvements

Planned enhancements include:

- Playwright automation framework
- GitHub Actions (CI/CD)
- Cross-browser execution
- Explicit waits using WebDriverWait
- BasePage implementation
- API testing examples
- Parallel test execution with Pytest-xdist
- Docker support

---

# 👩‍💻 Author

**Liliya Vildanova**

Junior Test Automation Engineer

GitHub:
https://github.com/liliyadev

LinkedIn:
https://www.linkedin.com/in/liliya-vildanovadev/

---

## ⭐ Project Goals

This project was created to strengthen my automation engineering skills and demonstrate knowledge of:

- Selenium WebDriver
- Python
- Pytest
- Test Framework Design
- UI Test Automation
- Software Testing Best Practices

As the project evolves, additional automation frameworks and CI/CD capabilities will be added to expand its functionality.
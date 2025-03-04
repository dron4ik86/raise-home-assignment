# Fake Store API Automation Framework

A Python-based API testing framework for testing the [FakeStoreAPI](https://fakestoreapi.com/). 
This framework uses [Behave BDD](https://github.com/behave/behave?tab=readme-ov-file#behave), [requests](https://requests.readthedocs.io/en/latest/), 
and [JSON Schema validation](https://python-jsonschema.readthedocs.io/en/latest/validate/).

## Documentation

- [QA Automation Strategy](https://github.com/dron4ik86/raise-home-assignment/blob/main/docs/AutomationStrategy.md) - Our approach to test automation
- [Team Management Plan](https://github.com/dron4ik86/raise-home-assignment/blob/main/docs/TeamManagementPlan.md) - How to build and manage a QA team

## Overview

This framework helps test REST API endpoints of the FakeStore API. It uses BDD (Behavior-Driven Development) with Behave, 
which allows for easily readable test scenarios.

Key features:
- BDD test scenarios written with [Gherkin](https://cucumber.io/) syntax
- JSON Schema validation for API responses
- [Docker](https://www.docker.com/) containers for consistent testing
- [GitHub Actions](https://github.com/features/actions) for continuous integration
- Dynamic test data creation using [Faker](https://github.com/joke2k/faker)
- Flexible test runs with tagging


## Project Structure

```
raise-home-assignment/                  # Root repository folder
├── .github/                            # GitHub configuration directory
│   └── workflows/                      # GitHub Actions workflows
│       └── api-automation.yml          # CI/CD workflow for API automation
├── .venv/                              # Virtual environment (not committed)
├── api/                                # API interaction layer
│   └── products/                       # Products API module
│       ├── schemas/                    # JSON schema validation files
│       │   ├── create_product_schema.py # Schema for product creation validation
│       │   └── product_schema.py       # Schema for product response validation
│       └── products.py                 # Products API client implementation
├── docs/                               # Documentation directory
│   ├── automation_strategy.md          # QA automation approach and strategy
│   └── team_management_plan.md         # QA team structure and management
├── features/                           # Behave BDD features
│   ├── steps/                          # Step definitions
│   │   └── products/                   # Products feature steps
│   │       └── products_steps.py       # Step implementations for product testing
│   └── tests/                          # Test feature files
│       └── products_tests.feature      # Product API test scenarios in Gherkin
├── .env                                # Environment variables
├── .env.template                       # Template for environment variables
├── .gitignore                          # Git ignore configuration
├── Dockerfile                          # Docker image configuration
├── environment.py                      # Behave environment setup/teardown hooks
├── execute.py                          # Test execution helper script
├── README.md                           # Project documentation
└── requirements.txt                    # Python dependencies
```

## Environment Configuration (.env file)

The `.env` file contains environment-specific configuration such as API base URLs and authentication credentials. 
For security reasons, this file should not be committed to version control.

**Note:** While in production environments, secrets should be managed by secure services like [HashiCorp Vault](https://www.vaultproject.io/), 
[Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault), or [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), 
we're using a local `.env` file in this test project for simplicity and 
to ensure you can run the tests immediately without additional setup. 
However, for GitHub Actions CI/CD pipelines, we do follow security best practices by using GitHub Secrets. 
In the workflow file, we access these secrets securely and create the .env file dynamically

Example `.env` file structure (create based on `.env.template`):
```
BASE_URL=https://fakestoreapi.com
# Add other environment variables as needed
```

Since this is a demo project with no actual sensitive credentials, we've prioritized making it easy to set up and run. 
In a real production environment, you would integrate with your organization's secret management solution instead of using local environment files.

## Getting Started

### Prerequisites

- Python 3.9+
- Docker
- Git

## Installation (Local running)

### On macOS

1. **Requirements**:

   - Download [Python 3.x](https://www.python.org/downloads/)
   - Download [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Open Terminal.
3. Navigate to the repository where you want to save the project.
   ```
   cd <folder name>
   ```
   
4. Clone the repository:
   ```
   git clone <repository-url>
   cd raise-home-assignment
   ```

5. Install the virtual environment.
   ```
   pip install virtualenv
   ```
6. Create a virtual environment in the project directory.
   ```
   cd <path to project folder>
   virtualenv venv
   ```
7. Activate the virtual environment.
   ```
   source venv/bin/activate
   ```
8. Install project dependencies.
   ```
   pip install -r requirements.txt
   ```

### Windows 11

1. **Requirements**:

   - Download [Python 3.x](https://www.python.org/downloads/)
   - Download [Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - Download and install [git](https://git-scm.com/downloads)
2. Open terminal as admin.
3. Navigate to the repository where you want to save the project.
   ```
   cd path\to\your\folder
   ```
4. Clone the repository:
   ```
   git clone <repository-url>
   cd raise-home-assignment
   ```
5. Install the virtual environment.
   ```
   pip install virtualenv
   ```
6. Create a virtual environment in the project directory.
   ```
   cd .\<path to project folder>\
   python -m venv venv
   ```
7. Activate the virtual environment.
   ```
   .\venv\Scripts\activate
   ```
8. Install project dependencies.
   ```
   pip install -r .\requirements.txt
   ```

## Running Tests

### Using Behave Framework

Run all tests:
```
behave
```

Run specific tests by tag:
```
behave -t @get_products
```

Run specific tests by tags:
```
behave -t @get_products,@create_product
```

### Using Docker
The `execute.py` script makes it easy to run tests with Docker. This helps everyone run tests in the same environment, 
solving the common "it works on my computer" problem.

Main benefits:
- Builds Docker images automatically
- Handles container setup and cleanup
- Ensures everyone runs tests in exactly the same way
- Easy to use with simple commands

Run all tests:
```
python execute.py run_tests
```

Run specific tests by tag:
```
python execute.py run_tests --tag_name get_products
```
Run specific tests by tags:
```
python execute.py run_tests --tag_name get_products,create_product 
```

### Development Mode

Enter development mode (opens a shell in the Docker container):
```
python execute.py dev
```

### Using GitHub Actions

Tests run automatically:
- When you push to the main branch
- On pull requests to these branches
- Manually through [GitHub Actions](https://github.com/dron4ik86/raise-home-assignment/actions/workflows/api-automation.yml) 
interface with optional tag parameters.

The workflow configuration is defined in `.github/workflows/api-automation.yml`.


## Troubleshooting

### **Problem 1**:

If you encounter issues activating the virtual environment on Windows 11, you might need to set the execution policy. 
Run the following command in PowerShell:
```
Set-ExecutionPolicy RemoteSigned
```

### **Problem 2**:

If Docker container fails to start, check that Docker Desktop is running and try restarting it.

## Contact

If you have any problem with the framework, please contact me.

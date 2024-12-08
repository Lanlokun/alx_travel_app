# ALX Travel App

The `alxtravelapp` project is a real-world Django application that serves as the foundation for a travel listing platform. This milestone focuses on setting up the initial project structure, configuring a robust database, and integrating tools to ensure API documentation and maintainable configurations. The aim is to equip learners with industry-standard best practices for starting and managing Django-based projects efficiently.

## Objectives

- Set up a scalable backend
- Integrate MySQL for database management
- Use Swagger for automated API documentation

These foundational steps are critical in preparing the application for future features and seamless team collaboration.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- MySQL
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/alxtravelapp.git
    cd alxtravelapp
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure the database settings in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. Run the initial migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

### API Documentation

Swagger is used for automated API documentation. To access the API documentation, navigate to `http://localhost:8000/swagger/` after starting the development server.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
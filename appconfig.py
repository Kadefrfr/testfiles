# config.py

class AppConfig:
    """
    Application configuration settings.
    """

    # Database configuration
    DATABASE_URL = "mysql://username:password@localhost:3306/mydatabase"

    # API keys
    API_KEY = "your_api_key_here"
    SECRET_KEY = "your_secret_key_here"

    # Application settings
    DEBUG_MODE = True
    LOG_FILE_PATH = "/path/to/log/file.log"

    # Email configuration
    EMAIL_HOST = "smtp.example.com"
    EMAIL_PORT = 587
    EMAIL_USERNAME = "your_email@example.com"
    EMAIL_PASSWORD = "your_email_password"
    EMAIL_DEFAULT_SENDER = "your_email@example.com"

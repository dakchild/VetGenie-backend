# VetGenie Backend

## Overview
VetGenie is a backend application designed to support the VetGenie mobile app. It provides RESTful APIs for managing veterinarians, appointments, and user authentication.

## Technologies Used
- Python
- FastAPI
- SQLAlchemy (for database interactions)
- Pydantic (for data validation)
- pytest (for testing)

## Project Structure
```
VetGenie-backend
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   └── __init__.py
│   ├── routes
│   │   └── __init__.py
│   ├── schemas
│   │   └── __init__.py
│   └── services
│       └── __init__.py
├── tests
│   ├── __init__.py
│   └── test_main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd VetGenie-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory and add your environment variables (e.g., database URL, secret keys).

## Running the Application
To start the application, run:
```
uvicorn app.main:app --reload
```

## Running Tests
To run the tests, use:
```
pytest
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
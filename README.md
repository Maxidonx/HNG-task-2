# Django Project API 

Welcome to the Django Project API! This API provides CRUD (Create, Read, Update, Delete) operations for managing "Person" resources.

## API Endpoints

### Create a Resource

- **Endpoint**: `/api/`
- **HTTP Method**: POST
- **Request Format**:
  - Content-Type: application/json
  - Body:
    ```json
    {
        "fullname": "value1",
        "track": "value2"
    }
    ```
- **Response Format**:
  - Status Code: 201 Created
  - Content-Type: application/json
  - Body:
    ```json
    {
        "id": 1,
        "fullname": "value1",
        "track": "value2",
    }
    ```

### Read a Resource

- **Endpoint**: `/api/<str:pk>/'
- **HTTP Method**: GET
- **Response Format**:
  - Status Code: 200 OK
  - Content-Type: application/json
  - Body:
    ```json
    {
        "id": 1,
        "fullname": "value1",
        "track": "value2",
        
    }
    ```

### Update a Resource

- **Endpoint**: `/api/<str:pk>/'`
- **HTTP Method**: PUT
- **Request Format**:
  - Content-Type: application/json
  - Body:
    ```json
    {
        "fullname": "updated_value1"
    }
    ```
- **Response Format**:
  - Status Code: 200 OK
  - Content-Type: application/json
  - Body:
    ```json
    {
        "id": 1,
        "fullname": "updated_value1",
        "track": "value2",
       
    }
    ```

### Delete a Resource

- **Endpoint**: `/api/<str:pk>/'
- **HTTP Method**: DELETE
- **Response Format**:
  - Status Code: 204 No Content

## Sample API Usage

### Creating a Resource
# API Endpoints
```bash

here describes the API endpoints of my projects. Include the endpoint URLs, HTTP methods, and a brief explanation of what each endpoint does.

Create Person: POST "/api/"

Create a new person with the provided data.
Read Person: GET "/api/{person id OR name}"

Retrieve details of a specific person by ID.
Update Person: PUT "/api/{person id or name}"

Update the details of an existing person by ID.
Delete Person: DELETE "/api/{person id or name}"

Delete a person by id or name.
```
# DATABASE
In this it is god to point out that PostreSQL was used as the database management system for this porject.

# Known Limitations
The API supports only JSON data format.
Error handling for invalid requests is not comprehensive in this version.

## Setting Up and Deploying Locally
## Prerequisites
- Python 3.7+
- Django 3.x
- Virtual Environment (recommended)
- Batabase

1. **Clone this repository to your local machine:**

   ```bash
   git clone https://github.com/Maxidon/HNG-2.git
    ```
2. ### Navigate to the project directory:
```bash
cd HNG-2/
```
3. ### Create and activate a virtual environment (recommended):
```bash
pip install pipenv
pipenv install Django
pipenv shell
```
4. ### Starting Django:
```bash
django-admin startproject HNG .
python manage.py startapp peopleAPI
```
5. ### Install project dependencies:
```bash
pipenv install 
```
6. ### Make migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
7. ### Run the development server:
```bash
python manage.py runserver
```

Now, your Django Project API is up and running locally at http://localhost:8000/.

# Testing
- Localhost:8000/api/
- Server_url https://hng-task-2-wqfj.onrender.com/api/
- * ENSURE YOU TEST EACH ENDPOINTS WITH POSTMAN 

# A UML Diagram is attached to this project to further discribe this project.






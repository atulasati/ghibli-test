# Ghibli Project
ghibli_project
Images Attached with this code

## Prerequisites

- Python 3.9
- Docker

## A) Running the Application on Docker

Ensure that Python and Docker are installed on your system. After that, navigate to the '/' directory and execute the following command:

- sudo docker-compose up
  
### Access the Application

You can access the application by visiting the following link in your web browser:


[http://localhost:8000/movies?ghiblikey=ghiblivalue](http://localhost:8000/movies)

Make sure the application is running before accessing the link.

The application will run on port 8000, and the endpoint is '/myapp'. Access the index page to interact with the application.

### For Swagger 
 Use this key value for access (ghiblikey=ghiblivalue)
 [http://localhost:8000/docs](http://localhost:8000/docs)

## B) Running Test Cases

To execute the test cases, use the following commands in the terminal:

* To install the dependencies pip install -r requirements.txt
* To run the tests: `python3 manage.py test`
* Test Case Coverage  `coverage run manage.py test`
* Coverage Report `coverage report`

The test results will be displayed, including the coverage report.

# Without Docker
The Movie List Project is a Python application to consume Ghibli APIs and display a list movies, with their related actors, in the movies page `/movies/`.
 
The data displayed is cached using memcached, and the cache expires every 60 seconds.

The project is built using **Python 3.x** and **Django 3.x**

##Installation

* To **install the project's requirements** run: `pip3 install -r requirements.txt` 


* To **start the web server** run: `python3 manage.py runserver` and access `http://127.0.0.1:8000/movies?ghiblikey=ghiblivalue`
* Swagger Url `http://127.0.0.1:8000/docs/`

* To run the tests: `python3 manage.py test`
* Test Case Coverage  `coverage run manage.py test`
* Coverage Report `coverage report`
  

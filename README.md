# Women's Period Cycle (WPC) API

A REST API that helps estimate a woman’s period cycles within a specific timeframe and also determine what period of her monthly cycle a lady is currently in.

## Requirements (Prerequisites)
* Python >= 3.8
* Pip

Dependencies (will be installed on step 6 in next section):
* Django~=3.2.8
* djangorestframework==3.12.4
* django-environ==0.7.0

## Installation & Setup
### Windows
1. Open a terminal and `cd` into the directory you want to clone this repository.
2. Run `git clone https://github.com/ifeekz/wpc_api.git` to clone this project.
3. Run `cd wpc_api` to get into the project directory.
4. Run `python -m venv wpc_venv` to create a virtal environment
5. Run `wpc_venv\Scripts\activate` to activate the virtal environment
6. Run `python -m pip install --upgrade pip` to install or upgrade pip
7. Run `pip install -r requirements.txt` to install dependencies
8. Run `copy .env.example .env` to copy the environment wariables
9. Run `python manage.py migrate` to setup DB migrations

### Linux and OS X
1. Open a terminal and `cd` into the directory you want to clone this repository.
2. Run `git clone https://github.com/ifeekz/wpc_api.git` to clone this project.
3. Run `cd wpc_api` to get into the project directory.
4. Run `python3 -m venv wpc_venv` to create a virtal environment
5. Run `source wpc_venv\Scripts\activate` or `. wpc_venv\Scripts\activate` to activate the virtual environment
6. Run `python -m pip install --upgrade pip` or `python -m pip install -U --force-reinstall pip` to install or upgrade pip
7. Run `pip install -r requirements.txt` to install dependencies
8. Run `copy .env.example .env` to copy the environment wariables
9. Run `python manage.py migrate` to setup DB migrations

## Usage
To use the application follow these instructions:

- Run `python manage.py runserver` to start the server
- To create cycles, use this endpoint using tool like postman:

    POST: `http://localhost:8000/womens-health/api/create-cycles`

    Header: `Accept: application/json`

    Body (sample): 

        {
            "last_period_date": "2020-06-20",
            "cycle_average": 25,
            "period_average": 5,
            "start_date": "2020-07-25",
            "end_date": "2021-07-25"
        }

- To get cycle event for a date use

    GET: `http://localhost:8000/womens-health/api/cycle-event`

    Header: `Accept: application/json`

    Query Parameters (sample):

      {date: '2021-01-19'}

## Running the tests
Run `python manage.py test` to run the tests
# python-django

## Install virtualEnv

`sudo pip3 install virtualenv`

## Go Into Project folder

`cd PYTHON-DJANGO`

## run The following Command

`virtualenv venv -p python3`

## If You don't Have a DB then run the Following Command

### For Creating A Table schema

`python manage.py makemigrations`

## For Creating A Table

`python manage.py migrate`

## For run Project

`python manage.py runserver`

## If you want to know Table Structure

** Go to backend folder**
`cd Project/backend`

### Check the models.py file

# API Doc

### Getting all Employees

`GET  /employees`

### create new Employee

`POST /employees`

### Body

`
{
"name":"aakash khan",
"email":"xsyzsyswa@gmail.com",
"phone":9119292992,
"address":"xyz",
"department":"IT",
"designation":"engineering",
"salary":45000

}

`

## task

### Get all employees Task list

`GET /employee/get/task/list`

### Get employee Task list

\_ id :- employee Id

`GET /employee/get/task/list?id=1`

### Update Task

\_ <int:id> :- employee Id
\_ taskId :- which taskn you want to update

`PUT employee/task/<int:id>?taskId=1`

### Body

`
{
"task_name":"working on read me",
"progress":20

}
`

### Create a task for employee

\_ <int:id> :- employee Id

`POST /employee/task/<int:id>`

### Upload Document for employee

\_ <int:id> :- employee Id
\_ type :- document Type

`POST /employee/upload/doc/1?type=pen_card`

### Body

\_ FormData
\_\_ key pdf value file

### Get employees Document

`GET /employees/get/document `

### Get employee Document

\_ <int:id> :- employee Id

`GET employee/get/documents/<int:id>`

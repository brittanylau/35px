# 35px

A Django and Django REST framework project.

## Prerequisites
* Python
* Django
* Django REST framework

## API endpoints

### Users
* **/api/users/** - app root
* **/api/users/users/**
* **/api/users/profiles/**

### Photos
* **/api/photos/** - app root
* **/api/photos/photos/** - list all posts
* **/api/photos/upload/** - upload new photo
* **/api/photos/comments/** - list all comments
* **/api/photos/tags/** - list all tags

### Equipment
* **/api/equipment/** - app root
* **/api/equipment/brands/**
* **/api/equipment/cameras/**
* **/api/equipment/film/**
* **/api/equipment/lenses/**

## Install
`pip install -r requirements.txt`

## Running
`cd 35px`\
`python manage.py runserver`

## Testing
`cd 35px`\
`python manage.py test`

# 35px

A Django and Django REST framework project.

## Prerequisites
* Python
* Django
* Django REST framework

## API endpoints

### Users
| Method | URL | Description |
| --- | --- | --- |
| `GET` | /api/users | API root |
| `GET` | /api/users/users | get list of users |
| `GET` | /api/users/profiles | get list of user profiles |

### Photos

#### Photos
| Method | URL | Description | Authentication |
| --- | --- | --- | --- |
| `GET` | /api/photos | API root |   |
| `GET` | /api/photos/photos | get list of photos |   |
| `GET` | /api/photos/photos/{pk} | get detailed info of a single photo |  |
| `POST` | /api/photos/photos | create a new photo on behalf of user |  |
| `POST` | /api/photos/upload | upload new image file | must be logged in |
| `PATCH` | /api/photos/photos/{pk} | edit info of a single photo | must be logged in as author |
| `DELETE` | /api/photos/photos/{pk} | delete a single photo | must be logged in as author |

#### Comments
| Method | URL | Description | Authentication |
| --- | --- | --- | --- |
| `GET` | /api/photos/comments | get list of comments |   |
| `GET` | /api/photos/comments/{pk} | get detailed info of a single comment |  |
| `POST` | /api/photos/comments | create a new comment on behalf of user |  |
| `PATCH` | /api/photos/comments/{pk} | edit info of a single comment | must be logged in as author |
| `DELETE` | /api/photos/comments/{pk} | delete a single comment | must be logged in as author |

#### Tags
| Method | URL | Description | Authentication |
| --- | --- | --- | --- |
| `GET` | /api/photos/tags | get list of tags |   |
| `GET` | /api/photos/tags/{pk} | get detailed info of a single tag |  |
| `POST` | /api/photos/tags | create a new tag |  |
| `PATCH` | /api/photos/tags/{pk} | edit info of a single tag | must be logged in |
| `DELETE` | /api/photos/tags/{pk} | delete a single tag | must be logged in |

### Equipment

#### Brands
| Method | URL | Description | Authentication |
| --- | --- | --- | --- |
| `GET` | /api/equipment | API root |   |
| `GET` | /api/equipment/brands | get list of brands |   |
| `GET` | /api/equipment/brands/{pk} | get detailed info of a single brand |   |
| `GET` | /api/equipment/cameras | get list of cameras |   |
| `GET` | /api/equipment/cameras/{pk} | get detailed info of a camera |   |
| `GET` | /api/equipment/film | get list of film |   |
| `GET` | /api/equipment/film/{pk} | get detailed info of a film |   |
| `GET` | /api/equipment/lenses | get list of lenses |   |
| `GET` | /api/equipment/lenses/{pk} | get detailed info of a lens |   |
| `POST` | /api/equipment/brands | create a new brand | must be logged in |
| `POST` | /api/equipment/cameras | create a new camera | must be logged in |
| `POST` | /api/equipment/film | create a new film | must be logged in |
| `POST` | /api/equipment/lenses | create a new lens | must be logged in |
| `DELETE` | /api/equipment/brands/{pk} | delete a single brand | must be logged in |
| `DELETE` | /api/equipment/cameras/{pk} | delete a single camera | must be logged in |
| `DELETE` | /api/equipment/film/{pk} | delete a single film | must be logged in |
| `DELETE` | /api/equipment/lenses/{pk} | delete a single lens | must be logged in |

## Install
`pip install -r requirements.txt`\
`cd 35px`\
`python manage.py migrate`

## Running
`python manage.py runserver`

## Testing
`python manage.py test`

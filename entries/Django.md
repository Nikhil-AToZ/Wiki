# Django
---
## Introduction

Django is a high-level **Python web framework** used for building web applications.

It provides features such as URL routing, database management, authentication, forms, templates, security, and an administrative interface.

Django follows the principle of **Don't Repeat Yourself (DRY)** and encourages reusable application components.

## Django Architecture

Django commonly follows a pattern called **Model-Template-View (MTV)**.

```text
User Request
     ↓
    URL
     ↓
   View
   ↙   ↘
Model   Template
   ↓       ↓
Database  HTML
     ↘   ↙
    Response
```

- **Model** manages data and database interactions.
- **View** contains application logic.
- **Template** defines the HTML presented to the user.

## Django Project

A Django project contains the overall configuration of a website.

A project can be created using:

```bash
django-admin startproject myproject
```

The development server can be started with:

```bash
python manage.py runserver
```

## Django Applications

A project can contain multiple applications.

For example:

```text
myproject/
├── blog/
├── accounts/
├── store/
└── manage.py
```

An application can be created using:

```bash
python manage.py startapp blog
```

Applications usually handle specific areas of a project.

## URL Routing

Django uses URL patterns to connect URLs to views.

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

When a user visits the matching URL, Django calls the corresponding view.

## Views

A view receives a request and returns a response.

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")
```

A view can also render a template:

```python
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
```

## Templates

Django templates allow data to be inserted into HTML.

```html
<h1>Hello, {{ name }}</h1>
```

A view can pass data to the template:

```python
def index(request):
    return render(request, "index.html", {
        "name": "Nikhil"
    })
```

Templates also support conditions and loops.

```html
{% for item in items %}
    <p>{{ item }}</p>
{% endfor %}
```

## Models

Models define the structure of data stored in a database.

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Django can use this model to interact with the database.

## Migrations

Migrations track changes made to database models.

Create migrations with:

```bash
python manage.py makemigrations
```

Apply them with:

```bash
python manage.py migrate
```

## Django ORM

Django provides an **Object-Relational Mapper (ORM)** for interacting with databases using Python.

```python
students = Student.objects.all()
```

A new object can be created using:

```python
Student.objects.create(
    name="Nikhil",
    age=18
)
```

The ORM removes the need to write raw SQL for many common operations.

## Forms

Django provides a form system for handling and validating user input.

```python
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
```

Forms can validate submitted data before it is processed.

## Authentication

Django includes a built-in authentication system for:

- Users
- Login
- Logout
- Password management
- Permissions
- Groups

This allows developers to add common authentication functionality without building everything from scratch.

## Django Admin

Django provides an administrative interface for managing database records.

A model can be registered with:

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

The model can then be managed through the admin interface.

## Static Files

Static files include CSS, JavaScript, and images.

A template can load static files using:

```html
{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

## Security

Django includes protection mechanisms for common web security problems, including CSRF, XSS, clickjacking, and unsafe database queries.

However, Django does not automatically make an application completely secure. Developers still need to configure and use the framework correctly.

## Databases

Django supports several databases, including:

- SQLite
- PostgreSQL
- MySQL
- MariaDB
- Oracle

SQLite is commonly used during development, while PostgreSQL and other database systems are often used in production.

## Advantages

- Built with Python
- Many features included out of the box
- Powerful ORM
- Built-in authentication
- Built-in admin interface
- Strong security features
- Large community and ecosystem

## Limitations

- Can feel complex for very small applications.
- Its large feature set creates a learning curve.
- It may provide more functionality than needed for a small service.
- Developers still need to understand HTTP, databases, authentication, and security.

## Django Request Flow

A typical Django request can be represented as:

```text
Browser
   ↓
HTTP Request
   ↓
URL Configuration
   ↓
View
   ↓
Model / Database
   ↓
Template
   ↓
HTTP Response
   ↓
Browser
```

## Conclusion

Django is a powerful Python framework for developing web applications. It connects frontend templates, backend logic, URLs, forms, databases, authentication, and other components into a structured web application.

Learning Django also helps developers understand important backend concepts such as HTTP requests, databases, routing, authentication, and server-side rendering.

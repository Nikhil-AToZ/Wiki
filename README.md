# Wiki

A Django-based encyclopedia web application where users can browse, search, create, edit, and view encyclopedia entries written in Markdown.

## Overview

Wiki is a dynamic web application inspired by Wikipedia. It allows users to interact with encyclopedia entries through a clean web interface while using Django on the backend to handle routing, forms, templates, and application logic.

Each encyclopedia entry is stored as Markdown and converted into HTML when displayed.

## Features

* 🔎 **Search Entries**

  * Search for encyclopedia entries by title.
  * Supports exact matches and partial matches.
  * Search results can redirect directly to an existing entry.

* 📖 **Browse Entries**

  * View a list of all available encyclopedia entries.
  * Open individual entries using their dedicated URLs.

* 📝 **Create New Entries**

  * Create new encyclopedia entries using Markdown.
  * Prevents duplicate entries from being created.

* ✏️ **Edit Entries**

  * Modify the Markdown content of existing entries.
  * Changes are saved and reflected immediately.

* 🎲 **Random Entry**

  * Open a randomly selected encyclopedia entry.

* 📄 **Markdown Support**

  * Entries are written in Markdown.
  * Markdown content is converted to HTML before being rendered.

* 🧭 **Dynamic Routing**

  * Each entry has its own URL based on its title.
  * Django URL namespaces are used to organize application routes.

## Technologies Used

* Python
* Django
* HTML
* CSS
* Markdown
* Git & GitHub

## Project Structure

```text
Wiki/
│
├── encyclopedia/
│   ├── migrations/
│   ├── templates/
│   │   └── encyclopedia/
│   ├── static/
│   │   └── encyclopedia/
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   └── ...
│
├── entries/
│   └── ...
│
├── wiki/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## How It Works

### Viewing an Entry

When a user selects an encyclopedia entry, Django receives the requested title through the URL.

The application retrieves the corresponding Markdown content and converts it into HTML before passing it to the template.

```text
User
  ↓
Entry URL
  ↓
Django URL Router
  ↓
View
  ↓
Retrieve Markdown Content
  ↓
Convert Markdown → HTML
  ↓
Render Template
```

### Searching

Users can enter a search query from the search form.

If the query exactly matches an existing entry, the application redirects the user directly to that entry.

For partial matches, the application displays the relevant entries containing the search term.

### Creating an Entry

Users can create a new entry by providing:

* Entry title
* Markdown content

Before saving the entry, the application checks whether an entry with the same title already exists.

### Editing an Entry

Existing entries can be edited through a dedicated edit page. The current Markdown content is loaded into a form, allowing the user to modify and save it.

## Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Nikhil-AToZ/Wiki.git
cd Wiki
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django markdown
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

Open the application in your browser at:

```text
http://127.0.0.1:8000/
```

## Key Django Concepts Practiced

This project provided practical experience with:

* Django project and app structure
* URL routing
* URL namespaces
* Django views
* Templates
* Template inheritance
* Forms and POST requests
* Handling user input
* Redirects
* Dynamic URL parameters
* Static files
* Markdown processing
* File-based data handling
* Error handling
* Git branching and version control

## What I Learned

Building this project helped strengthen my understanding of how Django connects different parts of a web application:

```text
URL
 ↓
View
 ↓
Application Logic
 ↓
Data
 ↓
Template
 ↓
HTML Response
```

It also provided practical experience debugging common Django issues involving URL patterns, template syntax, form submissions, redirects, and static files.

## Future Improvements

Possible improvements for the project include:

* Add user authentication
* Allow users to manage their own entries
* Add categories or tags
* Add entry revision history
* Improve Markdown sanitization
* Add automated tests
* Improve responsive design
* Add pagination for large numbers of entries
* Replace file-based storage with a database-backed model

## License

This project was created for educational and learning purposes.

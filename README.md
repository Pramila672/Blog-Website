# Blog Application

This is a simple blog application built with Django. It allows users to create, edit, and delete blog posts. Users can also view posts created by others.

## Features

- User authentication (login, logout, register)
- Create, edit, and delete blog posts
- View blog posts by other users
- Authorization checks to ensure users can only edit or delete their own posts

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/blog-application.git
    cd blog-application
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Usage

- Register a new user or log in with an existing account.
- Create a new blog post by navigating to the "New Post" page.
- Edit or delete your own posts by navigating to the post detail page.
- View posts created by other users on the homepage.

# Receipies
Receipies is a simple web application built using Django, where users can manage their favorite recipes. It features functionality for adding, editing, viewing, and deleting recipes, along with user authentication and image upload.

## Features

- **Add, Edit, Delete Recipes**: Users can create, update, or remove their favorite recipes.
- **Recipe Image**: Users can upload an image for each recipe or update it later.
- **User Authentication**: Users can log in to manage recipe collection.
- **Simple UI**: The application comes with a responsive, easy-to-navigate user interface.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Prakhar2706/Receipies-CRUD.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Receipies
   ```
3. Create a virtual environment:
   
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:

   * On Windows:
     
   ```bash
   .\env\Scripts\activate
   ```

   *On macOS/Linux:
   
   ```bash
   source env/bin/activate
   ```
5. Install the dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
6. Create migrations for your models:

   ```bash
   python manage.py makemigrations
   ```
7. Apply migrations:
   
   ```bash
   python manage.py migrate
   ```
8. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
9. Start the development server:
   
   ```bash
   python manage.py runserver
   ```
10. Visit http://127.0.0.1:8000 in your browser to access the app.

11. For admin panel:
    
    ```bash
    http://127.0.0.1:8000/admin
    ```

## Requirements

Django (see requirements.txt for exact version)

## Usage

Once the server is running, you can:

- Add new recipes with a name, description, and image.
- Edit existing recipes if you need to make changes.
- Delete recipes you no longer want.
- Log in as a user to manage your personal recipe collection.

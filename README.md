# timetune
A Django todo app for managing tasks,  and tracking progress. Easy to use and helps you stay organized.

### Quick Start Guide

1. **Clone the repository and navigate to the project directory**
   ```bash
   git clone git@github.com:Nyae44/timetune.git
   cd timetune
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv env
   source env/bin/activate  # Unix/Mac
   env\Scripts\activate  # Windows
   python3 -m venv env
   ```


2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Make database migrations**

    ```bash
    python3 manage.py makemigrations
    then
    python3 manage.py migrate
    ```

4. **Run server**
   

    ```bash
    cd timetune
    python3 manage.py runserver
    ```


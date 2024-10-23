# Flask Guest Episodes API

This is a Flask-based RESTful API that manages episodes, guests, and their appearances on various episodes. The API allows retrieving information about episodes and guests, as well as adding new appearances. This project uses SQLAlchemy for database management and Flask-Migrate for handling migrations.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Database Models](#database-models)
7. [Running Migrations](#running-migrations)
8. [Seeding the Database](#seeding-the-database)
9. [License](#license)

## Features

- RESTful API for episodes, guests, and their appearances.
- Flask-SQLAlchemy ORM for database interactions.
- Data validation and error handling.
- SQLite as the default database for development.
- Database migrations handled by Flask-Migrate.
- Easily extendable for other types of data or additional features.

## Requirements

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-RESTful
- SQLAlchemy-Serializer

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MUCHIRIJOHN1990/Phase-4-Code-Challenge-Late-Show.git
   cd Phase-4-Code-Challenge
   ```

2. **Install dependencies using Pipenv:**

   ```bash
   pipenv install
   ```

3. **Activate the virtual environment:**

   ```bash
   pipenv shell
   ```

4. **Set up the SQLite database:**

   ```bash
   flask db upgrade
   ```

## Usage

1. **Run the application:**

   ```bash
   flask run
   ```

2. The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- **GET /episodes**: Returns a list of all episodes.
- **GET /episodes/{episode_id}**: Returns details of a specific episode.
- **GET /guests**: Returns a list of all guests.
- **POST /appearances**: Adds a new appearance with guest and episode details. Requires the following JSON body:

  ```json
  {
      "rating": 5,
      "episode_id": 1,
      "guest_id": 2
  }
  ```

## Database Models

- **Episode**:
  - `id`: Integer, Primary Key
  - `date`: String, Date of the episode
  - `number`: Integer, Episode number

- **Guest**:
  - `id`: Integer, Primary Key
  - `name`: String, Name of the guest
  - `occupation`: String, Occupation of the guest

- **Appearance**:
  - `id`: Integer, Primary Key
  - `rating`: Integer, Rating of the guest's appearance (1-5)
  - `episode_id`: ForeignKey, Reference to an `Episode`
  - `guest_id`: ForeignKey, Reference to a `Guest`

## Running Migrations

Whenever there are changes to the models, use Alembic migrations to apply the changes to the database:

1. **Create a migration:**

   ```bash
   flask db migrate -m "description of the changes"
   ```

2. **Apply the migration:**

   ```bash
   flask db upgrade
   ```

## Seeding the Database

To populate the database with initial data for testing:

1. Run the `seed.py` script:

   ```bash
   python seed.py
   ```

2. The database will be cleared and repopulated with the initial set of episodes, guests, and appearances.

# Flask Comment System

A simple Flask web application that allows users to create comments and replies. The application uses SQLite databases to store comments and their associated replies.

## Features

- Create new comments
- Reply to existing comments
- Persistent storage using SQLite databases
- Simple and clean interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Minhaj401/hand-for-health-careworkers
cd flaskapp
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install flask
```

## Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Database Structure

The application uses two SQLite databases:

- `comments.db`: Stores main comments
  - Table: `comments`
    - `id`: Integer (Primary Key)
    - `content`: Text

- `replies.db`: Stores replies to comments
  - Table: `replies`
    - `id`: Integer (Primary Key)
    - `content`: Text
    - `comment_id`: Integer (Foreign Key)

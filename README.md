# English Premier League Fixtures API

# **ℹ️ Project Overview**

The "English Premier League Fixtures API" is an API created using Python's Pandas and Flask frameworks, offering real-time access to EPL 2023 -2024 fixtures organized into game weeks.

# **👨‍💻 Technologies**

Python: The core programming language that underpins the API's functionality and logic.

- Flask: A lightweight web framework for Python used to construct API endpoints.
- Pandas: A Python framework employed for efficient CSV data reading and manipulation.

# 🕸️ API Consumption

To interact with the English Premier League API and access its data, adhere to the steps outlined below:

1. **Retrieve All Gameweeks and Fixtures**:
Make a **`GET`** request to the base URL to access all gameweeks and their fixtures:
    
    ```jsx
    https://epl-fixtures-api.sifeddineeddr.repl.co/gameweeks
    ```
    
2. **Retrieve Fixtures for a Specific Gameweek**:
To fetch fixtures for a specific gameweek, replace **`{gameweek_number}`** with the desired gameweek's number in the URI:
    
    ```jsx
    https://epl-fixtures-api.sifeddineeddr.repl.co/gameweeks/{gameweek_number}
    ```
    
3. **Retrieve Team-Specific Fixtures**:
Obtain fixtures for a particular team by replacing **`{team_name}`** with the desired team's name:
    
    ```jsx
    https://epl-fixtures-api.sifeddineeddr.repl.co/gameweeks/{team_name}
    ```
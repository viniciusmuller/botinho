# Botinho

## A bot made with discord.py designed for handling multiple requests simultaneously without concurrence issues.


## Setup

- Clone the repository

    ```bash
    git clone https://github.com/arcticlimer/botinho
    ````

- Enter the application directory

    ```bash
    cd botinho
    ````

- Install the dependencies

    ```bash
    python3 -m pip install -r requirements.txt
    ```

- Provide the necessary TOKEN and DATABASE_URL inside `secrets.example.py`

    ```py
    # secrets.example.py

    # A postgres database url
    # postgresql://[user[:password]@][netloc][:port][/dbname]
    DATABASE_URL=""
    # Your discord bot token
    TOKEN=""
    ```

- Rename it to `secrets.py`

- Start the application

    ```py
    python3 main.py
    ```

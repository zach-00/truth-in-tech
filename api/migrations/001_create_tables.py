steps =[
    [
    """
    CREATE TABLE users(
    id SERIAL PRIMARY KEY NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    avatar_url VARCHAR(1000) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
    );
    """,

    """
    DROP TABLE users;
    """
    ],
    [
    """
    CREATE TABLE companies(
    id SERIAL PRIMARY KEY NOT NULL,
    company_name VARCHAR(50) UNIQUE NOT NULL,
    company_logo VARCHAR(1000) NOT NULL
    );
    """,

    """
    DROP TABLE companies;
    """
    ],
    [
    """
    CREATE TABLE reviews(
    id SERIAL PRIMARY KEY NOT NULL,
    anonymous BOOLEAN DEFAULT FALSE,
    salary DECIMAL(10, 0),
    job_title VARCHAR(50),
    location VARCHAR(50),
    body TEXT,
    user_id INTEGER REFERENCES users(id),
    company_id INTEGER REFERENCES companies(id)
    );
    """,

    """
    DROP TABLE reviews;
    """
    ]
]

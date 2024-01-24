steps = [
    [
        """
    CREATE TABLE accounts(
    id SERIAL PRIMARY KEY NOT NULL,
    username VARCHAR(200) UNIQUE NOT NULL,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    hashed_password VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL
    );
    """,
        """
    DROP TABLE accounts;
    """,
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
    """,
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
    account_id INTEGER REFERENCES accounts(id),
    company_id INTEGER REFERENCES companies(id),
    date_created TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP
    );
    """,
        """
    DROP TABLE reviews;
    """,
    ],
]

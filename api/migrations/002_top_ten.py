steps = [
    [
        """
    CREATE TABLE top_ten(
    id SERIAL PRIMARY KEY NOT NULL,
    salary DECIMAL(10, 0),
    job_title VARCHAR(50),
    location VARCHAR(50),
    body TEXT,
    username VARCHAR(200),
    company_name VARCHAR(200),
    company_logo VARCHAR(1000),
    date_created TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP
    );
        """,
        """
    DROP TABLE top_ten;
    """,
    ],
]

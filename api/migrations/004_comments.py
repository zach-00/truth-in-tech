steps = [
    [
        """
    CREATE TABLE comments(
    id SERIAL PRIMARY KEY NOT NULL,
    body TEXT,
    account_id INTEGER REFERENCES accounts(id),
    review_id INTEGER REFERENCES reviews(id),
    date_created TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP
    );
    """,
        """
    DROP TABLE comments;
    """,
    ],
]

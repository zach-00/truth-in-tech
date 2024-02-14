steps = [
    [
        """
    CREATE TABLE likes(
    id SERIAL PRIMARY KEY NOT NULL,
    account_id INTEGER REFERENCES accounts(id),
    review_id INTEGER REFERENCES reviews(id) ON DELETE CASCADE
    );
    """,
        """
    DROP TABLE comments;
    """,
    ],
]

steps = [
    [
        """
    ALTER TABLE reviews
    ADD likes INTEGER DEFAULT(0);
    """,
        """
    DROP TABLE accounts;
    """,
    ],
]

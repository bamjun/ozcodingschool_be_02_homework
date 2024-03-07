from pysql import connection

with connection.cursor() as cursor:
    cursor.execute(
        """
        CREATE TABLE articles (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            author VARCHAR(255) NOT NULL,
            body TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL
        )
        """
    )

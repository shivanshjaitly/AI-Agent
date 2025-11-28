import mysql.connector

class DatabaseAdapter:

    def run(self, query):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Iwilldoit@1103",
            database="finance",
            auth_plugin="mysql_native_password"
        )

        cursor = conn.cursor()
        cursor.execute(query)

        row = cursor.fetchone()

        conn.close()

        # ✅ SAFETY CHECK
        if row is None or row[0] is None:
            return 0

        return row[0]

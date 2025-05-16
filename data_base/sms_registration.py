import pyodbc
import platform

class SmsRegistration:
    @staticmethod
    def get_last_sms_by_phone(phone):
        if platform.system() == "Windows":
            driver = "SQL Server"
        else:
            driver = "ODBC Driver 18 for SQL Server"  # או 17 אם 18 לא מותקן

        connection_string = (
            f"DRIVER={{{driver}}};"
            "SERVER=10.1.6.165;"
            "DATABASE=AppDes_Pay24;"
            "UID=yanirp;"
            "PWD=Yp654123&;"
        )

        try:
            # Connect to the database
            with pyodbc.connect(connection_string) as connection:
                # Adjust the query to fetch the last record based on ID
                query = """
                SELECT TOP 1 Code 
                FROM tbl_SmsRegistration 
                WHERE Phone = ? 
                ORDER BY Id DESC
                """

                # Execute the query with parameterized input
                with connection.cursor() as cursor:
                    cursor.execute(query, (phone,))
                    row = cursor.fetchone()

                    # Check if a result is found
                    if row:
                        return row[0]  # Adjust based on the column index or name
                    else:
                        raise Exception("No SMS found")
        except Exception as e:
            print(f"Error: {e}")
            raise

import pyodbc
import platform
import os

class SmsRegistration:
    @staticmethod
    def get_last_sms_by_phone(phone):
        if os.getenv("CI") == "true" and phone == os.getenv("CI_TEST_PHONE"):
            print("Using fixed password for CI")
            return os.getenv("CI_TEST_PASSWORD")

        if platform.system() == "Windows":
            driver = "SQL Server"
        else:
            driver = "ODBC Driver 18 for SQL Server"

        connection_string = (
            f"DRIVER={{{driver}}};"
            "SERVER=10.1.6.165;"
            "DATABASE=AppDes_Pay24;"
            "UID=yanirp;"
            "PWD=Yp654123&;"
        )

        try:
            with pyodbc.connect(connection_string) as connection:
                query = """
                SELECT TOP 1 Code 
                FROM tbl_SmsRegistration 
                WHERE Phone = ? 
                ORDER BY Id DESC
                """
                with connection.cursor() as cursor:
                    cursor.execute(query, (phone,))
                    row = cursor.fetchone()
                    if row:
                        return row[0]
                    else:
                        raise Exception("No SMS found")
        except Exception as e:
            print(f"Error: {e}")
            raise

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for the ORM
Base = declarative_base()

# Define the model for the tbl_SmsRegistration table
class SmsRegistrationModel(Base):
    otp = 'tbl_SmsRegistration'  # Specify the actual table name here

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Phone = Column(String)
    Code = Column(String)

# Define the SmsRegistration class with ORM
class SmsRegistration:
    # Class variable to hold the session factory
    engine = create_engine("mssql+pyodbc://yanirp:Yp654123&@10.1.6.165/AppDes_Pay24?driver=ODBC+Driver+17+for+SQL+Server")
    Session = sessionmaker(bind=engine)

    @staticmethod
    def get_last_sms_by_phone(phone):
        # Create a new session
        session = SmsRegistration.Session()
        try:
            # Query the database using ORM
            last_sms = (
                session.query(SmsRegistrationModel)
                .filter_by(Phone=phone)
                .order_by(SmsRegistrationModel.Id.desc())
                .first()
            )

            if last_sms:
                return last_sms.Code
            else:
                raise Exception("No SMS found")
        except Exception as e:
            print(f"Error: {e}")
            raise
        finally:
            session.close()

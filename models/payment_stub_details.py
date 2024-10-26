import json

class PaymentStubDetailsModel:
    def __init__(self, company_Name: str, companyId: str, Payer_Number: str, Stub_Number: str):
        self.company_name = company_Name
        self.company_id = companyId
        self.payer_number = Payer_Number
        self.stub_number = Stub_Number

def get_payment_stub_details():
    file_path = r'C:\Repos\AutomationPython\tests\StubsForPayment.json'  # Use raw string
    with open(file_path, encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data

for payment_stub in get_payment_stub_details():
    print(f"PayerNumber: {payment_stub['PayerNumber']}, StubNumber: {payment_stub['StubNumber']}")

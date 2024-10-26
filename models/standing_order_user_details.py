class StandingOrderModel:
    def __init__(self, name: str, id: str, phone: str, payer: str, asset: str, mail: str):
        self.name = name
        self.id = id
        self.phone = phone
        self.payer = payer
        self.asset = asset
        self.mail = mail

# Example data for the test
standing_order_data = StandingOrderModel(
    name="יניר טסט",
    id="039901186",
    phone="0503021038",
    payer="039901186",
    asset="160076001000",
    mail="yanirqa10@gmail.com"
)
class CreditCardModel:
    def __init__(self, card_number: str, month: str, year: str):
        self.card_number = card_number
        self.month = month
        self.year = year

credit_card_data = CreditCardModel(
    card_number="5326140282245281",
    month="10",
    year="2026"

)

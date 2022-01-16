class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, Bill, flatmate2):
        return Bill.amount * (self.days_in_house) / (self.days_in_house + flatmate2.days_in_house)


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


bill = Bill(120, "March 2021")
john = Flatmate("John", 20)
mary = Flatmate("Mary", 25)

print(john.pays(bill, mary))

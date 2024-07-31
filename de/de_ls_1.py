# Schreibt bitte eine Funktion, dass “Hallo an alle “ ausgibt
def hallo():
    print("Hallo an alle ")


# Erstellen Sie eine Funktion
# sumTransactionAmounts(transactions),
# die eine Liste von Wörterbüchern
# mit Informationen zu Transaktionen
# (Betrag und Währung) akzeptiert
# und den Gesamtbetrag in Dollar
# unter Anwendung des aktuellen Wechselkurses zurückgibt.

def sumTransactionAmounts(transactions):
    sum = 0
    for transaction in transactions:
        if transaction["currency"] == "eur":
            sum += transaction["amount"] * 1.08
        else:
            sum += transaction["amount"]
    return sum


# Erstellen Sie eine Funktion convertPhoneNumbers(phones),
# die eine Liste von Telefonnummern aus
# verschiedenen internationalen Formaten
# in ein einheitliches Standardformat umwandelt,
# das mit einem + Zeichen beginnt und nur
# Zahlen enthält, ohne Leerzeichen,
# Klammern oder Bindestriche.
# Zum Beispiel sollte +1(999)12-34-456 in +19991234456
# umgewandelt werden.
def convertPhoneNumbers(phones):
    for i in range(len(phones)):
        phone = phones[i]
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")
        phone = phone.replace("-", "")
        phone = phone.replace(" ", "")
        phone = phone.replace("+", "")
        phones[i] = "+" + phone
    return phones





if __name__ == "__main__":
    hallo()
    transactions = [
        {"amount": 100, "currency": "usd"},
        {"amount": 200, "currency": "usd"},
        {"amount": 300, "currency": "usd"},
        {"amount": 100, "currency": "eur"},
    ]
    print(f" GesamteSumme ist: {sumTransactionAmounts(transactions)} USD")

    list_numbers = [
        "+1(999)12-34-456",
        "+1(999)12-34-457",
        "+1(999)12-34-458"
    ]
    print(convertPhoneNumbers(list_numbers))
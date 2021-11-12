@classmethod
def from_csv(cls, csv_file):
    accounts = []

    with open(csv_file) as file:
        reader = csv.reader(file)

        for account_number, account_name, balance in reader:
            accounts.append(
                cls(account_number, account_name, int(balance)))

    return accounts
import csv

class Login:
    def __init__(self, filename="../model/users.csv"):
        self.filename = filename

    def register(self, username, password):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        return True

    def check_credentials(self, username, password):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username and row[1] == password:
                        return True
            return False
        except FileNotFoundError:
            return False

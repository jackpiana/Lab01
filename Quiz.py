import random

class Quiz:
    def __init__(self, row):
        self.domanda = row[0]
        self.livello = row[1]
        self.corretta = row[2]
        self.opzioni = [row[3], row[4], row[5], row[2]]

    def __str__(self):
        random.shuffle(self.opzioni)
        return (f"Livello: {self.livello}"
                f"{self.domanda}"
                f"a. {self.opzioni[0]}"
                f"b. {self.opzioni[1]}"
                f"c. {self.opzioni[2]}"
                f"d. {self.opzioni[3]}")

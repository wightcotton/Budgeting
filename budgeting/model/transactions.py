import pickle

# a transaction record is a list of date, category and a concatenated string of everything else
# transaction records are stored in a set to ensure there are no duplicates

class Transactions:
    def __init__(self):
        # load pickled dict
        self.dataset = set([])
            #pickle.load("C:/Users/Bob/Documents/money/budget/transactions.pi")

    def add(self, aList ):
        self.dataset.add( aList )

    def p(self):
        for r in self.dataset:
            print(sorted( r, key=lambda i:i[0] ) )
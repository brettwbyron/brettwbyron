class Domino(object):

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __str__(self):
        return "|" + str(self.head) + ":" + str(self.tail) + "|"

    def flip(self):
        #this method should switch out the head and the tail values
        pass

    def fits(self, other):
        #this methods should return True if the two dominoes are compatible
        #and false otherwise
        pass

class Chain(object):

    def __init__(self):
        self.dominoes = []
        self.chain = []

    def __str__(self):
        reply = "Current chain: "

        #the output here should mimic that of the example

        return reply

    def add(self, domino):
        self.dominoes.append(domino)

    def play(self, num):
        #here we should attempt to add domino # num to the chain
        #and print out success or failure
        pass

    def moves(self, num_list):
        #given a list of numbers, we try to make those plays in that order
        pass

#main - test code
my_chain = Chain()
my_chain.add(Domino(2,3))
my_chain.add(Domino(6,4))
my_chain.add(Domino(1,3))
my_chain.add(Domino(4,1))
my_chain.moves([0,1,0,1,0])
print my_chain

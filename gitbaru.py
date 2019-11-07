
class karnivora:
    def __init__(self):
        self.karnivora = 'daging'

class herbivora:
    def __init__(self):
        self.herbivora = 'tumbuhan'

class omnivora(karnivora, herbivora):
    def __init__(self):
        karnivora.__init__(self)
        herbivora.__init__(self)
        self.mcd = 'mcd'

objo = omnivora()
print(vars(objo))


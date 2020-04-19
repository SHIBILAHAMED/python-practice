class hello(object):
    def override(self):
        print("\n OTHER  override()")

    def implicit(self):
        print ("\n OTHER  implicit()")

    def altered(self):
        print ("\n OTHER  altered()")

class child (object):

    def __init__(self):
        self.other= hello()

    def implicit(self):
        self.other.implicit()
        print ("c is ")

    def override(self):
        print ("\n child override()")

    def altered(self):
        print ("\n child before other altered()")
        self.other.altered()
        print("\n child after other altered()")


son =child()

son.implicit()
son.override()
son.altered()

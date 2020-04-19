class parent (object):

    def override(self):
        print("\n parent override()")

    def implicit(self):
        print ("\n parent implicit()")
    def altered(self):
        print ("\n parent altered()")


class child (parent):

    def override(self):
        print ("\n child override()")

    def altered(self):
        print ("\n child before parent altered()")
        super().altered()
        print ("\n child after parent altered()")


dad = parent()
son = child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

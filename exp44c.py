class parent(object):
    def altered(self):
        print("parent altererd()")

class child(parent):

    def altered(self):

        print ("child before parent altered()")
        super(child, parent).altered()
        print ("child after parent altered()")

dad=parent()
son= child()

dad.altered()
son.altered()

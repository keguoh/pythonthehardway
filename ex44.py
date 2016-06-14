class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print "\n"




class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

print "\n"



class Parent(object):

    def altered(self):
        print "PARENT altered()\n"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()\n"

dad = Parent()
son = Child()

dad.altered()
son.altered()
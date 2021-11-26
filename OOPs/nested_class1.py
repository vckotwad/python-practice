#nested class
class Human:
    def __init__(self):
        print("Human object created")
        self.head=self.Head()
    class Head:
        def __init__(self):
            print("Head object created")
            self.brain=self.Brain()
        def talk(self):
            print(" I am talking")
        class Brain:
            def __init__(self):
                print("brain object created")
                self.Nervous_system=self.Nervous_system()
            def think(self):
                print("I am thinking")
            class Nervous_system:
                def __init__(self):
                    print("nervous system object is created")
                def signal(self):
                    print("Nervous system is passing signal")




h=Human()
h.head.talk()
h.head.brain.think()
h.head.brain.Nervous_system.signal()

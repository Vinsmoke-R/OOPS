#Single Inheritance 
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"The {self.name} makes a sound")

class Dog(Animal):
    def bark(self):
        print(f"The {self.name} barks")

dog = Dog("Jonny")
print(dog.name)
dog.bark()

# ---------------------------------------------------------------------------

# Multilevel Inheritance

class Grandparent:
    def __init__(self, name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story.")

    # Intermediate class
class Parent(Grandparent):

    def work(self):
        print(f"{self.name} is working.")

    # Derived class
class Child(Parent):

    def play(self):
        print(f"{self.name} is playing.")

    # Create an instance of Child
child = Child("Charlie")
child.tell_story()  # Output: Charlie tells a story.
child.work()        # Output: Charlie is working.
child.play()        # Output: Charlie is playing.


# ---------------------------------------------------------------------------

# Hierarchical Inheritance

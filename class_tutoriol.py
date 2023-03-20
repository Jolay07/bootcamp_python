
class Human():
    def __init__(self, name, surname, age):
        self.different = name
        self.surname = surname
        self.age = age

    def greeting(self):
        print(f"Hey {self.different}, wake up!")

    def running(self):
        print(f"Is not able to run")

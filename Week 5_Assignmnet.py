# Base class
class Device:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"This is a device from {self.brand}.")

# Smartphone class inherits from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage):
        super().__init__(brand)  # Call the parent constructor
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def info(self):
        # Polymorphism: override the method from Device
        print(f"{self.brand} {self.model} with {self.storage}GB storage.")

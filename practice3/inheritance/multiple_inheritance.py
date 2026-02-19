# 1. Combining Smartphone features
class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def call(self):
        print("Calling...")

class SmartPhone(Camera, Phone):
    pass

# 2. Multi-functional Printer
class Printer:
    def print_doc(self):
        print("Printing document")

class Scanner:
    def scan_doc(self):
        print("Scanning document")

class AllInOne(Printer, Scanner):
    pass

# 3. Hybrid Vehicle
class Electric:
    def charge(self):
        print("Charging battery")

class Gas:
    def refuel(self):
        print("Refueling tank")

class HybridCar(Electric, Gas):
    pass

sp = SmartPhone()
sp.call()
sp.take_photo()
# 1. Basic Sound overriding
class Bird:
    def sound(self):
        print("Bird makes a sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot says: Hello!")

# 2. Payment system overriding
class Payment:
    def process(self):
        print("Processing general payment")

class CryptoPayment(Payment):
    def process(self):
        print("Processing Bitcoin transaction via Blockchain")

# 3. UI Element overriding
class Element:
    def render(self):
        print("Rendering basic element")

class Button(Element):
    def render(self):
        print("Rendering a clickable Button")

p = Parrot()
p.sound() # Overridden method
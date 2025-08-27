# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"


# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # Call parent constructor
        self.storage = storage
        self.battery = battery
    
    def call(self, contact):
        return f"📞 Calling {contact} from {self.device_info()}..."
    
    def charge(self, percent):
        self.battery += percent
        return f"🔋 Battery charged to {self.battery}%"
    
    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}%"

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 50)
print(phone1.phone_info())
print(phone1.call("Alice"))
print(phone1.charge(30))

class Car:
    # Class Attributes
    cars = []

    def __init__(self, model, color):
        # Instance Attributes
        self.model = model
        self.color = color
        Car.cars.append(self)

    # Instance Method
    def print_details(self):
        print(self.model)
        print(self.color)

    
    # Class Methods
    @classmethod
    def display_company_name(cls):
        print(cls.company)

    @staticmethod
    def is_valid_model(model):
        
        valid_models = ["Tesla Model S" , "Toyota Corolla", "Ford Mustang"]
        return model in valid_models
    
    @classmethod
    def change_company_name(cls , name):
        cls.company = name






if Car.is_valid_model("Tesla Model S"):
    Car("Tesla Model S" , "RED")


for x in Car.cars:
    x.print_details()
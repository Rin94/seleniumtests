class Car:

    def __init__(self, brand,model, color, fuel):
        self.brand=brand
        self.model=model
        self.color=color
        self.fuel=fuel

    def start(self):
        pass
    def halt(self):
        pass
    def drift(self):
        pass
    def speedup(self):
        pass
    def turn(self):
        pass
    def __str__(self):
        return f"car model: {self.model}, brand: {self.brand}."

class Van(Car):

    def __init__(self,*args,**kwargs):
        super(Van,self).__init__(*args,**kwargs)

    def __str__(self):
        return f"van model: {self.model}, brand: {self.brand}."


if __name__ == '__main__':
    blackverna=Car('Hyundai', "Verna", "Black", 'Oil')

    ranger=Van('Ford', "Ranger", "Red", 'diesel')
    print(blackverna.__str__())
    print(ranger.__str__())
class Car:
    speed = 0
    def __init__(self, Nbrand, Nyear, Nmoteur, Ncolor):
        self.brand = Nbrand
        self.year = Nyear
        self.moteur = Nmoteur
        self.color = Ncolor
    
    def Accelerate(self, speednbr):
        self.speed = self.speed + speednbr
        print(f"Current speed of {self.brand} km/h is {self.speed}km/h")
    
    def Deaccelerate(self):
        self.speed = max(self.speed - 10 ,0)
        print(f"Current speed of {self.brand} km/h is {self.speed}km/h")

    def SpeedLimit(self):
        print("ALERT ALERT OVER SPEED LIMIT")
        while self.speed != 100:
            self.Deaccelerate()

car1 = Car("Mercedes", "2017", "2.0", "Black")
car2 = Car("Audi", "2022", "2.2", "Red")

while True:
    car1.Accelerate(10)
    car2.Accelerate(20)
    if car1.speed >= 150:
        car1.SpeedLimit()
    if car2.speed >= 150:
        car2.SpeedLimit()
    if car1.speed == 100 and car2.speed == 100:
        break 


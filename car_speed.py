class car_simulator:
    def __init__(self,st,re):
        self.st = st
        self.re = re
        self.car = False
        self.speed = 30

    def start(self):
        if self.car:
            print(f"{self.re} your car")
            return

        self.car = True
        print(f"car is {self.st}")

    def gear1(self):
        if  self.car:
            print(f"car in first gear:{self.speed}km/h")
            return

        self.car = True
        self.speed = 0
        print("gear1 is stopped")

    def gear2(self):
        self.speed += 30
        print(f"car in second gear:{self.speed}km/h")


    def gear3(self):
        self.speed += 30
        print(f"car in third gear:{self.speed}Km/h")

    def gear4(self):
        self.speed += 30
        print(f"car in fourth gear:{self.speed}Km/h")

    def gear5(self):
        self.speed += 30
        print(f"car in fifth gear:{self.speed}Km/h")

    def brake(self):
        if self.speed  <= 100:
            print(f"Nice Going:{self.speed} km/h")
            return
        print(f"Too Dangerous:{self.speed}km/h")
        self.speed -= 40
        if self.speed  < 0 :
            self.speed = 0
        print(f"slow your car speed:{self.speed}Km/h")
        self.speed = 180




    def display_speed(self):
        print("------------------------------------")
        print("          Speed Limit Test")
        print("------------------------------------")
        print(f"Kilometer Speed Test:   {self.speed} km/h")



g=car_simulator("started","restart")
g.start()
g.gear1()
g.gear2()
g.gear3()
g.gear4()
g.brake()
g.display_speed()
class Car:

    def __init__(self, color, max_speed, acceleration, tyre_friction, current_speed):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.start_engine = False
        self.current_speed = current_speed

    def stop_engine(self):
        self.start_engine = False
        print("Engine stopped")

    def startEngine(self):
        self.start_engine = True
        print("Engine Started")

    def Acceleration(self,speed):
        self.speed = speed
        if self.current_speed >= self.max_speed:
            print("max speed is reached")
        else:
            self.current_speed += speed
            print("Accelereation Applied, Current speed is", self.current_speed)

    def apply_breaks(self,tyre_friction):
        self.tyre_friction = tyre_friction
        if  self.current_speed > 0 and self.current_speed >= self.max_speed:
            self.current_speed -= tyre_friction
            print("breaks  are applied, current speed",self.current_speed)
        else:

            print("breaks cant be applied")
    def sound_horn(self):
        if self.start_engine is True:
            print("Beep Beep")
        else:
            print("car has not started yet")
carObj = Car("Black", 120, 10, 20, 60)
print(carObj)

carObj.stop_engine()
carObj.startEngine()
carObj.Acceleration(50)
carObj.apply_breaks(15)
carObj.sound_horn()



class cars:
    def __init__(self):
        self.color1 = "red"

class renault(cars):
    __VIN = "SQE546"
    __VIN1 = "24242"
    
    def __init__(self, model, driver):
        super().__init__()
        self.model = model
        self.driver = driver

    def info(self):
        print(f"This is {self.color1} Renault {self.model}. My name is {self.driver}. "
              f"And i am driver of this car. Let's start the engine: ")

    def engine_sound(self):
        print("Pshhbrrrrrrr")

    def giftakey(self):
        print("Now I gift you keys from my car")
        print(self.__VIN + self.__VIN1)

class bugatti(cars):
    VIN = 42349341
    VIN1 = 2349341

    def __init__(self, model, driver):
        super().__init__()
        self.model = model
        self.driver = driver

    def info(self):
        print(f"This is {self.color1} Bugatti  {self.model}. My name is {self.driver}. And i am driver of this car. Let's start the engine: ")

    def engine_sound(self):
        print("VROOOOOM RRRRR")

    def __giftakey(self): #для вывода численного значения не обходимо убрать двойное подчеркивание, тогда класс станет открытым
        print("Now I gift you keys from my car")
        print(self.VIN + self.VIN1)

renault1 = renault("Logan", "Shamil")
bugatti1 = bugatti("Chiron", "Pablo")

for car in (renault1, bugatti1):
    car.info()
    car.engine_sound()
    car.giftakey()
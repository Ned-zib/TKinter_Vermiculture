class data(object):
    def __init__(self, temperature, humidity, fan, heater, pump):
        self.temperature = temperature
        self.humidity = humidity
        self.fan = fan
        self.heater = heater
        self.pump = pump

    def setData(self, temperature, humidity, fan, heater, pump):
        self.temperature = temperature / 100
        self.humidity = humidity / 100
        self.fan = fan
        self.heater = heater
        self.pump = pump

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getFan(self):
        return self.fan

    def getHeater(self):
        return self.heater

    def getPump(self):
        return self.pump

    def printData(self):
        print(self.temperature)
        print(self.humidity)
        print(self.fan)
        print(self.heater)
        print(self.pump)

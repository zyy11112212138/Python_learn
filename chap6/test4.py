class Car():
    def __init__(self, car_type, car_num):
        self.car_type = car_type
        self.car_num = car_num

    def start(self):
        pass;
    def stop(self):
        pass;

class Taxi(Car):
    def __init__(self, car_type, car_num, car_company):
        super().__init__(car_type, car_num)
        self.car_company = car_company

    def start(self):
        print('乘客您好！')
        print(f'我是{self.car_company}出租公司，我的车牌是{self.car_num}，您要去哪里')

    def stop(self):
        print('目的地到了，请您扫码付款，欢迎下次乘坐')

class FamilyCar(Car):
    def __init__(self, car_type, car_num, name):
        super().__init__(car_type, car_num)
        self.name = name

    def start(self):
        print(f'我是{self.name}，老子想咋开咋开')

    def stop(self):
        print('下车')

taxi = Taxi('大众','渝A1111','重庆出租车')
fc = FamilyCar('奔驰','渝B88888','曾垚垚')

taxi.start()
taxi.stop()
fc.start()
fc.stop()
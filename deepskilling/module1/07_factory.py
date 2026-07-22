class Car:
    def drive(self): print('Driving Car')
class Bike:
    def drive(self): print('Riding Bike')
class Factory:
    @staticmethod
    def get(v): return Car() if v=='car' else Bike()
Factory.get('car').drive()

class Singleton:
    _i=None
    def __new__(cls):
        if not cls._i: cls._i=super().__new__(cls)
        return cls._i
print(Singleton() is Singleton())

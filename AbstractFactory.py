from abc import ABCMeta, abstractmethod

class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self):
        pass

class JapaneseEngine(IEngine):
    def release_engine(self):
        print('Японский Двигатель')

class RussianEngine(IEngine):
    def release_engine(self):
        print('Русский Двигатель')

class ChineseEngine(IEngine):
    def release_engine(self):
        print('Китайский Двигатель')


class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self, engine: IEngine):
        pass

class JapaneseCar(ICar):
    def release_car(self, engine: IEngine):
        print('Собрали Японский Автомобиль, ', end='')
        engine.release_engine()

class RussianCar(ICar):
    def release_car(self, engine: IEngine):
        print('Собрали Русский Автомобиль, ', end='')
        engine.release_engine()

class СhineseCar(ICar):
    def release_car(self, engine: IEngine):
        print('Собрали Китайский Автомобиль, ', end='')
        engine.release_engine()


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self) -> IEngine:
        pass
    @abstractmethod
    def create_car(self) -> ICar:
        pass

class JapaneseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return JapaneseEngine
    def create_car(self) -> ICar:
        return JapaneseCar

class RussianFactory(IFactory):
    def create_engine(self) -> IEngine:
        return RussianEngine
    def create_car(self) -> ICar:
        return RussianCar

class СhineseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return ChineseEngine
    def create_car(self) -> ICar:
        return СhineseCar



if __name__ == '__main__':
    j_factory = JapaneseFactory()
    j_engine = j_factory.create_engine()
    j_car = j_factory.create_car()

    j_car.release_car(j_engine)





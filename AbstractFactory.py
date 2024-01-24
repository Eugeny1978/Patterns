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
        return JapaneseEngine()
    def create_car(self) -> ICar:
        return JapaneseCar()

class RussianFactory(IFactory):
    def create_engine(self) -> IEngine:
        return RussianEngine()
    def create_car(self) -> ICar:
        return RussianCar()

class СhineseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return ChineseEngine()
    def create_car(self) -> ICar:
        return СhineseCar()


if __name__ == '__main__':
    jp_engine = JapaneseEngine()
    jp_car = JapaneseCar()
    print('jp_engine', jp_engine)
    print('jp_car', jp_car)

    j_factory = JapaneseFactory()
    j_engine = j_factory.create_engine()
    j_car = j_factory.create_car()
    print('j_engine', j_engine)
    print('j_car', j_car)


    r_factory = RussianFactory()
    r_engine = r_factory.create_engine()
    r_car = r_factory.create_car()

    ch_factory = СhineseFactory()
    ch_engine = ch_factory.create_engine()
    ch_car = ch_factory.create_car()

    j_car.release_car(engine=j_engine)
    r_car.release_car(r_engine)
    ch_car.release_car(ch_engine)







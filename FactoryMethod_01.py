def metod_A(data):
    print('Выполняются действия по методу "А" | Точность 0')
    return round(data, 0)

def metod_B(data):
    print('Выполняются действия по методу "B" | Точность 1')
    return round(data, 1)

def metod_C(data):
    print('Выполняются действия по методу "C" | Точность 2')
    return round(data, 2)

def metod_D(data):
    print('Выполняются действия по методу "D" | Преобразуется в Целое (дробная часть отбрасывается)')
    return int(data)

def get_metod(method_name):
    match method_name:
        case 'A':
            return metod_A
        case 'B':
            return metod_B
        case 'C':
            return metod_C
        case 'D':
            return metod_D
        case _:
            raise ValueError(method_name)

metods = {
    'A': metod_A,
    'B': metod_B,
    'C': metod_C,
    'D': metod_D
}

class CalculateAccuracy:

    def calculate(self, data, method_name):
        calculator = get_metod(method_name)
        result = calculator(data)
        print(result)
        return result

    def calculate2(self, data, method_name):
        try:
            result = metods[method_name](data)
        except:
            raise ValueError(method_name)
        print(result)
        return result
    

if __name__ == '__main__':
     obj = CalculateAccuracy()
     obj.calculate(10.7467889, 'A')
     obj.calculate(10.7467889, 'B')
     obj.calculate(10.7467889, 'C')
     obj.calculate(10.7467889, 'D')

     obj.calculate2(10.7467889, 'A')
     obj.calculate2(10.7467889, 'B')
     obj.calculate2(10.7467889, 'C')
     obj.calculate2(10.7467889, 'D')

     obj.calculate2(10.3467889, 'E')

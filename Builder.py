from abc import ABCMeta

class Phone:
    def __init__(self):
        self.data: str = ''
    def about_phone(self):
        return self.data
    def append_data(self, string: str):
        self.data += string

class IDeveloper(metaclass=ABCMeta):
    def create_display(self):
        pass
    def create_box(self):
        pass
    def install_system(self):
        pass
    def get_phone(self) -> Phone:
        pass

class AndroidDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data('Произведен Дисплей Samsung; ')
    def create_box(self):
        self.__phone.append_data('Произведен Корпус Samsung; ')
    def install_system(self):
        self.__phone.append_data('Установлена Система Android 12.4; ')
    def get_phone(self) -> Phone:
        return self.__phone

class IphoneDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()
    def create_display(self):
        self.__phone.append_data('Произведен Дисплей IPhone; ')
    def create_box(self):
        self.__phone.append_data('Произведен Корпус IPhone; ')
    def install_system(self):
        self.__phone.append_data('Установлена Система IOS 9.7 ; ')
    def get_phone(self) -> Phone:
        return self.__phone

class Director:
    def __init__(self, developer: IDeveloper):
        self.__developer = developer
    def set_developer(self, developer: IDeveloper):
        self.__developer = developer
    def mount_only_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        return self.__developer.get_phone()
    def mount_full_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        self.__developer.install_system()
        return self.__developer.get_phone()


if __name__ == '__main__':

    android_dev: IDeveloper = AndroidDeveloper()
    director = Director(android_dev)
    samsung: Phone = director.mount_full_phone()
    print(samsung.about_phone())

    iphone_dev: IDeveloper = IphoneDeveloper()
    director.set_developer(iphone_dev)

    iphone: Phone = director.mount_only_phone()
    print(iphone.about_phone())
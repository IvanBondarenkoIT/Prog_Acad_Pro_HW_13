import abc


# 1) Создайте ABC класс с абстрактным методом проверки целого числа на
# простоту. Т.е., если параметром этого метода является целое число и оно
# простое, то метод должен вернуть True, а в противном случае False.
class AbstractPrime(abc.ABC):
    @abc.abstractmethod
    def is_prime_number(self, num: int):
        if not isinstance(num, int):
            return False  # raise TypeError
        else:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        return False
                    else:
                        return True
            else:
                return False

    @classmethod
    def __subclasshook__(abc_class, cls):
        for sub_class in cls.__mro__:
            for property_name in sub_class.__dict__:
                if property_name == "is_prime_number":
                    return True
        return False


# 2) Создайте класс его наследующий.
class SuccessorClass(AbstractPrime):
    def is_prime_number(self, num: int):
        return super().is_prime_number(num)


# 3) Создайте класс, который не наследует пользовательский ABC класс, но
# обладает нужным методом. Зарегистрируйте его в качестве виртуального
# подкласса.
class MyClass:
    def is_prime_number(self, num: int):
        if not isinstance(num, int):
            return False  # raise TypeError
        else:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        return False
                    else:
                        return True
            else:
                return False


# 4) Проверьте работоспособность проекта.
def test(obj):
    print(f"isinstance {isinstance(obj, AbstractPrime)}")
    print(obj.is_prime_number(-11))
    print(obj.is_prime_number(1))
    print(obj.is_prime_number(0))
    print(obj.is_prime_number("7"))
    print(obj.is_prime_number(5.0))
    print(obj.is_prime_number(3))
    print(obj.is_prime_number(7))
    print(obj.is_prime_number(9))
    print(obj.is_prime_number(10))
    print(obj.is_prime_number(11))
    print(obj.is_prime_number(11111))
    

def main():
    successor_inst = SuccessorClass()
    test(successor_inst)
    SuccessorClass.register(MyClass)  # HW 13.3
    my_inst = MyClass()
    test(my_inst)
    

if __name__ == "__main__":
    main()



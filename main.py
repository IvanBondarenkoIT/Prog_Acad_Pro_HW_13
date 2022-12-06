'''Домашнее задание


3) Создайте класс, который не наследует пользовательский ABC класс, но
обладает нужным методом. Зарегистрируйте его в качестве виртуального
подкласса.
4) Проверьте работоспособность проекта.'''

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


# 2) Создайте класс его наследующий.
class MyClass(AbstractPrime):
    def is_prime_number(self, num: int):
        return super().is_prime_number(num)


def main():
    c1 = MyClass()
    print(c1.is_prime_number(-11))
    print(c1.is_prime_number(1))
    print(c1.is_prime_number(0))
    print(c1.is_prime_number("7"))
    print(c1.is_prime_number(5.0))
    print(c1.is_prime_number(3))
    print(c1.is_prime_number(7))
    print(c1.is_prime_number(9))
    print(c1.is_prime_number(10))
    print(c1.is_prime_number(11))
    print(c1.is_prime_number(11111))

if __name__ == "__main__":
    main()



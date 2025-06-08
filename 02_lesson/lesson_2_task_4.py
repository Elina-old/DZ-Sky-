n = int(input("Введите число:"))


def fizz_buzz(n):
    for i in range(3, n + 5):
        if i % 15 == 0:
            print(f"{i} - FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} - Fizz ")
        elif i % 5 == 0:
            print(f"{i} - Buzz")

        else:
            print(i)


fizz_buzz(15)

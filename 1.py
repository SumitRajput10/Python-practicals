class numeric_error(Exception):
    pass
def get_values():
    """ For getting values in string format """
    print("Enter first number:")
    num1 = input()

 #exception handling for string number-1 for numeric entry or for unsuccessful conversion
    try:
        if num1.isnumeric():
            raise numeric_error
    except numeric_error:
        print("Enter number in string format.")
        exit()
    try:
        number1 = int(string_to_num(num1))
    except ValueError:
        print("Please enter correct format")
        exit()

 # exception handling for string number-2 for numeric entry or for unsuccessful conversion
    print("Enter second number:")
    num2 = input()
    try:
        if num2.isnumeric():
            raise numeric_error
    except numeric_error:
        print("Enter number in string format.")
        exit()

    try:
        number2 = int(string_to_num(num2))
    except ValueError:
        print("Please enter correct format")
        exit()

    else:

        temp = str(Gcd(number1, number2))  # converting the returned GCD to string
        result = num_to_string(temp)
        print(f"Result is {result}")


def string_to_num(num):
        if 'zero' in num:
             num = num.replace("zero", "0")
        if 'one' in num:
             num = num.replace("one", "1")
        if 'two' in num:
             num = num.replace("two", "2")
        if 'three' in num:
             num = num.replace("three", "3")
        if 'four' in num:
             num = num.replace("four", "4")
        if 'five' in num:
             num = num.replace("five", "5")
        if 'six' in num:
             num = num.replace("six", "6")
        if 'seven' in num:
             num = num.replace("seven", "7")
        if 'eight' in num:
             num = num.replace("eight", "8")
        if 'nine' in num:
             num = num.replace("nine", "9")
        return num


def num_to_string(num):
        if '0' in num:
            num = num.replace("0", "zero")
        if '1' in num:
            num = num.replace("1", "one")
        if '2' in num:
            num = num.replace("2", "two")
        if '3' in num:
            num = num.replace("3", "three")
        if '4' in num:
            num = num.replace("4", "four")
        if '5' in num:
            num = num.replace("5", "five")
        if '6' in num:
            num = num.replace("6", "six")
        if '7' in num:
            num = num.replace("7", "seven")
        if '8' in num:
            num = num.replace("8", "eight")
        if '9' in num:
            num = num.replace("9", "nine")

        return num

def Gcd(x, y):
      if y == 0:
        return x
      else:
        return Gcd(y, x % y)

if __name__ == "__main__":
    get_values()
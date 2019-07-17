class Calculator():
    def add(n1, n2):  # Functions have a definition
        return n1+n2  # And elsewhere in the code an invocation

    def subtract(n1, n2):
        return n1-n2

    def multiply(n1, n2):
        return n1*n2

    def divide(n1, n2):
        return n1/n2

    value1 = int(input('Give me a number: '))
    value2 = int(input('Give me another number: '))
    print(add(value1, value2))


# def area_of_circle(radius):
#     pi = 3.143  # Pi is a local variable
#     return pi * radius * radius
#
# result = area_of_circle(int(input('Please enter your circle radius')))
# print(result)

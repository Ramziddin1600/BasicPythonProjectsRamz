
try:
    number = float(input("Enter a number: "))
except ValueError:
    print(f"The input is not valid. Please enter a valid number.")


converting_from = input("Enter the degree measure you are converting from(C/F/K): ").upper()
converting_to = input("Enter the degree measure you are converting to(C/F/K): ").upper()
def fahrenheit_to_celcius(fahrenheit):
    result = (fahrenheit - 32) * 5/9
    return result

def celcius_to_fahrenheit(celcius):
    result = celcius * 9 / 5 + 32
    return result

def kelvin_to_celcius(kelvin):
    result = kelvin - 273.15
    return result

def celcius_to_kelvin(celcius):
    result = celcius + 273.15
    return result

def fahrenheit_to_kelvin(fahrenheit):
    result = (fahrenheit - 32) * 5 / 9 + 273.15
    return result

def kelvin_to_fahrenheit(kelvin):
    result = (kelvin - 273.15) * 9 / 5 + 32
    return result

if converting_from == 'C' and converting_to == 'F':
    print(f"The result is {celcius_to_fahrenheit(number):.2f} degrees Fahrenheit.")
elif converting_from == 'C' and converting_to == 'K':
    print(f"The result is {celcius_to_kelvin(number):.2f} degrees Kelvin.")
elif converting_from == 'F' and converting_to == 'K':
    print(f"The result is {fahrenheit_to_kelvin(number):.2f} degrees Kelvin.")
elif converting_from == 'F' and converting_to == 'C':
    print(f"The result is {fahrenheit_to_celcius(number):.2f} degrees Celcius.")
elif converting_from == 'K' and converting_to == 'F':
    print(f"The result is {kelvin_to_fahrenheit(number):.2f} degrees Fahrenheit.")
elif converting_from == 'K' and converting_to == 'C':
    print(f"The result is {kelvin_to_celcius(number):.2f} degrees Celcius."



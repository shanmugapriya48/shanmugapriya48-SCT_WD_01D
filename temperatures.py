def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    print("Temperature Conversion Program")
    print("Choose the input temperature scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    choice = int(input("Enter choice (1/2/3): "))
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to:")
        print(f"{celsius_to_fahrenheit(celsius)}°F")
        print(f"{celsius_to_kelvin(celsius)}K")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to:")
        print(f"{fahrenheit_to_celsius(fahrenheit)}°C")
        print(f"{fahrenheit_to_kelvin(fahrenheit)}K")
    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin}K is equal to:")
        print(f"{kelvin_to_celsius(kelvin)}°C")
        print(f"{kelvin_to_fahrenheit(kelvin)}°F")
    else:
        print("Invalid choice. Please try again.")
convert_temperature()

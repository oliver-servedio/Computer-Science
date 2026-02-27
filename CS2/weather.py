def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")

main()
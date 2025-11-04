def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def main():
    print("=== Temperature Converter CLI ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = input("Choose conversion (1-4): ")

    try:
        value = float(input("Enter temperature value: "))
        if choice == '1':
            print(f"Result: {celsius_to_fahrenheit(value):.2f} °F")
        elif choice == '2':
            print(f"Result: {fahrenheit_to_celsius(value):.2f} °C")
        elif choice == '3':
            print(f"Result: {celsius_to_kelvin(value):.2f} K")
        elif choice == '4':
            print(f"Result: {kelvin_to_celsius(value):.2f} °C")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
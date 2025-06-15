# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0  # Fixed typo in variable name (was FACTOR)

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    while True:
        try:
            temp_input = input("Enter the temperature to convert (or 'q' to quit): ")
            if temp_input.lower() == 'q':
                print("Goodbye!")
                break
                
            temp = float(temp_input)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
            
            if unit == 'F':
                converted = convert_to_celsius(temp)
                print(f"\n{temp}°F is {converted:.2f}°C\n")  # Formatting to 2 decimal places
            elif unit == 'C':
                converted = convert_to_fahrenheit(temp)
                print(f"\n{temp}°C is {converted:.2f}°F\n")  # Formatting to 2 decimal places
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue
                
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

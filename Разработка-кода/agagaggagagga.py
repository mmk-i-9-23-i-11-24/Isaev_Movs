def convert_length(value, unit_from, unit_to):
    conversion_factors = {
        'mile': 1609,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001
    }
    value_in_meters = value * conversion_factors[unit_from]
    converted_value = value_in_meters / conversion_factors[unit_to]
    return converted_value

input_string = input("Введите данные (например, '15.5 mile in km'): ")
value, unit_from, _, unit_to = input_string.split()
value = float(value)
result = convert_length(value, unit_from, unit_to)
print(f"{result:.2e}")
height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")
# BMI = weight (kg) / height^2 (m^2)

bmi = float(weight) / float(height) ** 2
print(int(bmi))

# Both the height input and weight input need to be converted to floats, because the input() function returns a string.
# The height input is also raised to the power of 2, using the exponent operator "**".
# The result is then converted to an integer, using the int() function.
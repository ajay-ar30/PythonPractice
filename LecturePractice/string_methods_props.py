string_value = "same"

# string_value[0] = 'g' invalid because string character values are immutable(cant be changed)

#string concatenation:

new_string_value = string_value[1:]

concat_string = 'g'+new_string_value
print("Concatenated string value is",concat_string)

x = "Concat practice"
x = x + " in VS code"

print("Concatenated string is", x)

#String multiplication:

y = 'abc'
y = y * 5
print("Value of y multiplied 5 times is",y)

# String built-in methods and attributes:
# use . after variable name for the list

z = "Hello World"

z = z.upper()
print('Uppercase value of z is', z)

# Split strings by whitespace or character (creates list of strings) using split() method

z = z.split()
print("New value of z using split method is", z)

var_name = "Mississipi is a river"
var_name = var_name.split('i')
print("Split string value of var_name on i character is", var_name)


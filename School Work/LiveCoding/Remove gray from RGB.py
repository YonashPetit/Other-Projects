red = int(input())
green = int(input())
blue = int(input())

min_value = red

if green < min_value:
    min_value = green
if blue < min_value:
    min_value = blue

print(red - min_value, green - min_value, blue - min_value)
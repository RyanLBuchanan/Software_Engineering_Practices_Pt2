from shirt import Shirt

shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve', 10)

print(shirt_one.price)
print(shirt_two.color)

shirt_three.change_price(45)
print(shirt_three.price)
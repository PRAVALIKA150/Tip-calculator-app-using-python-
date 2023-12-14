 Tip Calculator App
food_amount = float(input('Enter food amount $: '))
tip_percentage = float(input('Enter your tip percentage %: ')) / 100
tip_amount = food_amount * tip_percentage

total = food_amount + tip_amount
total = food_amount + tip_amount
print('\n\n\n')
print('--------------------------------')
print(f'🥘 Food Amount: ${food_amount}')
print(f'⚖️ Tip Amount: ${tip_amount}')
print('\n')
print(f'💰 Total Amount: ${total}')
print('--------------------------------')

# using functions
def calculateFoodTotal(food: float, tip_percentage: int) -> float:
  tip = food * (tip_percentage / 100)
  total = food + tip
  print('\n\n\n')
  print('--------------------------------')
  print(f'🥘 Food Amount: ${food}')
  print(f'⚖️ Tip Amount: ${tip}')
  print('\n')
  print(f'💰 Total Amount: ${total}')
  print('--------------------------------')
  return total

total=calculateFoodTotal(100, 10)
calculateFoodTotal(food=100, tip_percentage=20)


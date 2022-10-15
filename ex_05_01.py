largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        int(num)
    except:
        print('Invalid input')
        continue

    if largest is None or int(num)  > largest:
        largest = int(num)
    elif smallest is None or int(num) < smallest:
        smallest = int(num)
  
print('Maximum is', largest)
print('Minimum is', smallest)
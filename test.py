command = ""
started = False
while command.upper != "QUIT":
    command = input("").upper()
    if command == "START":
        if started:
            print('Car already started')
        print("Car started")
    elif command == "STOP":
        if not started:
            print('Car already stopped')
        print("Car stopped")
    elif command == "QUIT":
        break
    else:
        ("I dont understand your command")

prices = [10,20,30]
total_price = 0

for price in prices:
    total_price = total_price + price
    print(total_price)
def show_balance():
    print(f"Your Balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to deposit: "))
    if amount <= 0:
        print("Money konodin negative hoi na bokasuda")
        return 0
    else:
        return amount


def withdraw():
    amount = float(input("Enter an amount to withdraw: "))
    if amount <= 0:
        print("Ore sona sunno taka ba tar kom taka tule kar bal chirba")
        return 0
    elif amount > balance:
        print("banchod tor bank a ato taka ache???")
        return 0
    else:
        return amount


balance = 0
is_running = True
while is_running:
    print("Welcome to Banking System")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance = balance + deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice")
print("Thank you for using Banking System")

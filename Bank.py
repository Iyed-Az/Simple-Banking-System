##SIMPLE BANKING SYSTEM##

def show_balance(balance):
    print(f"Your balance is  {balance: .2f} DZD") 
def deposit():
    amount = float(input("Enter an amount to be deposited:"))

    if amount<0:
        print("Enter a valid amount please")
        return 0
    else :
        return amount


def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn please:"))

    if amount>balance:
        print("Amount is bigger than balance")
        return 0
    elif amount<0:
        print("Amount must be greater than 0")
        return 0   

    else:
        return amount    

def main():
    balance=0
    is_running=True

    while is_running:
        print("$$$$$$$$$$$$$$$$$$")
        print("WELCOME TO THE BANK")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("$$$$$$$$$$$$$$$$$$")

        choice=input("Enter your choice (1-4):")

        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance += deposit()
        elif choice=='3':
            balance-=withdraw(balance)
        elif choice=='4':
            is_running=False 

        else:
            print("Enter a right choice please")          

    print("THANK YOU ! Have a nice day :)")        


if __name__  == '__main__' :
    main()
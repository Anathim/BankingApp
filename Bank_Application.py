import os

bankFile = 'Bank Data.txt'
transFile = 'Transaction Log.txt'

def displayBalance():
    with open(bankFile, 'r') as f:
        balance = float(f.readline())
        print('Your current balance is: {:.2f}'.format(balance))

def deposit(amount):
    with open(bankFile, 'r+') as f:
        balance = float(f.readline())
        f.seek(0)
        f.write(str(balance + amount) + '\n')
        f.truncate()

    with open(transFile, 'a') as f:
        f.write('Deposit: +{:.2f}\n'.format(amount))

def withdraw(amount):
    with open(bankFile, 'r+') as f:
        balance = float(f.readline())
        if balance < amount:
            print('Insufficient funds')
            return
        f.seek(0)
        f.write(str(balance - amount) + '\n')
        f.truncate()

    with open(transFile, 'a') as f:
        f.write('Withdrawal: -{:.2f}\n'.format(amount))

def isValidInput(prompt, validResponses):
    response = input(prompt)
    while response not in validResponses:
        print('You provided an invalid input')
        response = input(prompt)
    return response

def isValidAmount(prompt):
    amount = input(prompt)
    while not amount.isdigit():
        print('You provided an invalid input')
        amount = input(prompt)
    return float(amount)

def main():
    if not os.path.exists(bankFile):
        with open(bankFile, 'w') as f:
            f.write('0\n')

    displayBalance()

    makeTransaction = isValidInput('Would you like to make a transaction? (Yes/No): ')

    while makeTransaction == 'Yes':
        depositOrWithdraw = isValidInput('Would you like to make a deposit or withdrawal? (Deposit/Withdrawal): ')

        if depositOrWithdraw == 'Deposit':
            amount = isValidAmount('How much would you like to deposit?: ')
            deposit(amount)
        else:
            amount = isValidAmount('How much would you like to withdraw?: ')
            withdraw(amount)

        displayBalance()
        makeTransaction = isValidInput('Would you like to make another transaction? (Yes/No): ')

    print('Thank you for using our bank application!')

if __name__ == '__main__':
    main()

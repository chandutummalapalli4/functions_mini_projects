                    ###---------------MINI PROJECT 3---------------###

# 1. display_bank_header()
# 2. customer_profile()
# 3. deposit_money()
# 4. withdraw_money()
# 5. account_status()
# 6. bank_summary()
                       ###---------------CODE-------------------###
###----------- ABC BANK MANAGEMENT SYSTEM -----------###

def display_bank_header():
    print("==============================")
    print(" ABC BANK MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Customer Profile")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Account Status")
    print("==============================")
    print()


def customer_profile(name, age, city, account_number, account_type, balance):
    print("----- CUSTOMER PROFILE -----")
    print("Account Holder Name :", name)
    print("Age                 :", age)
    print("Bank Location       :", city)
    print("Account Number      :", account_number)
    print("Account Type        :", account_type)
    print("Account Balance     :", balance)
    print()


def deposit_money(balance, deposit_amount):
    updated_balance = balance + deposit_amount

    print("----- DEPOSIT -----")
    print("Current Balance :", balance)
    print("Deposit Amount  :", deposit_amount)
    print("Updated Balance :", updated_balance)
    print()


def withdraw_money(balance, withdraw_amount):
    updated_balance = balance - withdraw_amount

    print("----- WITHDRAW -----")
    print("Current Balance :", balance)
    print("Withdraw Amount :", withdraw_amount)
    print("Updated Balance :", updated_balance)
    print()


def account_status(balance):
    print("----- ACCOUNT STATUS -----")

    if balance >= 5000:
        print("Status : ACTIVE")
    elif balance > 0 and balance < 5000:
        print("Status : LOW BALANCE")
    else:
        print("Status : ZERO BALANCE")

    print()


# Master Function
def bank_summary(name, age, city, account_number, account_type,
                 balance, deposit_amount, withdraw_amount):

    customer_profile(name, age, city, account_number, account_type, balance)

    deposit_money(balance, deposit_amount)

    withdraw_money(balance + deposit_amount, withdraw_amount)

    account_status(balance + deposit_amount - withdraw_amount)


# Main Program
display_bank_header()

bank_summary(
    "Chandu", 21, "Nagullanka",
    123456, "Current",
    1200000, 5000, 2500
)

bank_summary(
    "Raju", 25, "Amalapuram",
    22256756, "Savings",
    256000, 10000, 5000
)

bank_summary(
    "Ramu", 65, "Vizag",
    78656756, "Savings",
    575000, 15000, 25000
)

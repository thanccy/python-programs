
import re

# Function to validate email address
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        print("Valid email address")
    else:
        print("Invalid email address")


# Function to validate phone number
def validate_phone(phone):
    pattern = r'^[6-9][0-9]{9}$'

    if re.match(pattern, phone):
        print("Valid phone number")
    else:
        print("Invalid phone number")


# Function to extract transaction IDs from logs
def extract_transaction_ids(logs):
    pattern = r'TXN[0-9]{6}'

    transaction_ids = re.findall(pattern, logs)

    print("Transaction IDs found:")
    for txn in transaction_ids:
        print(txn)


# Main program
print("===== Online Registration Validation =====")

email = input("Enter email address: ")
validate_email(email)

phone = input("Enter phone number: ")
validate_phone(phone)

logs = input("Enter transaction logs: ")
extract_transaction_ids(logs)

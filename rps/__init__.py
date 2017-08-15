import hmac
import hashlib
import secrets

options = ["Rock", "Paper", "Scissors"]
amount_of_options = len(options)
print(options)

key = secrets.token_hex(16)

computer_val_index = secrets.randbelow(amount_of_options)
computer_val = options[computer_val_index]

key_bytes = str(key).encode('utf-8')
data_bytes = bytes(computer_val, 'utf-8')

computer_val_hash = hmac.new(
    key_bytes,
    data_bytes,
    hashlib.sha256
).hexdigest()

print("Computer's choice is: " + computer_val_hash)
user_val = input("Print your choice there: ")
user_val_index = options.index(user_val)

result = (amount_of_options + computer_val_index - user_val_index) % amount_of_options
if result == 0:
    print("Tie!")
elif result % 2 == 1:
    print("Computer wins!")
elif result % 2 == 0:
    print("You win!")

print("Computer's choice was: " + computer_val)
print('Key: ' + str(key))
input('Press close to exit')
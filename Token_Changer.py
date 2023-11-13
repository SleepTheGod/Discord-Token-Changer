import requests

# Made By Taylor Christan Newsome And Arya Ebrahami
def change_password(token, new_password):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    payload = {
        'password': new_password
    }
    response = requests.patch('https://discord.com/api/v10/users/@me', headers=headers, json=payload)
    if response.status_code == 200:
        print("Password changed successfully!")
    else:
        print("Failed to change password.")

# Prompt the user for their Discord token and new password
token = input("Enter your Discord token: ")
new_password = input("Enter your new password: ")

# Call the function to change the password
change_password(token, new_password)

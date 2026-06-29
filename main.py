import requests
import time 
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("API_KEY")


def get_exchange_rate():
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['conversion_rate']
    if rate is None:
        print("Error: Unable to retrieve exchange rate.")
        return
    converted_amount = amount * rate
    try :
        with open("exchange_rate.txt", "a") as file:
            file.write(f"\n{amount} {base_currency} = {converted_amount} {target_currency} at rate {rate}\n")
    except FileNotFoundError:
        print("Error: Unable to write to file.")
        return
    print(f"\n{amount} {base_currency} is equal to {converted_amount} {target_currency} at the current exchange rate of {rate}.")

def view_history():
    try :
        with open("exchange_rate.txt" , "r") as file :
            history = file.read()
            print("history :")
            print(history)
    except FileNotFoundError :
        print("File Not Found")
        return
    
def clear_history():
    try :
        with open("exchange_rate.txt" , "w") as file :
            clear = file.write("")
            print("history Cleared")
    except FileNotFoundError :
        print("File Not Found")
        return
    
while True :
    print("\n===== CURRENCY EXCHANGE CENTRE =====\n")
    print("1. Exchange Currencies ")
    print("2. view history")
    print("3. clear history")
    print("4. exit")
    choice = input("Enter your choice (1,2,3,4) : ")

    if choice == "1" :
        get_exchange_rate()
    elif choice == "2" :
        view_history()
    elif choice == "3" :
        clear_history()
    elif choice == "4" :
        print("Exiting the Application.....")
        time.sleep(1.75)
        print("\nThank you, Have a great day")
        break
    


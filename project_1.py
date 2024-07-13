"""
project_1.py: first project for Engeto Online Python Academy
author: Radka Štorchová
email: r.storchova@gmail.com
discord: radkastorchova

"""
import task_template #here are saved the texts for analysis
from analyze_text import analyze_text # importing my defined function to analyze text
from plot_word_freq import plot_word_freq
# importing my defined function to plot the freq of word based on the length of the word

#Defining how many texts are in the template and therefore which numbers can be chosen later
possible_numbers = list(range(1, (len(task_template.TEXTS) + 1)))

#Registered users (keys represent names, passwords are in the values)
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
#User login
user_name = str(input("User name:"))
password = str(input("Password:"))

#In case of unexisting user name:
if user_name not in registered_users:
    print("unregistered user, terminating the program...")
# succesful login:
elif registered_users[user_name] == password:
    print(f"Welcome to the app,{user_name}")
    text_number = int(input(f"Enter a number btw {possible_numbers[0]} and {possible_numbers[-1]}:"))
    if text_number in possible_numbers:
        chosen_text = task_template.TEXTS[text_number-1]
        analyze_text(chosen_text)
        plot_word_freq(chosen_text)
    else:
        print("Your input is not in the possible numbers, terminating the program...")

#In case of wrong combination of user name and password
else:
    print("wrong password, terminating the program...")

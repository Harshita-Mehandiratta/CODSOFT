#!/usr/bin/env python
# coding: utf-8

# In[6]:


#task 1 to do list
import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=20)
        
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()
        
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack()
        
        edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        edit_button.pack()
        
        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack()
        
        self.load_tasks()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            edited_task = self.task_entry.get()
            if edited_task:
                self.tasks[selected_task_index] = edited_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, edited_task)
                self.task_entry.delete(0, tk.END)
                self.save_tasks()
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
            self.save_tasks()
    
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task = line.strip()
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


# In[5]:


#task 2 calculator
import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to calculate the square root of a number
def square_root(x):
    if x < 0:
        return "Invalid input. Cannot calculate the square root of a negative number."
    return math.sqrt(x)

# Function to calculate the exponentiation of a number
def exponentiate(x, y):
    return x ** y

# Function to calculate the modulus of two numbers
def modulus(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x % y

# Main calculator function
def calculator():
    print("Welcome to the Calculator!")

    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'sqrt' for square root")
        print("Enter 'exponentiate' for exponentiation")
        print("Enter 'modulus' for modulus")
        print("Enter 'quit' to end the program")

        user_input = input(": ")

        if user_input == "quit":
            print("Thank you for using the calculator. Goodbye!")
            break
        elif user_input in ("add", "subtract", "multiply", "divide", "sqrt", "exponentiate", "modulus"):
            if user_input == "sqrt" or user_input == "exponentiate" or user_input == "modulus":
                num = float(input("Enter a number: "))
                if user_input == "sqrt":
                    result = square_root(num)
                elif user_input == "exponentiate":
                    exp = float(input("Enter an exponent: "))
                    result = exponentiate(num, exp)
                elif user_input == "modulus":
                    num2 = float(input("Enter another number: "))
                    result = modulus(num, num2)
            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if user_input == "add":
                    result = add(num1, num2)
                elif user_input == "subtract":
                    result = subtract(num1, num2)
                elif user_input == "multiply":
                    result = multiply(num1, num2)
                elif user_input == "divide":
                    result = divide(num1, num2)

            print("Result:", result)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator(


# In[6]:


#task 3 password generator
import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create an empty list to store password characters
password_list = []

# Generate random letters for the password
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Generate random symbols for the password
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Generate random numbers for the password
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password characters to make it random
random.shuffle(password_list)

# Convert the list of characters into a string
password = ''.join(password_list)

# Print the generated password
print(f"Your generated password is: {password}")


# In[2]:


#task 4 rock paper scissors game
import random

# Define the choices for the game
choices = ["rock", "paper", "scissors"]

# Function to get the user's choice
def get_user_choice():
    while True:
        print("Choose one:")
        for i, choice in enumerate(choices):
            print(f"{i}. {choice}")
        
        try:
            user_choice = int(input("Enter the number of your choice: "))
            if user_choice >= 0 and user_choice < len(choices):
                return user_choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get the computer's choice
def get_computer_choice():
    return random.randint(0, 2)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        return "Congratulations! You win!"
    else:
        return "Sorry, you lose."

# Main game loop
while True:
    print("Welcome to Rock-Paper-Scissors!")
    
    user_choice = get_user_choice()
    print(f"You chose: {choices[user_choice]}")

    computer_choice = get_computer_choice()
    print(f"Computer chose: {choices[computer_choice]}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing! Goodbye!")
        break


# In[4]:


import openpyxl

# Define the contacts dictionary to store contact data
contacts = {}

# Function to load user data from an Excel sheet into a dictionary
def load_user_data():
    contact_book = {}
    try:
        workbook = openpyxl.load_workbook(r'codsoft contact book.xlsx')
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=4, values_only=True):
            name, phone, email, address = row
            contact_book[name] = {"phone": phone, "email": email, "address": address}
        workbook.close()
    except FileNotFoundError:
        print("Contact book file not found.")
    return contact_book

# Function to authenticate a user
def authenticate_user(username, password, user_data):
    if username in user_data and user_data[username] == password:
        return True
    else:
        return False

# Function to add a new contact
def add_contact(name, phone, email, address):
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("Your contact book is empty.")
    else:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("")

# Function to search for a contact by name or phone number
def search_contact(query):
    results = []
    for name, info in contacts.items():
        if query in name or query in info['phone']:
            results.append((name, info))
    
    if results:
        print("\nSearch Results:")
        for name, info in results:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("")
    else:
        print("No matching contacts found.")

# Function to update a contact's information
def update_contact(name, phone, email, address):
    if name in contacts:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found. Update failed.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found. Deletion failed.")

# Main application loop
while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        name = input("Enter the contact's name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")
        address = input("Enter the address: ")
        add_contact(name, phone, email, address)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        query = input("Enter a name or phone number to search: ")
        search_contact(query)
    elif choice == "4":
        name = input("Enter the name of the contact to update: ")
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        address = input("Enter the new address: ")
        update_contact(name, phone, email, address)
    elif choice == "5":
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)
    elif choice == "6":
        print("Thank you for using the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


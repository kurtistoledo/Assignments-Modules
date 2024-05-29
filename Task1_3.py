# Lesson 1: Overview of Modules In Python
# 3. Mastering Python Modules and Aliases

def reverse_string(s):
    """Function to reverse a string."""
    return s[::-1]

def capitalize_string(s):
    """Function to capitalize a string."""
    return s.capitalize()

import Task1_3 as tu

def main():
    while True:
        print("""
        Text Utilities
        1. Reverse String
        2. Capitalize String
        3. Quit
        """)
        choice = input("Select an option: ")
        
        if choice == '1':
            text = input("Enter a string to reverse: ")
            print("Reversed string:", tu.reverse_string(text))
        
        elif choice == '2':
            text = input("Enter a string to capitalize: ")
            print("Capitalized string:", tu.capitalize_string(text))
        
        elif choice == '3':
            print("Exiting Text Utilities. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

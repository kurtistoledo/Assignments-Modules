# Lesson 1: Overview of Modules In Python
# 1. Python Modules and Data Handling Assignment

def mood_response(mood):
    mood_responses = {
        'happy': "That's great to hear! Keep smiling!",
        'sad': "I'm sorry you're feeling sad. Hope things get better soon.",
        'excited': "Awesome! It's wonderful to feel excited!",
        'angry': "Take a deep breath. It's okay to feel angry sometimes.",
        'anxious': "Remember to take some time to relax. You're doing great.",
        'bored': "Maybe try a new hobby or read a book to pass the time.",
        'tired': "Make sure to get some rest and take care of yourself.",
        'confused': "It's okay to feel confused. Take things one step at a time."
    }

    return mood_responses.get(mood.lower(), "I'm not sure how to respond to that mood, but I hope you have a great day!")

import Task1_1

def main():
    mood = input("How are you feeling today? ")
    response = Task1_1.mood_response(mood)
    print(response)

if __name__ == "__main__":
    main()

# Second/Minute/Hour needed for a word Project
import time

while True:
    t0 = time.time()     # Starting time
    test_string = input("Enter sentence: ")       # Input sentence
    t1 = time.time()     # Finishing time

    # Total time taken to input sentence
    time_taken = t1 - t0
    # Counting words using split() function
    word_count = len(test_string.split())

    # Measuring words per second
    if word_count > 0:
        print("Total Time:", time_taken)  # Printing total time
        wps = time_taken / word_count
        print("Seconds needed for a word:", wps)  # Printing second needed for a word

    # Measuring words per minute if time taken more than 1 minute
    if time_taken >= 60:
        wpm = time_taken / (word_count * 60)
        print("Minutes needed for a word:", wpm)  # Printing minute needed for a word

    # Measuring words per minute if time taken more than 1 hour
    if time_taken >= 3600:
        hpm = time_taken / (word_count * 3600)
        print("Hours needed for a word:", hpm)    # Printing hour needed for a word

    # Again speed check
    Again = input("Do you want to check again?: ")  # Inputting yes or no
    Again = Again.upper()
    if Again == "NO":
        break

    while Again != "YES":
        print("Wrong Input! Please type YES or NO.")
        Again = input("Do you want to check again?: ")
        Again = Again.upper()
        if Again == "YES":
            break

        elif Again == "NO":
            break
    if Again == "NO":
        break

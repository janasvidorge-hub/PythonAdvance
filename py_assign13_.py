
import threading
import time

# Task 1: Print numbers
def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

# Task 2: Print alphabets
def print_alphabets():
    for ch in 'ABCDE':
        print("Alphabet:", ch)
        time.sleep(1)

# Task 3: Display messages
def print_messages():
    messages = ["Hello", "Welcome", "Python", "Threads", "Finished"]
    for msg in messages:
        print("Message:", msg)
        time.sleep(1)

# Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)
t3 = threading.Thread(target=print_messages)

# Starting threads
t1.start()
t2.start()
t3.start()

# Waiting for all threads to finish
t1.join()
t2.join()
t3.join()

print("All tasks completed successfully.")

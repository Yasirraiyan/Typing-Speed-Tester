import random
import time

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "I enjoy learning new things every day.",
    "Artificial Intelligence is transforming the world.",
    "Let's build something incredible today!",
    "Reading books can be very enlightening.",
    "Consistency is the key to success.",
    "Coding can be both challenging and rewarding.",
    "The sun sets beautifully over the horizon.",
    "A healthy diet is essential for a healthy life."
]

# Choose a random sentence
choosingsentence = random.choice(sentences)
print("Selected sentence is:", choosingsentence)

# Start the timer before user starts typing

def CheckValidityofinputsentence(choosingsentence):
    if(choosingsentence in sentences):
        print("The sentence is valid:")
        return 1;
    else:
        print("The sentence is invalid")
        return 0
starttime = time.time()

# Get user input
writingsentence = input("Type the sentence here: ")

# End the timer after user finishes typing
endtime = time.time()

# Calculate the time taken
timetakentotype = endtime - starttime
print("The time taken by user to type:", timetakentotype, "seconds")

# Count words in the chosen sentence
words = len(choosingsentence.split())

# Calculate WPM (Words Per Minute)
wpm = (words / timetakentotype) * 60
print("The typing speed is:", wpm, "WPM")

# Determine the type of writer
def typeofwriter(wpm):
    if wpm < 20:
        return "Beginner"
    elif 20 <= wpm <= 40:
        return "Intermediate"
    elif 40 <= wpm <= 60:
        return "Proficient"
    elif 60 <= wpm <= 80:
        return "Advanced"
    elif 80 <= wpm <= 100:
        return "Expert"
    else:
        return "Master"

writer_type = typeofwriter(wpm)
print(f"The writer type is: {writer_type}")

    
    
    

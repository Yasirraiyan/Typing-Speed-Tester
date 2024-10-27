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

    

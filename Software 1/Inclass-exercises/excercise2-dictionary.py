
def student_scores():
    scores = {"Joshua": 9,
              "Princess": 8,
              "Clary": 7,
              "Tara": 6}

    name, score = input("Enter name with new score: "), int(input("Enter new score: "))

    scores["Maria"] = 8
    if name in scores:
        scores[name] = score
        print(f"{name}'s score is now {scores[name]}.")
    else:
        print("Sorry we don't have this person's phone number.")

    return scores

def topstudent(final_scores):
    highest = max(final_scores, key=final_scores.get) #copares values and not the keys
    return highest

final_scores = student_scores()
print(final_scores)
print("The person with the highest score is" , topstudent(final_scores))

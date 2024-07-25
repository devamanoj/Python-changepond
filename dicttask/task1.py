# def main():
   
#     grading_scale = {
#         "A": (90, 100),
#         "B": (80, 89),
#         "C": (70, 79),
#         "D": (60, 69),
#         "E": (50, 59),
#         "F": (0, 49)
#     }

    
#     score = int(input("Enter the score: "))

    
#     if score >= 0 and score <= 100:
#         if score >= grading_scale['A'][0] and score <= grading_scale['A'][1]:
#             print(f"The grade for the score {score} is: A")
#         elif score >= grading_scale['B'][0] and score <= grading_scale['B'][1]:
#             print(f"The grade for the score {score} is: B")
#         elif score >= grading_scale['C'][0] and score <= grading_scale['C'][1]:
#             print(f"The grade for the score {score} is: C")
#         elif score >= grading_scale['D'][0] and score <= grading_scale['D'][1]:
#             print(f"The grade for the score {score} is: D")
#         elif score >= grading_scale['E'][0] and score <= grading_scale['E'][1]:
#             print(f"The grade for the score {score} is: E")
#         elif score >= grading_scale['F'][0] and score <= grading_scale['F'][1]:
#             print(f"The grade for the score {score} is: F")
#     else:
#         print("Invalid ")

# if __name__ == "__main__":
#     main()


def main():
    # Define the grading scale using a dictionary
    grading_scale = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'E': 50,
        'F': 0
    }

    # Get the score from the user
    score = int(input("Enter the score: "))

    # Determine the grade based on the score
    if score >= 0 and score <= 100:
        if score >= grading_scale['A']:
            print(f"The grade for the score {score} is: A")
        elif score >= grading_scale['B']:
            print(f"The grade for the score {score} is: B")
        elif score >= grading_scale['C']:
            print(f"The grade for the score {score} is: C")
        elif score >= grading_scale['D']:
            print(f"The grade for the score {score} is: D")
        elif score >= grading_scale['E']:
            print(f"The grade for the score {score} is: E")
        elif score >= grading_scale['F']:
            print(f"The grade for the score {score} is: F")
    else:
        print("Invalid score")

if __name__ == "__main__":
    main()

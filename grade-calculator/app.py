print("GRADE CALCULATOR")

test_scores = []
while True:
    score = input("Enter test score (or 'done): ")
    if score == 'done':
        break
    test_scores.append(float(score))

    average_score = sum(test_scores) / len(test_scores) if test_scores else 0
    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"Average Score: {average_score:.2f}")
    print(f"Final Grade: {grade}")

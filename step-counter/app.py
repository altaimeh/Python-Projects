print("🚶‍♂️ STEP COUNTER 🚶‍♂️")

goal = input("Enter your daily step goal: ")
steps = input("Enter the number of steps you walked today: ")


goalCounter = int(goal)
stepsCounter = int(steps)

if stepsCounter >= goalCounter:
    print("🎉 Congratulations! You've reached your step goal for today!")
else:
    print(f"Keep going! You need {goalCounter - stepsCounter} more steps to reach your goal.")

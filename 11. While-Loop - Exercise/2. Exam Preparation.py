maxPoorGrades = int(input())

score = 0
problems = 0
lastProblem = ""
poorGrades = 0

while True:
    problem = input()
    if problem == "Enough":
        print(f"Average score: {score / problems:.2f}")
        print(f"Number of problems: {problems}")
        print(f"Last problem: {lastProblem}")
        break
    else:
        lastProblem = problem
        grade = int(input())
        problems += 1
        score += grade
        if grade <= 4:
            poorGrades += 1
            if poorGrades >= maxPoorGrades:
                print(f"You need a break, {poorGrades} poor grades.")
                break
# Student Score Analyzer.
# This program analyzes student marks using Python and NumPy.
# It calculates grades, statistics, and performs array operations.

import numpy as np


# Part 1 - Python Basics

# Take number of students as input
n = int(input("Enter the number of students: "))

marks = []

# Take marks as input
for i in range(n):
    score = int(input(f"Enter marks of Student {i+1}: "))
    marks.append(score)

# Function to assign grades
def grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

print("\nStudent Grades:")
for i, score in enumerate(marks, start=1):
    print(f"Student {i}: {score} -> {grade(score)}")


# Part 2 - NumPy Analysis

scores = np.array(marks)

print("\n----- Statistical Analysis -----")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Maximum:", np.max(scores))
print("Minimum:", np.min(scores))
print("Standard Deviation:", np.std(scores))

average = np.mean(scores)

above_average = scores[scores > average]
print("Students scoring above class average:", len(above_average))

print("A Grade Scores:")
print(scores[scores >= 85])

# Part 3 - Bonus

choice = input("\nDo you want to add 5 more students? (yes/no): ").lower()

if choice == "yes":
    for i in range(5):
        score = int(input(f"Enter marks of New Student {i+1}: "))
        marks.append(score)

    scores = np.array(marks)

    print("\n----- Updated Statistical Analysis -----")
    print("Mean:", np.mean(scores))
    print("Median:", np.median(scores))
    print("Maximum:", np.max(scores))
    print("Minimum:", np.min(scores))
    print("Standard Deviation:", np.std(scores))

    grade_count = {"A": 0, "B": 0, "C": 0, "F": 0}

    for score in scores:
        grade_count[grade(score)] += 1

    print("\nGrade Counts:")
    for g, count in grade_count.items():
        print(f"{g}: {count}")

    most_common = max(grade_count, key=grade_count.get)
    print("Most Common Grade:", most_common)

    
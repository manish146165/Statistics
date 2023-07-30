import statistics

def get_student_scores():
    scores = []
    for i in range(10):
        while True:
            try:
                score = float(input(f"Enter the score of student {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return scores

def calculate_mean(scores):
    return statistics.mean(scores)

def calculate_median(scores):
    return statistics.median(scores)

def calculate_mode(scores):
    return statistics.mode(scores)

def calculate_standard_deviation(scores):
    return statistics.stdev(scores)

def main():
    print("Enter the scores of 5 students:")
    student_scores = get_student_scores()

    mean = calculate_mean(student_scores)
    median = calculate_median(student_scores)
    mode = calculate_mode(student_scores)
    standard_deviation = calculate_standard_deviation(student_scores)

    print("\nResults:")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {standard_deviation}")

if __name__ == "__main__":
    main()

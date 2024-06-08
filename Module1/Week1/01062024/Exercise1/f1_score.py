
# This function serves as the entry point of the program
def main():
    # True positives (correctly classified positive cases)
    tp = 123
    # False positives (incorrectly classified positive cases)
    fp = 'a'  # This should be an integer, fix it before running
    # False negatives (missed positive cases)
    fn = 123

    # Call the evaluation function with the calculated values
    evaluate_classification(tp=tp, fp=fp, fn=fn)


# This function evaluates the classification performance based on provided inputs
def evaluate_classification( tp, fp, fn ):
    # Ensure true positives is an integer
    if type(tp) is not int:
        print("tp must be an integer (number of true positives)")
        return

    # Ensure false positives is an integer
    if type(fp) is not int:
        print("fp must be an integer (number of false positives)")
        return

    # Ensure false negatives is an integer
    if type(fn) is not int:
        print("fn must be an integer (number of false negatives)")
        return

    # Ensure all inputs are greater than zero to avoid division by zero
    if tp == 0 or fp == 0 or fn == 0:
        print("tp, fp, and fn must all be greater than zero")
        return

    # Calculate precision using a separate function
    precision = calculate_precision(tp, fp)

    # Calculate recall using a separate function
    recall = calculate_recall(tp, fn)

    # Print the precision value
    print(f"Precision is {precision}")

    # Print the recall value
    print(f"Recall is {recall}")

    # Calculate F1-score using a separate function and print the result
    print(f"F1-score is {calculate_f1_score(precision, recall)}")

    return


# This function calculates precision based on true and false positives
def calculate_precision( tp, fp ):
    # Precision = tp / (tp + fp)
    return tp / (tp + fp)


# This function calculates recall based on true positives and false negatives
def calculate_recall( tp, fn ):
    # Recall = tp / (tp + fn)
    return tp / (tp + fn)


# This function calculates F1-score based on precision and recall
def calculate_f1_score( precision, recall ):
    # F1-score = 2 * ((precision * recall) / (precision + recall))
    return 2 * ((precision * recall) / (precision + recall))


# This block ensures the code within only runs when the script is executed directly
if __name__ == '__main__':
    main()
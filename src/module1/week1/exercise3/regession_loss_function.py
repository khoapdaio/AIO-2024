import random
import math

def calculate_regression_loss(loss_name, y_true, y_pred):
    """
    Calculates the regression loss without using NumPy functions.

    Args:
        loss_name (str): The name of the regression loss to use. Options include:
            - 'MAE': Mean Absolute Error
            - 'MSE': Mean Squared Error
            - 'RMSE': Root Mean Squared Error (optional)

    Returns:
        float: The calculated loss value.
    """

    if loss_name == 'MAE':
        # Mean Absolute Error (MAE)
        loss = 0
        for i in range(len(y_true)):
            loss += abs(y_true[i] - y_pred[i])
        loss /= len(y_true)
    elif loss_name == 'MSE':
        # Mean Squared Error (MSE)
        loss = 0
        for i in range(len(y_true)):
            loss += (y_true[i] - y_pred[i])**2
        loss /= len(y_true)
    elif loss_name == 'RMSE':
        # Root Mean Squared Error (RMSE)
        loss = 0
        for i in range(len(y_true)):
            loss += (y_true[i] - y_pred[i])**2
        loss /= len(y_true)
        loss = math.sqrt(loss)
    else:
        raise ValueError(f"Invalid loss name: {loss_name}")

    return loss


def generate_data_and_calculate_loss(num_samples, loss_name):
    """
    Generates data, calculates the loss, and prints the results.

    Args:
        num_samples (int): The number of samples to generate.
        loss_name (str): The name of the regression loss to use.
    """

    for sample_id in range(num_samples):
        # Generate random target and predicted values
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)

        # Calculate the loss
        loss_value = calculate_regression_loss(loss_name, [target], [predict])

        # Print the results
        print(f"Sample-{sample_id}:")
        print(f"Loss Name: {loss_name}")
        print(f"Target: {target}")
        print(f"Predict: {predict}")
        print(f"Loss: {loss_value}")


if __name__ == '__main__':
    # Get user input for number of samples
    while True:
        try:
            num_samples = int(input("Nhập số lượng sample: "))
            if num_samples > 0:
                break
            else:
                print("Số lượng sample phải là số nguyên dương!")
        except ValueError:
            print("Giá trị nhập vào không phải là số nguyên! Vui lòng nhập lại.")

    # Get user input for loss name
    while True:
        loss_name = input("Nhập tên loss (MAE, MSE, RMSE): ").upper()
        if loss_name in ['MAE', 'MSE', 'RMSE']:
            break
        else:
            print("Tên loss không hợp lệ! Vui lòng nhập MAE, MSE hoặc RMSE.")

    # Generate data and calculate loss
    generate_data_and_calculate_loss(num_samples, loss_name)

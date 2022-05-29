import numpy as np


def gradient_descent(ages, weights, sbp):
    theta0 = theta1 = theta2 = 0
    iterations = 100
    learning_rate = 0.005
    n = len(ages)

    for i in range(iterations):
        # linear hypothesis function
        y_predicted = theta0 + theta1 * ages + theta2 * weights

        #loss funtion
        loss_fun = (y_predicted - sbp)**2

        # cost function
        cost_fun = (1/2*n) * sum([val**2 for val in (y_predicted - sbp)])

        #coefficient: derivatives
        theta0_der = (1/2*n) * sum(y_predicted - sbp)
        theta1_der = (1/2*n) * sum((y_predicted - sbp)*ages)
        theta2_der = (1/2*n) * sum((y_predicted - sbp) * weights)

        # gradientdescentvalues in each iteration
        theta0 -= learning_rate * theta0_der
        theta1 -= learning_rate * theta1_der
        theta2 -= learning_rate * theta2_der

        print(
            f"theta0: {theta0}, theta1: {theta1}, theta2: {theta2}, cost: {cost_fun}, h0: {theta0 + theta1 * 65 + theta2 * 85}")


def main():
    ages = np.array([0.188, 0.155, 0.264, 0.284, 0.091, 0.071, 0.006,
                    0.361, 0.091, 0.381, 0.091, 0.329, 0.188, 0.155])
    weights = np.array([0.439, 0.272, 0.406, 0.128, 0.350, 0.028, 0.194,
                       0.406, 0.406, 0.528, 0.239, 0.472, 0.083, 0.106])
    sbp = np.array([0.178, 0.121, 0.350, 0.049, 0.105, 0.067,
                   0.310, 0.690, 0.181, 0.216, 0.159, 0.105, 0.291, 0.272])

    gradient_descent(ages, weights, sbp)


if __name__ == '__main__':
    main()

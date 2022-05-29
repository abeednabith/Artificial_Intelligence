import numpy as np
import matplotlib.pyplot as plt


def plot_diag(x, y):
    print(x)
    print(y)
    plt.figure()
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('exp(x)')
    plt.title('Exponential function')

    plt.show()


def second_order_function_calculations(x, y):
    theta0 = theta1 = theta2 = 0
    n = len(x)
    learning_rate = 0.003
    iterations = 1

    for i in range(iterations):
        # hypothesis function
        y_predict = theta0 + theta1 * x + theta2 * (x**2)

        # loss funtion
        loss_fun = (y_predict - y)**2

        # cost function
        cost_fun = (1/2*n) * sum([val**2 for val in (y_predict - y)])

        #coefficient: derivatives
        theta0_der = (1/n) * sum(y_predict - y)
        theta1_der = (1/n) * sum((y_predict - y) * x)
        theta2_der = (1/n) * sum((y_predict - y) * (x**2))

        # 0's in each iteration
        theta0 -= learning_rate * theta0_der
        theta1 -= learning_rate * theta1_der
        theta2 -= learning_rate * theta2_der

        print(theta0 + theta1 * x + theta2 * (x**2))
    #plot_diag(x, theta0 + theta1 * x + theta2 * (x**2))
    #print(theta0 + theta1 * x + theta2 * (x**2))


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([4, 5, 16, 21, 36, 45, 64, 77, 100, 117, 144])

second_order_function_calculations(x, y)

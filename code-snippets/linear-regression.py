#linear regression

def plot_regression_line(x, y, b, x1, y1): 

    plt.scatter(x, y, color = "g", marker = "o", s = 30)

    plt.ylim(-1,4)

    # plt.plot(a1, b1, color = "g", marker = "<")

    # plt.plot(a2, b2, color = "m", marker = ">")

    # predicted response vector 

    y_pred = b[0] + b[1]*x 

    #y1 =  b[1]*x1

    # plotting the regression line 

    plt.plot(x, y_pred, color = "k") 

    # plt.xlim(5,10)

    # putting labels 

    plt.xlabel('CGPA + TENTH + TWELFTH/Dip + AMCAT') 

    plt.ylabel('PLACED COUNT') 

    plt.plot(x1, y1, color = "r", marker = "v")

    plt.grid(True)

    # function to show plot 

    plt.show()

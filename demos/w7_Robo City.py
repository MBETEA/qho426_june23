import matplotlib.pyplot as plt
def display(x,y):

    plt.plot(x,y)
    x = []
    y = []
    plt.show()
    return x,y

def run():
    x_values =[0,1,3,4,5]
    y_values = [1,4,9,16,25]
    display(x_values, y_values)

run()
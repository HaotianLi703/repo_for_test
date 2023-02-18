import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = np.array([[[1, 1], [2,2],[3,3]],[[4,4],[5,5],[6,6]],[[7,7],[8,8],[9,9]]])
    print(a)
    print(a.shape)
    print(a.reshape(3, 3, 2, 1))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

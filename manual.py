from get import *
from test import *
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def manual(major,minor):
    number=1
    for i in major:
        for j in minor:
            pair={i,j}
            print(str(number) + ' Color pair is {}'.format(pair))
            number=number+1
            
if __name__ == '__main__':
    manual(MAJOR_COLORS,MINOR_COLORS)

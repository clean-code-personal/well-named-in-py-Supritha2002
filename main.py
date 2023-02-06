from test_fun import *
from get_fun import *
def color_coding_manual():
    manual = []
    for i in MAJOR_COLORS:
        for j in MINOR_COLORS:
            pair_number=get_pair_number_from_color(i, j)
            manual.append(f'{pair_number} - {i}, {j}')
    return "\n".join(manual)
if __name__ == '__main__':
    print(color_coding_manual())

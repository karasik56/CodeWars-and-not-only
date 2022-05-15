'''https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python'''
#TODO доделать

def snail(snail_map):
    full_path_list = []

    vert_column = [x[-1] for x in snail_map[1:-1: 1]]
    vert_column_revers = [y[0] for y in snail_map[-2:0:-1]]
    hor_centr_row = [x[-2] for x in snail_map[1:-1: 1]]

    lst = (snail_map[0],vert_column, snail_map[-1][::-1], vert_column_revers, hor_centr_row)
    for i in lst:
        full_path_list.extend(i)

    return full_path_list


print(snail([[1, 2, 3],
             [4, 5, 6],
             [10, 11, 12],
             [7, 8, 9]]))

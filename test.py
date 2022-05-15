
def chunk(new_list, chunk_size):
    chunk_list = []
    chunk_var = 0
    quantity_index = len(new_list)// chunk_size
    while len(chunk_list) <= quantity_index:
        elem_chunk_list = new_list[chunk_var: chunk_var + chunk_size]
        if len(elem_chunk_list) < chunk_size:
            break
        else:
            chunk_list.append(elem_chunk_list)
            chunk_var += chunk_size
    print(chunk_list)



new_list = list(range(2, 99, 2))
chunk(new_list, 10)










# current_string = ''
# new_string = ''
# counter = 1
# for i in current_string:
#     if i in new_string:
#         counter += 1
#     else:
#         if new_string != '':
#             new_string = new_string + str(counter) + i
#             counter = 1
#         else:
#             new_string = new_string + i
# new_string = new_string + str(counter)
#
# print(new_string)

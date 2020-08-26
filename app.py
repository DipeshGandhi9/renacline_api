#
# from copy import deepcopy
#
#
# def ge_unique_max_char_count(arr):
#     if 1 <= len(arr) <= 16:
#         max_possible_length_char = ''
#         if len(arr) == 1:
#             max_possible_length_char = arr[0]
#         else:
#             for item in arr:
#                 if 1 <= len(list(item)) <= 26:
#                     print("Test 1 passed")
#                     new_arr = deepcopy(arr)
#                     new_arr.remove(item)
#                     print(new_arr)
#                     for new_arr_val in new_arr:
#                         s = "{}{}".format(new_arr_val, item)
#                         if len(list(s)) == len(set(list(s))):
#                             if len(list(s)) > len(list(max_possible_length_char)):
#                                 max_possible_length_char = ''.join(s)
#                 else:
#                     print("Validation error 1 <= arr[i].length <= 26")
#                     break
#         return len(list(max_possible_length_char))
#     else:
#         print ("Validation error 1 <= arr.length <= 16")
#
# ge_unique_max_char_count(["un","iq","ue"])
#
#
# import random
#
#
# def unique_int_sum_at_zero(n):
#     if 1 <= n <= 1000:
#         list_of_numbers = []
#         for i in range(n - 1):
#             while True:
#                 random_number = random.randint(-n, n)
#                 if random_number not in list_of_numbers:
#                     list_of_numbers.append(random_number)
#                     break
#         missing_value = sum(list_of_numbers)
#         missing_element = -1 * missing_value
#         list_of_numbers.append(missing_element)
#         return list_of_numbers
#     else:
#         print("Validation error, Criteria 1 <= n <= 1000 does not matched" )
#         return 0
#
#
# print(unique_int_sum_at_zero(5))
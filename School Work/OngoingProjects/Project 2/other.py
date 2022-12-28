# from rle_program import *
# print (expand_by_index([2,1,3]))

# list = [3, 15, 6, 4]
# dic = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",  10: "a", 11: "b", 12: "c", 13: "d",  14: "e", 15: "f" }
# for i in range(len(list)):
#     list[i] = dic[list[i]]
# string = "".join(list)
# print(string)

# list=[]
# string = "3f64"
# dic2 = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6,  "7":7, "8":8,  "9":9, "a": 10,  "b": 11,  "c": 12, "d": 13, "e": 14, "f": 15}
# for item in string:
#     CorrectDigit = dic2[item]
#     list.append(CorrectDigit)
# print(list)
#
# arr = [15, 15, 15, 4, 4, 4, 4, 4, 4, 7, 7, 7]
# list2 = []
# current = arr[0]
# count = 1
# i = 0
# for item in arr[1:]:
#     if current == item:
#         count += 1
#         i+=1
#     else:
#         list2.append(count)
#         list2.append(arr[i])
#         current = item
#         count = 1
#         i += 1
# list2.append(count)
# list2.append(arr[i])
# print(list2)
#

# counter = 0
# for c in range(len(list2)):
#     if c % 2 == 0:
#         counter += 1
# print(counter)

# length = 0
# for c in range(len(list2)):
#     if c % 2 == 0:
#         length += list2[c]
# print(length)

# list3= []
# for c in range(len(list2)):
#     if c % 2 == 0:
#         for i in range(list2[c]):
#             (list3.append(list2[c+1]))
# print(list3)
#




# list = [4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# print(encode_rle(list))

# list = [15, 15, 15, 4, 4, 4, 4, 4, 4]
# print(to_hex_string(encode_rle(list)))                      #method 1 (returns string)
# print(count_runs(list))                                     #method 2 (returns counter)
# print(encode_rle(list))                                     #method 3 (returns list2)
# print(get_decoded_length(encode_rle(list)))                 #method 4 (returns length)
# print(decode_rle(encode_rle(list)))                         #method 5 (returns list3)
# print(string_to_data(to_hex_string(encode_rle(list))))      #method 6 (returns list4)



# def consecutive_four(arr):
#     current = arr[0]
#     count = 1
#     for item in arr[1:]:
#         if current == item:
#             count += 1
#         else: #item = 2, current = 3
#             # encode_rle: append count and current int res
#             current = item
#             count = 1
#         if count >= 4: # special case, there are no more thant 15 elements in a group
#             return True
#     return False
#
# def sum_by_parity(arr):
#     sum_even = 0
#     sum_odd = 0
#     for index, item in enumerate(arr):
#         if index % 2 == 0:
#             sum_even += item
#         else:
#             sum_odd += item
#     return [sum_even, sum_odd]
#
# def expand_by_index(arr):
#     res = []
#     for index, item in enumerate(arr):
#         for i in range(item):
#             res.append(index)
#     return res
#
# def numerical_count(string):
#     count = 0
#     for item in string:
#         if item.isdigit():
#             count += 1
#     return count

# list = [3, 15, 6, 4,5,3]
# list5 = []
# dic = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c",
#            13: "d", 14: "e", 15: "f"}
# for c in range(len(list)):
#     if c % 2 != 0:
#         list[c] = dic[list[c]]
#     list[c] = str(list[c])
# for i in range(0, len(list)-1, 2):
#     list5.append(list[i] + list[i+1])
# list5 = ":".join(list5)

#----------------------------------------------------------------------------------------------------------------

# string = "15f:64:14b:73:21"
# list = []
# list6 = []
#
# dic2 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
#             "d": 13, "e": 14, "f": 15}
# for item in string:
#     if item in dic2:
#         item = dic2[item]
#     list.append(item)
#
# for i in range(len(list)):
#     if i < len(list)-3:
#         if list[i+3] == ":" and list[i] != ":":
#             list[i] = int(str(list[i]) + str(list[i+1]))
#         else:
#             continue
#
# for i in range(len(list)):
#     if i < len(list) - 3:
#         if list[i+3] == ":" and list[i] != ":":
#             del list[i+1]
#
# for i in range(len(list)):
#     if list[i] != ":":
#         list6.append(list[i])
#
# print(list6)







# try:
#     for i in range(len(list)):
#         if list[i] == ":":
#             list
#     print(list)
# except:
#     pass
#

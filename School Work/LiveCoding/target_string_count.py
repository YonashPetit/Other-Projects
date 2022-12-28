def target_string_count(s, target):
    if len(s) < len(target):
        return 0
    if s[0: len(target)] == target:
        return 1 + target_string_count(s[1:], target)
    else:
        return target_string_count(s[1:], target)

# def sum_element(a_list):
#     if len(a_list) == 0:
#         return 0
#     return a_list[0] + sum_element(a_list[1:])

if __name__ == "__main__":
    string = input()
    string = string.split(" ")
    answer = target_string_count(string[0], string[1])
    print(answer)

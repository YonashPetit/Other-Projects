def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        item, loc = a_list[i], i
        while loc - 1 >= 0 and a_list[loc - 1] > item:
            a_list[loc] = a_list[loc-1]
            loc -= 1
        a_list[loc] = item


if __name__ == "__main__":
    size = int(input())
    a_list = []
    for i in range(size):
        a_list.append(int(input()))

    # print(a_list)
    insertion_sort(a_list)
    print(a_list)



def bubble_sort(a_list):
    for i in range(0, len(a_list)):
        for j in range(0, len(a_list)):
            if j + 1 < len(a_list) and a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

if __name__ == "__main__":
    size = int(input())
    a_list = []
    for i in range(size):
        a_list.append(int(input()))

    # print(a_list)
    bubble_sort(a_list)
    print(a_list)
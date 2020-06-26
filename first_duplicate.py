#python3

"""This will return the first duplicate in an input array with the SMALLEST
amount of distance between the ervals in the input array."""

def frst_duplicate(a: list) -> int:
    flag = -1
    len_a = len(a)
    dict_a = {}
    duplicate_list = []
    for i in range(len_a - 1):
        if a[i] in dict_a:
            flag = i
            dict_a[a[i]] = sum(i for i in range(a[i], len_a-1))
        else:
            dict_a[a[i]] = -1

    min_val = min(x for x in dict_a.values() if x != -1)
    #print(min_val)
    res = [k for k, v in dict_a.items() if v != -1 and v == min_val]

    return res[0]
"""
def first_duplicate(a: list) -> int:
    # Initialize index of first repeating element
    Min = -1

    # Creates an empty hashset
    myset = dict()
    len_a = len(a)

    # Traverse the input array from right to left
    for i in range(len_a -1, -1, -1):

        # If element is already in hash set,
        # update Min
        if a[i] in myset.keys():
            Min = i

        else:  # Else add element to hash set
            myset[a[i]] = 1

    # Print the result
    if (Min != -1):
        print("The first repeating element is",
              a[Min])
    else:
        print("There are no repeating elements")
"""



def main():
    a = [0, 5, 8, 11, 7, 38, 22, 11, 14, 174, 6, 14, 14, 4, 19]
    print(frst_duplicate(a))


if __name__ == "__main__":
    main()



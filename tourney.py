def centuryFromYear(year: int) -> int:
    year = str(year)

    if len(year) <= 2:
        return 1

    elif len(year) == 3 and int(year[1:]) > 0:
        return int(year[0]) + 1

    elif len(year) == 3 and year[1:] == '00':
        return int(year[0])

    elif len(year) == 4 and str(year[2:]) == '00':
        return int(str(year[0:2]))
    else:
        return int(year[0:2]) + 1


assert(centuryFromYear(55) == 1)
assert(centuryFromYear(667) == 7)
assert(centuryFromYear(800) == 8)
assert(centuryFromYear(1700) == 17)
assert(centuryFromYear(1701) == 18)
assert(centuryFromYear(1905) == 20)


"""
def arrayMaxConsecutiveSum(inputArray, k):

    result = 0
    currentSum = 0

    for i in range(k - 1):
        currentSum += inputArray[i]
    for i in range(k - 1, len(inputArray)):
        currentSum += inputArray[i]
        if currentSum < result:
            result = currentSum
        currentSum += inputArray[i - k + 1]

    return result


print(arrayMaxConsecutiveSum([1,2,3,4,5,6,7,44,108,1,2,4], 3))
"""



def numberOfOperations(a, b):

    if a < b:
        a, b = b, a
    if b % a == 0:
        return 0
    return 1 + numberOfOperations(a / b, b)





def reflectString(inputString):
    new_alphabet = []
    for i in inputString:
        new_alphabet.append(ord(i + 26))

    return new_alphabet










"""You have a apples, and your friend has b apples. You will be happy if - and only if - you both have the same number of apples.

Given integers a and b, check if you will be happy after you give your friend one of your apples.
Example
For a = 3 and b = 1, the output should be
shareAnApple(a, b) = true.
Input/Output
[execution time limit] 4 seconds (py3)
[input] integer a
Guaranteed constraints:
1 ≤ a ≤ 15.
[input] integer b
Guaranteed constraints:
1 ≤ b ≤ 10.
[output] boolean
true if you will be happy, false otherwise.
[Python3] Syntax Tips"""


def shareAnApple(a, b):
    a = a - 1
    if (a - 1 + b) % 2 == 0 and (a-1 == b):
        return True
    else:
        return False



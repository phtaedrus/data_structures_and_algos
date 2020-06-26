#python3

"""
Example
For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
"""


def check_palindrome(input_str: str) -> bool:
    mid = int(len(input_str) / 2)

    if len(input_str) == 1:
        return True

    if len(input_str) % 2 == 0:
        left_half = input_str[:mid]
        right_half = input_str[mid:]

    elif len(input_str) % 2 != 0:
        left_half = input_str[:mid + 1]
        right_half = input_str[mid:]

    if left_half[::-1] == right_half:
        return True
    else:
        return False

check_palindrome('aaaa')
print(check_palindrome('aaabaaa'))
print(check_palindrome("hlbeeykoqqqqokyeeblh"))
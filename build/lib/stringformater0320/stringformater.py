def reverse_string(string):
    """
    문자열을 뒤집어 반환합니다.
    """
    return string[::-1]

def is_palindrome(string):
    """
    주어진 문자열이 팰린드롬인지 확인합니다.
    """
    string = string.lower().replace(" ", "")
    return string == string[::-1]

def count_vowels(string):
    """
    문자열에 포함된 모음의 개수를 세어 반환합니다.
    """
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count
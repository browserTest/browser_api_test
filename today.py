import json


def test():
    nums = [4, 2, 4, 11, 6, 15]
    tar = 8
    for k in range(len(nums)):
        for t in range(len(nums) - 1, -1, -1):
            if nums[k] + nums[t] == tar:
                res = [k, t]
                return res
                break


def countBits(n):
    if n >= 0:
        res = 0
        li = list(bin(n).replace("0b", ""))
        for i in range(len(li)):
            if int(li[i]) == 1:
                res += 1
        return res

# print(countBits(10))


def is_pangram(s):
    for i in range(97, 123):
        if chr(i) in list(s):
            return True
        else:
            return False
            break

# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))


def getCount(inputStr):
    num_vowels = 0
    test = ["a", "e", "i"]
    for i in range(len(list(inputStr))):
            if list(inputStr)[i] in test:
                num_vowels += 1
    return num_vowels

# print(getCount("abracadabriea"))

def find_outlier(integers):
    res1 = []
    for i in range(len(integers)):
        res1.append(integers[i] % 2)
    if res1.count(0) > 1:
        for i in range(len(integers)):
            if integers[i] % 2 != 0:
                return integers[i]
    else:
        for i in range(len(integers)):
            if integers[i] % 2 != 1:
                return integers[i]


# print(find_outlier([2, 4, 6, 8, 10, 3]))


def string_title(a):
    str = a.title()
    return str

# print(string_title("How can mirrors be real if our eyes aren't real"))




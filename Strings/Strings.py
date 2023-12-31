import functools
import string

# string to int 
def stringToInt(s):
    return functools.reduce(
        lambda runningSum, c: runningSum*10 + string.digits.index(c),
        s[s[0] == '-'], 0) * (-1 if s[0] == '-' else 1)

# int to string 

def intToString(x):
    negativeBool = False
    if x < 0:
        x, negativeBool = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x ==0:
            break
    return ('-' if negativeBool else '') + ''.join(reversed(s))

# given a string and two numbers, first representing the first base of the num and second
# representing the second base , convert the string number to base number that was given

def convertBase(numString, base1,base2):
    def constructFromBase(numInt, base):
        return ('' if numInt == 0 else 
        constructFromBase(numInt//base, base) + string.hexdigits[numInt % base].upper())
    negative = numString[0] == '-'
    numInt = functools.reduce(
        lambda x, c:x * base1 + string.hexdigits.index(c.lower()),
        numString[negative:],0)
    return ('-' if negative else '') + ('0' if numInt == 0 else 
    constructFromBase(numInt,base2))

# compute integer representation of an excel column id

def decodeColumnNumber(column):
    return functools.reduce(lambda result,c: result*26 + ord(c) + ord('A') + 1, column, 0)

# print(decodeColumnNumber('ZZZ'))

# remove b's and replace a's with double d's

def replaceAndRemove(s):
    writeIndex, aCount = 0,0
    for i in range(len(s)):
        if s[i] != 'b':
            s[writeIndex] = s[i]
            writeIndex += 1
        if s[i] == 'a':
            aCount += 1
    curIndex = writeIndex - 1
    writeIndex += aCount - 1
    while curIndex >= 0:
        if s[curIndex] == 'a':
            s[writeIndex -1 :writeIndex +1] = 'dd'
            writeIndex -= 2
        else:
            s[writeIndex] = s[curIndex]
            writeIndex -= 1
        curIndex -= 1
    return s
a = ['a','b','d','c','a','a']
# print(replaceAndRemove(a))

# check if string is a palindrome 

def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i,j = i+ 1,j -1
    return True

# reverse words in a sentence

def reverseWords(s):
    s.reverse()

    def reverseRange(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start,end = start + 1, end -1

    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            break
        reverseRange(s, start, end - 1)
        start = end + 1
    reverseRange(s,start, len(s) - 1)
    return s

#compute mnemonics for a phone number 

def mnemonicsOfAPhoneNumber(number):
    MAPPING = ('0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ')

    def phoneMnemonicHelper(digit):
        if digit == len(number):
            mnemonics.append(''.join(partialMnemonic))
        else:
            for c in MAPPING[int(number[digit])]:
                partialMnemonic[digit] = c
                phoneMnemonicHelper(digit + 1)
    mnemonics, partialMnemonic = [], [0] *len(number)
    phoneMnemonicHelper(0)
    return mnemonics

# print(mnemonicsOfAPhoneNumber('7895847'))

# look and say problem, its weird but read the numbers outloud 1 one, two twos, three ones etc
# take a number n and return the nth integer in the look and say sequence return the result as
# a string

def lookAndSay(n):
    def nextNumber(s):
        result, i = [],0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1 
            result.append(str(count) + s[i])
            i += 1 
        return ''.join(result)
    s = '1'
    for _ in range(1, n):
        s = nextNumber(s)
    return s

# roman to decimal

def romanToDecimal(s):
    T = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    return functools.reduce(lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]),
    reversed(range(len(s)-1)), T[s[-1]])

print(romanToDecimal('XIVM'))
# compute valid IPs
# function must determine where to put commas

def getValidIpAddresses(s):
    def isValidPart(s):
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)
    result, parts = [], [None] * 4
    for i in range (1, min(4,len(s))):
        parts[0] = s[:i]
        if isValidPart(parts[0]):
            for j in range(1, min(len(s) -i,4)):
                parts[1] = s[i:i+j]
                if isValidPart(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2],parts[3] = s[i+j:i+k+j], s[i+j+k:]
                        if isValidPart(parts[2]) and isValidPart(parts[3]):
                            result.append('.'.join(parts))
    return result

#run length encoding
# and decoding

def decoding(s):
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:
            result.append(c * count)
            count = 0
    return ''.join(result)

def encoding(s):
    result, count = [], 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i -1]:
            result.append(str(count) + s[i - 1])
            count = 1
        else:
            count += 1
    return ''.join(result)

#find first occurence of a substring
# Rabin Karp algorithm
def findSubString(t,s):
    if len(s) > len(t):
        return -1
    
    BASE = 26
    t_hash = functools.reduce(lambda h, c:h*BASE + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c:h*BASE + ord(c), s, 0)
    power_s = BASE **max(len(s) - 1, 0)

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])
    
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)
    return -1 
def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        #print(x)
        #print(str[startIndex],str[endIndex])
        if str[startIndex] != str[endIndex]:
            #print(str, " is not a Palindrome")
            return False
            break
        startIndex += 1
        endIndex -= 1

        if startIndex == endIndex | (startIndex == endIndex +1):
            return True
            break

        #print(str[startIndex],str[endIndex])
        #print(startIndex,endIndex)
        #print(str, ' is a Palindrome')
    #return True


print(isPalindrome('rascdddedddcsar'))


def isPalindrome2(str):
    if str == str[::-1]:
        return True
    else: return False

print(isPalindrome('rascdddedcsar'))
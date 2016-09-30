
def reverseString(self, word):
    revList = word.split()
    revList.reverse()
    return revList.join()
print(reverseString("duck"))
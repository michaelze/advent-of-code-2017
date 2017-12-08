import unittest


class Password:

    def check(password):
        words = password.split(' ')
        seenWords = []
        for word in words:
            if word in seenWords:
                return False
            else:
                seenWords.append(word)
        return True

    def checkAnagram(password):
        words = password.split(' ')
        letterCounts = []
        for word in words:
            letterDict = {}
            for letter in word:
                if letter in letterDict:
                    letterDict[letter] = letterDict[letter] + 1
                else:
                    letterDict[letter] = 1
            letterCounts.append(letterDict)
        letterCountsLength = len(letterCounts)
        for index in range(0, letterCountsLength - 1):
            for compIndex in range(index + 1, letterCountsLength):
                letterCount = letterCounts[index]
                compLetterCount = letterCounts[compIndex]
                if len(letterCount) == len(compLetterCount):
                    anagram = True
                    for letter, count in letterCount.items():
                        if not letter in compLetterCount or letterCount[letter] != compLetterCount[letter]:
                            anagram = False
                            break
                    if anagram:
                        return False
        return True


class TestPassword(unittest.TestCase):

    def testCheck(self):
        self.assertTrue(Password.check('aa bb cc dd ee'))
        self.assertFalse(Password.check('aa bb cc dd aa'))
        self.assertTrue(Password.check('aa bb cc dd aaa'))

    def testCheckAnagram(self):
        self.assertTrue(Password.checkAnagram('abcde fghij'))
        self.assertFalse(Password.checkAnagram('abcde xyz ecdab'))
        self.assertTrue(Password.checkAnagram('a ab abc abd abf abj'))
        self.assertTrue(Password.checkAnagram('iiii oiii ooii oooi oooo'))
        self.assertFalse(Password.checkAnagram('oiii ioii iioi iiio'))


def checkPasswordFile(checkFunc):
    correctPasswords = 0
    with open('passwords.txt') as passwordsFile:
        passwords = passwordsFile.readlines()
        for password in passwords:
            if checkFunc(password.strip()):
                correctPasswords = correctPasswords + 1
    return correctPasswords


if __name__ == '__main__':
    correctPasswords1 = checkPasswordFile(lambda x: Password.check(x))
    correctPasswords2 = checkPasswordFile(lambda x: Password.checkAnagram(x))
    print ('correct passwords1: ' + str(correctPasswords1) + ' correct passwords2: ' + str(correctPasswords2))
    unittest.main()

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


class TestPassword(unittest.TestCase):

    def testCheck(self):
        self.assertTrue(Password.check('aa bb cc dd ee'))
        self.assertFalse(Password.check('aa bb cc dd aa'))
        self.assertTrue(Password.check('aa bb cc dd aaa'))


if __name__ == '__main__':
    correctPasswords = 0
    with open('passwords.txt') as passwordsFile:
        passwords = passwordsFile.readlines()
        for password in passwords:
            if Password.check(password.strip()):
                correctPasswords = correctPasswords + 1
    print ('correct passwords: ' + str(correctPasswords))
    unittest.main()

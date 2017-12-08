import unittest


class JumpList:

    def compute(input):
        jumpCount = 0
        currentIndex = 0
        inputLength = len(input)
        while currentIndex >= 0 and currentIndex < inputLength:
            jumpLength = input[currentIndex]
            input[currentIndex] += 1
            currentIndex += jumpLength
            jumpCount += 1
        return jumpCount

    def computeStranger(input):
        jumpCount = 0
        currentIndex = 0
        inputLength = len(input)
        while currentIndex >= 0 and currentIndex < inputLength:
            jumpLength = input[currentIndex]
            if jumpLength >= 3:
                input[currentIndex] -= 1
            else:
                input[currentIndex] += 1
            currentIndex += jumpLength
            jumpCount += 1
        return jumpCount


class TestJumpList(unittest.TestCase):

    def testCompute(self):
        self.assertEqual(JumpList.compute([0, 3, 0, 1, -3]), 5)

    def testComputestranger(self):
        self.assertEqual(JumpList.computeStranger([0, 3, 0, 1, -3]), 10)

def readInput():
    instructions = []
    with open('list.txt') as instListFile:
        instLines = instListFile.readlines()
        for instLine in instLines:
            instructions.append(int(instLine.strip()))
    return instructions


if __name__ == '__main__':
    instructions = readInput()
    jumpCount = JumpList.compute(instructions)
    print ('number of jumps: ' + str(jumpCount))
    instructions = readInput()
    jumpCount = JumpList.computeStranger(instructions)
    print ('number of strange jumps: ' + str(jumpCount))
    unittest.main()


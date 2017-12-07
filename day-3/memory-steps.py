import unittest
import math


class MemorySteps:

    def compute(input):
        nextSqrt = math.ceil(math.sqrt(input))
        nextSqr = math.pow(nextSqrt, 2)
        back = nextSqr - input
        inputX = 0
        inputY = 0
        if nextSqrt % 2 == 0:
            targetX = math.ceil(nextSqrt / 2) - 1
            targetY = targetX + 1
            if back > nextSqrt - 1:
                inputX = nextSqrt - 1
                inputY = back - (nextSqrt - 1)
            else:
                inputX = back
                inputY = 0
        else:
            targetX = math.ceil(nextSqrt / 2) - 1
            targetY = targetX
            if back > nextSqrt - 1:
                inputX = 0
                inputY = nextSqrt - (back - nextSqrt + 1) - 1
            else:
                inputX = nextSqrt - 1 - back
                inputY = nextSqrt - 1
        return int(abs(inputX - targetX) + abs(inputY - targetY))


class TestMemorySteps(unittest.TestCase):

    def testCompute(self):
        self.assertEqual(MemorySteps.compute(12), 3)
        self.assertEqual(MemorySteps.compute(14), 3)
        self.assertEqual(MemorySteps.compute(13), 4)
        self.assertEqual(MemorySteps.compute(15), 2)
        self.assertEqual(MemorySteps.compute(1024), 31)

        self.assertEqual(MemorySteps.compute(1), 0)
        self.assertEqual(MemorySteps.compute(21), 4)
        self.assertEqual(MemorySteps.compute(23), 2)
        self.assertEqual(MemorySteps.compute(17), 4)
        self.assertEqual(MemorySteps.compute(25), 4)


if __name__ == '__main__':
    print ("solution for 289326 " + str(MemorySteps.compute(289326)))

    unittest.main()
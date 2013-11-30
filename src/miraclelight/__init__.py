import fcntl
import os
import sys
import termios
import unittest
from unittest import runner


class MiracleTestResult(runner.TextTestResult):
    def startTest(self, test):
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

        count = 10
        i = 0
        face = "( ^q^)ﾉｼ"
        hands = ["ﾉ ", "ﾉｼ", "ノ"]
        self.stream.write(face)
        self.stream.flush()
        try:
            while i < count:
                c = sys.stdin.read(1)
                if c == '\n':
                    i += 1
                    self.stream.write("\b\b")
                    self.stream.write(hands[0])
                    self.stream.flush()
                    hands = hands[1:] + [hands[0]]
        finally:
            self.stream.write("\b" * len(face))
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

        super(MiracleTestResult, self).startTest(test)


class MiracleTestRunner(runner.TextTestRunner):
    resultclass = MiracleTestResult

    def run(self, test):
        self.stream.writeln("ライトをふって　プリキュアを　おうえんしてね！"
                            "(Press enter, enter, enter)")
        return super(MiracleTestRunner, self).run(test)


class TestProgram(unittest.TestProgram):
    verbosity = 1

    def __init__(self, module=None, defaultTest='.', argv=None,
                 testRunner=None, testLoader=None, exit=True):
        if testRunner is None:
            testRunner = MiracleTestRunner
        extra_args = {'exit': exit}
        super(TestProgram, self).__init__(
            module=module, defaultTest=defaultTest, argv=argv,
            testRunner=testRunner, testLoader=testLoader, **extra_args)

run = main = TestProgram

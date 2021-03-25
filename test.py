from multiprocessing import Process
import os

def processTest(t):
    print("Process: ", t)
    print("Process Parent ID: ", os.getppid())
    print("Process ID: ", os.getpid())
    print()


def testfunc():
    print('Hello, world, project 2')



# Haha, so this is what makes the comments comments!
if __name__ == '__main__':
    processTest("Parent")
    p1 = Process(target=processTest, args=("Child 1",))
    p2 = Process(target=processTest, args=("Child 2",))
    p3 = Process(target=processTest, args=("Child 3",))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
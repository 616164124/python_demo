import time
import os


def method1(one):
    print(one)
    print(os.path)


def method2(param):
    print(param)
    print("method2")
    return "sjlfkj"

if __name__ == '__main__':
    print(time.thread_time())
    method1("sf")
    print(method2("ij"))

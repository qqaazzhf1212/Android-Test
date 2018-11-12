import os
import time


# 控制类
class Manager(object):

    def __init__(self, count):
        self.counter = count
        self.memfile = open('mem.txt', 'w')

    # 单次测试过程
    def testRunTime(self):
        cmd = "adb shell  dumpsys  meminfo com.yhjs.bbus.app"
        result = os.popen(cmd).readlines()
        for line in result:
            if "TOTAL" in line:
                mem = line.split("    ")[3]
                break
        print("内存：", mem)
        self.memfile.write(mem + "\n")

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.testRunTime()
            self.counter = self.counter - 1
            time.sleep(2)
        # 关闭资源
        self.memfile.close()


if __name__ == "__main__":
    controller = Manager(10)
    controller.run()

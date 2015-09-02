__author__ = 'vladimir'


class CPU(object):

    def __init__(self, file_name1="jump.txt", file_name2="execute.txt"):
        self.file_jump = file_name1
        self.file_execute = file_name2

    def jump(self):
        with open(self.file_jump, 'r') as input_:
            for item in input_:
                print(item)

    def execute(self):
        with open(self.file_execute, 'r') as input_:
            for item in input_:
                print(item)


class Memory(object):

    def __init__(self, file_name="load.txt"):
        self.file_load = file_name

    def load(self):
        with open(self.file_load, 'r') as input_:
            for item in input_:
                print(item)


class HardDrive(object):

    def __init__(self, file_name="read.txt"):
        self.file_read = file_name

    def read(self):
        with open(self.file_read, 'r') as input_:
            for item in input_:
                print(item)


# FACADE
class Computer(object):

    def __init__(self):
        pass

    def start(self):
        #  Instance of computer component
        cpu = CPU()
        mem = Memory()
        hd = HardDrive()

        hd.read()
        mem.load()
        cpu.jump()
        cpu.execute()




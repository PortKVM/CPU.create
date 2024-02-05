import random

class CPU:
    def __init__(self, name, cores, speed):
        self.name = name
        self.cores = cores
        self.speed = speed

    def generate_random_cpu(self):
        self.name = "CPU-" + str(random.randint(1, 1000))
        self.cores = random.randint(1, 8)
        self.speed = random.randint(1, 5)

    def print_cpu_info(self):
        print("CPU Name:", self.name)
        print("CPU Cores:", self.cores)
        print("CPU Speed:", self.speed, "GHz")

def create_cpu():
    cpu = CPU("", 0, 0)
    cpu.generate_random_cpu()
    return cpu

def main():
    cpu1 = create_cpu()
    cpu2 = create_cpu()
    cpu3 = create_cpu()

    cpu1.print_cpu_info()
    cpu2.print_cpu_info()
    cpu3.print_cpu_info()

if __name__ == "__main__":
    main()

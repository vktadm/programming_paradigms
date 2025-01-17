class CPU:
    def __init__(self, name: str, fr: str):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name: str, volume: int):
        self.name = name
        self.volume = volume

class MotherBoard():

    def __init__(self, name: str, cpu: CPU, mem_slots: list):
        self.name = name
        self.total_mem_slots = 4
        self.cpu = cpu
        self.mem_slots = mem_slots

    def get_config(self) -> list:
        motherboard = "; ".join([slot.name + " - " + str(slot.volume) for slot in self.mem_slots])
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {motherboard}']


if __name__ == '__main__':
    cpu = CPU('asus', 1333)
    mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
    mb = MotherBoard('Asus', cpu, [mem1, mem2])
    print(mb.get_config())
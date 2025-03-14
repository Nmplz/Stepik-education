class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = []

        if len(args) <= self.total_mem_slots:
            for i, memory_module in enumerate(args, start=1):
                if isinstance(memory_module, Memory):
                    setattr(self, f"memory{i}", memory_module)
                    self.mem_slots.append(memory_module)
                else:
                    raise ValueError(
                        "Все аргументы после cpu должны быть объектами класса Memory"
                    )

    def get_config(self):

        conf = [
            f"Материнская плата: {self.name}",
            f"Центральный процессор: {self.cpu.name},{self.cpu.fr}",
            f"Слотов памяти: {self.total_mem_slots}",
        ]

        conf1 = "Память: "

        for i in self.mem_slots:
            conf1 += f"{i.name} - {i.volume};"
        conf.append(conf1[: len(conf1) - 1])

        return conf


cpu = CPU("Intel i7", "3.4GHz")
mem1 = Memory("Kingston", "8GB")
mem2 = Memory("Corsair", "16GB")

mb = MotherBoard("MSI", cpu, mem1, mem2)

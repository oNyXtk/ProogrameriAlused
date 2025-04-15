import random

class component:
    def __init__(self, model, manufacturer, power_usage):
        self.model = model
        self.manufacturer = manufacturer
        self.power_usage = power_usage
        self.status = "ok"  # Статус по умолчанию
        
    def get_info(self):
        return f"Model: {self.model}, Manufacturer: {self.manufacturer}, Power Usage: {self.power_usage}W, Status: {self.status}"
        
    def run_diagnostic(self):
        raise NotImplementedError("This method should be implemented by subclasses")

class cpu(component):
    def __init__(self, model, manufacturer, power_usage, cores, frequency, temperature, status="ok"):
        super().__init__(model, manufacturer, power_usage)
        self.cores = cores
        self.frequency = frequency
        self.temperature = temperature
        self.status = status
        
    def run_diagnostic(self):
        temp = random.randint(40, 100)  # Случайная температура
        if temp > 85:
            self.status = "overheating"
            return False
        self.status = "ok"
        return True

class gpu(component):
    def __init__(self, model, manufacturer, power_usage, vram, frequency, driver_installed, status="ok"):
        super().__init__(model, manufacturer, power_usage)
        self.vram = vram
        self.frequency = frequency
        self.driver_installed = driver_installed
        self.status = status
        
    def run_diagnostic(self):
        if not self.driver_installed or self.vram < 2:
            self.status = "missing drivers or low VRAM"
            return False
        self.status = "ok"
        return True

class ram(component):
    def __init__(self, model, manufacturer, power_usage, size, frequency, usage, status="ok"):
        super().__init__(model, manufacturer, power_usage)
        self.size = size
        self.frequency = frequency
        self.usage = usage
        self.status = status
        
    def run_diagnostic(self):
        if self.usage > 95 or self.size < 2:
            self.status = "memory error"
            return False
        self.status = "ok"
        return True

class storage(component):
    def __init__(self, model, manufacturer, power_usage, storage_type, capacity, read_speed, bad_sectors, status="ok"):
        super().__init__(model, manufacturer, power_usage)
        self.storage_type = storage_type
        self.capacity = capacity  # В GB или TB
        self.read_speed = read_speed  # В MB/s
        self.bad_sectors = bad_sectors
        self.status = status

    def run_diagnostic(self):
        if self.read_speed < 10 or self.bad_sectors > 100:
            self.status = "read speed is low or too many bad sectors"
            return False
        self.status = "ok"
        return True
    
# Создание объектов
cpu_component = cpu(model="Intel i7-12700", manufacturer="Intel", power_usage=65, cores=8, frequency=3.6, temperature=50)
gpu_component = gpu(model="RTX 3080", manufacturer="NVIDIA", power_usage=320, vram=10, frequency=1.71, driver_installed=True)
ram_component = ram(model="DDR4", manufacturer="Corsair", power_usage=15, size=16, frequency=3200, usage=50)
storage_component = storage(model="Samsung 970 EVO", manufacturer="Samsung", power_usage=15, storage_type="SSD", capacity=1000, read_speed=3500, bad_sectors=0)

# Создание объекта компьютера
class computer:
    def __init__(self):
        self.components = []
        
    def addcomponents(self, components):
        # Добавляем переданные компоненты в список
        self.components.append(components)
        
    def totalpower(self):
        # Подсчитываем суммарное потребление мощности
        total_power = sum(component.power_usage for component in self.components)
        return total_power
    
    def diagnosting_all(self):
        # Запускаем диагностику для всех компонентов
        for component in self.components:
            if not component.run_diagnostic():
                return f"Diagnostic failed for {component.model}: {component.status}"
        return "All components passed the diagnostic check!"

# Создание объекта компьютера и добавление компонентов
my_computer = computer()
my_computer.addcomponents(cpu_component)
my_computer.addcomponents(gpu_component)
my_computer.addcomponents(ram_component)
my_computer.addcomponents(storage_component)

# Вывод общей мощности
print(f"Total power usage: {my_computer.totalpower()}W")

# Диагностика всех компонентов
print(my_computer.diagnosting_all())

# Вывод информации о каждом компоненте
for component in my_computer.components:
    print(component.get_info())
# base/ProcessManager.py
class ProcessManager:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

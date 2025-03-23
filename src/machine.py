import logging

# Machine class providing place to hold the Virtual machine details.
#includs returning dictionary and logging function

class machine:
    def __init__(self, name, os, cpu, ram, disk_space):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
        self.disk_space = disk_space
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def machine_list(self):
        return [self.name, self.os, self.cpu, self.ram, self.disk_space]
    
    def logging(self):
        self.logger.info(f"Machine {self.name} with {self.os} Successfully initialized!")



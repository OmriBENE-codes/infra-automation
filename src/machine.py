import logging
from pydantic import BaseModel, Field
import json
import os


# Machine class providing place to hold the Virtual machine details.
#includs returning dictionary and logging function

class machine:
    
    
 def machine_details():
        name = input("Enter machine name: ")
        os = input('Enter the os: ')
        cpu = input('Enter the amount of CPUs: ')
        ram = input('Enter the amount of RAM to provide: ')
        disk_space = input("Enter how much space to provide: ")

        machine = [
             name, 
             os,  
             cpu, 
             ram, 
             disk_space

    ]

        print(f"name: " + name, "os: "+ os, "cpu: " +cpu, "ram: " +ram, "disk_space: " +disk_space)
        return machine



def input_validation(machine_details):
    schema = {

            "name": {"type": "string"},
            "os": {"type": "string"},
            "cpu": {"type": "float"},
            "ram": {"type": "string"},
            "disk_space": {"type": "string"}
    }

    try:
        validate(instance = machine_details, schema = schema)
    except ValidationError as e:
        print(f'Invalid input: {e.message}')
        return False
    return True


def json_details(machine):
        path = 'configs/instance.json'
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            try:
                with open(path, "r") as file:
                    json_data = json.load(file)
                    if not isinstance(json_data, list):
                        print(f"Warning: The existing data is not a list. Reinitializing to an empty list.")
                        json_data = []

            except (FileNotFoundError, json.JSONDecodeError):
                json_data = []

            json_data.append(machine)

    
            with open('configs/instance.json', "w") as file:
                json.dump(json_data, file, indent=4)
            print("The machine details have been saved to configs/instance.json")
        except Exception as e:
            print(f'Error happend when saving to JSON: {str(e)}')


    
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

machine = machine.machine_details()
if input_validation(machine):
    json_details(machine)

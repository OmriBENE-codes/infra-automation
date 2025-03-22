from jsonschema import validate, ValidationError
import json
import os
import subprocess

'''
Here the users are asked to provide through input 
the machine details. {e.g cpu, ram, os...} '''


def machine_details():
    name = input("Enter machine name: ")
    os = input('Enter the os: ')
    cpu = input('Enter the amount of CPUs: ')
    ram = input('Enter the amount of RAM to provide: ')
    disk_space = input("Enter how much space to provide: ")

    machine = {
        'name': name, 
        'os': os, 'cpu': cpu, 
        'ram': ram, 
        'disk_space': disk_space

}

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
    path = "C:/Users/USER/Devops project/infra_automation/configs/instance.json"
    with open(path, "w") as file:
        json.dump(machine, file, indent=4)

    
    with open(path, "r") as file:
        data = json.load(file)
        print("Loaded data from JSON file:\n", data)


def bash_script():
    try:
        subprocess.run(["bash", "scripts/installing_nginx.sh"], check = True)
    except subprocess.CalledProcessError as e:
        print(f"Error have occured: {e}")







machine = machine_details()
if input_validation(machine):
    json_details(machine)

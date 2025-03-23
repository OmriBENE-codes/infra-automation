from jsonschema import validate, ValidationError
import json
import os
import subprocess
import machine

'''
Here the users are asked to provide through input 
the machine details. {e.g cpu, ram, os...} '''


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


def bash_script():
    try:
        subprocess.run(["bash", "scripts/installing_nginx.sh"], check = True)
    except subprocess.CalledProcessError as e:
        print(f"Error have occured: {e}")


  

machine = machine_details()
if input_validation(machine):
    json_details(machine)

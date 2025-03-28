import logging
from pydantic import BaseModel, Field, ValidationError
import json
import os


# Machine class providing place to hold the Virtual machine details.
#includs returning dictionary and logging function


LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
LOG_FILE = os.path.join(LOG_DIR, "provisioning.log")

os.makedirs(LOG_DIR, exist_ok=True)  # Ensure logs directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Machine(BaseModel):
    name: str = Field(..., min_length=1, description="Machine name")
    os: str = Field(..., min_length=1, description="Operating System (e.g windows, linux, mac)")
    cpu: float = Field(..., gt=0, description="Number of CPUs")
    ram: int = Field(..., gt=0, description="PRAM in GB")
    disk_space: int = Field(..., gt=0, description="Disk space in GB")
    
    
def machine_details(): #function to get and store the machine details inputted by users.
    while True:
        try:
            name = input("Enter machine name: ")
            os = input("Enter the OS: ")
            cpu = int(input("Enter the number of CPUs: "))
            ram = int(input("Enter RAM size in GB: "))
            disk_space = int(input("Enter disk space in GB: "))

            machine = Machine(name=name, os=os, cpu=cpu, ram=ram, disk_space=disk_space)
            logging.info(f'Machine details entered by the user: {machine}')
            return machine.dict()
        except ValidationError as e:
             print("\nInvalid input. Please correct the following part: ")
             for error in e.errors():
                print(f" - {error['loc'][0]}: {error['msg']}")
        except ValueError:
             print('Invalid input type. Please enter the numbers requested.')

def save_machine_details(machine_data): #machine details --> json saving function
    path = 'configs/instance.json'
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)

        try: #Loads the existing data from the log file
            with open(path, "r") as file:
                json_data = json.load(file)
                if not isinstance(json_data, list):
                    logging.warning(f"Warning: The existing data is not a list. Reinitializing to an empty list.")
                    json_data = []

        except (FileNotFoundError, json.JSONDecodeError):
            json_data = []

        json_data.append(machine_data) #append to the json file 
        
        with open(path, "w") as file:
            json.dump(json_data, file, indent=4)
        logging.info("The machine details was successfully saved into Instance.json file")
        print("The machine details have been saved successfully!")
    except Exception as e:
        logging.info(f"Error saving machine details: {str(e)}")
        print(f'Error happend when saving machine detwails into JSON')

if __name__ == "__main__":
    machine_data = machine_details()
    save_machine_details(machine_data)
from jsonschema import validate, ValidationError
import json
import os
import subprocess
import machine

'''
Here the users are asked to provide through input 
the machine details. {e.g cpu, ram, os...} '''



def bash_script():
    try:
        subprocess.run(["bash", "scripts/installing_nginx.sh"], check = True)
    except subprocess.CalledProcessError as e:
        print(f"Error have occured: {e}")


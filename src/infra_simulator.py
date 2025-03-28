import subprocess
import logging
from machine import Machine, machine_details, save_machine_details
import os
'''


'''
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
LOG_FILE = os.path.join(LOG_DIR, "provisioning.log")

os.makedirs(LOG_DIR, exist_ok=True) #ensures logs folder exists
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Starting infrastructure simulation...")
    machine_data = machine_details()
    save_machine_details(machine_data)
    logging.info("Infrastructure simulation has successfullt completed.")
    print(f"The infrastructure provisioning simulation completed for: {machine_data['name']}.")

    bash_script()

def bash_script():
    logging.info("Executing Nginx installation script...")
    script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts', 'install_nginx.sh')

    try:
        subprocess.run(["bash", script_path, "--simulate"], check=True)
        logging.info("Nginx installation completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred while installing Nginx: {e}")
        print(f"Error have occured: {e}")


if __name__ == "__main__":  
    main()


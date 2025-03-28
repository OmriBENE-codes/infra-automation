#!/bin/bash

LOG_FILE="~/infra_automation/logs/nginx_install_simulation.log"

# Clear previous logs
if [ -f "$LOG_FILE" ]; then
    echo "Clearing previous logs..." > $LOG_FILE
fi

echo "Starting Nginx installation simulation..." | tee -a $LOG_FILE

# Simulate checking if Nginx is installed
echo "Checking if Nginx is installed..." | tee -a $LOG_FILE
sleep 1

if [ "$1" == "--simulate" ]; then
    echo "Nginx is not installed. Simulating installation..." | tee -a $LOG_FILE
    sleep 2
    echo "Nginx installation simulated successfully!" | tee -a $LOG_FILE
else
    echo "Nginx is already installed (simulated)." | tee -a $LOG_FILE
fi

# Simulate enabling and starting Nginx
echo "Simulating enabling and starting Nginx service..." | tee -a $LOG_FILE
sleep 1
echo "Nginx service is running (simulated)." | tee -a $LOG_FILE

echo "Nginx installation simulation completed." | tee -a $LOG_FILE
exit 0
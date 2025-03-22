#!/bin/bash

#a simple bash script of installing Nginx service.

if ! command - v nginx &> /dev/null
then
    echo "Nginx not found on platform, Installing now.."
    sudo apt udpate && sudo apt install -y nginx

else 
    echo "Nginx is already installed." 
fi

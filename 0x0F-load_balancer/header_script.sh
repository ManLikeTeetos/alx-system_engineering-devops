#!/bin/bash

# Set the custom header name and value
HEADER_NAME="X-Served-By"
HEADER_VALUE=$(hostname)

# Modify the Nginx configuration file
sudo sed -i "s|# add_header.*|add_header $HEADER_NAME $HEADER_VALUE;|" /etc/nginx/nginx.conf

# Restart Nginx to apply the changes
sudo service nginx restart

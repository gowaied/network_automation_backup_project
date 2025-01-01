# network_automation_backup_project

# Network Automation - Cisco Device Configuration Backup

This project is a Python script designed to automate the backup of Cisco device configurations. It uses the **Netmiko** library to connect to Cisco devices, retrieve their configuration, and store it locally in a file. The script allows you to input multiple device IP addresses, automatically handle login credentials, and save the configuration files in an organized manner.

## Features

- **Automated Configuration Backup**: Connects to Cisco devices and backs up the running configuration.
- **Error Handling**: Includes error handling for authentication failures and connection timeouts.
- **Flexible Input**: Allows for multiple target IPs to be entered dynamically.
- **Config File Storage**: Saves each device’s configuration in a text file named after the device's hostname.

## Requirements

- Python 3.x
- Netmiko (`pip install netmiko`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/NetworkAutomation.git

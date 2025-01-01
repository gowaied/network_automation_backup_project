from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException
from getpass import getpass
import ipaddress

#Gather Credentials
username = input('Please, enter the username: ')
password = getpass('Please, enter the password: ')
secret = getpass('Please, enter the secret: ')

#Gather Target IP addresses
print('Enter the Target IPs one by one and write "done" when finish.')
ip_list = []
while True:
    ip_add = input('Enter IP: ')
    if ip_add.lower().strip() == 'done':
        break
    try:
        ipaddress.IPv4Address(ip_add)
        ip_list.append(ip_add)
    except ipaddress.AddressValueError:
        print('Invalid IP address! Please, try again.')

#Define the function
def backup(username, password, secret, ip_list):
    for ip in ip_list:
        device = {
                    'device_type' : 'cisco_ios',
                    'host' : ip,
                    'username' : username,
                    'password' : password,
                    'secret' : secret
                 }
        try:
            print(f'Connecting to host {ip}....')
            net_connect = ConnectHandler(**device)
            net_connect.enable()
            hostname = net_connect.send_command('show run | inc host').split()[1]
            config = net_connect.send_command('show run')
            file = open(f'{hostname}_config.txt' , 'w')
            file.write(config)
            print(f'Backup has been done for {hostname}')
        except NetMikoAuthenticationException:
            print(f'Authentication failed for host {ip}. Please check the credentials.')
        except NetMikoTimeoutException:
            print(f'Timeout while connecting to host {ip}. This host might be unreachable.')
        except Exception as e:
            print(f'Unexcpected error for device {ip}: {e}.')

backup(username,password,secret,ip_list)
print('The pross is Done!')
input('Press Enter to close....')

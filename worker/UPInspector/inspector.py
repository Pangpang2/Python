#from paramiko.client import SSHClient
import paramiko

def connect_ssh_server():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('stg-df-dkr3', port='22', username='mli', password='Liapaopao2', key_filename=r'D:\INTG\stg-df-dkr3_key_Important\Xshell_private')
    stdin, stdout, stderr = client.exec_command('cd /var')
    print stdin.readlines()
    print stdout.readlines()
    print stderr.readlines()
    stdin, stdout, stderr = client.exec_command('find  /var/log/docker/udbf_translator/ -name *_inf*g')
    # stdin, stdout, stderr = client.exec_command('pwd')
    print stdout.readlines()


if __name__ == '__main__':
    connect_ssh_server()
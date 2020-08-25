from paramiko import SSHClient, Transport, AutoAddPolicy, util
import time


t1 = time.clock()
hostname = 'stg-df-dkr4'
username = 'mli'
password = 'Liapaopao2'
key_filename = r'D:\INTG\stg-df-dkr3_key_Important\XShell_private'

util.log_to_file('.\paramiko.log')
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect(hostname, username=username, password=password, key_filename=key_filename)

# t2 = time.clock()
# print t2-t1
stdin, stdout, stderr = client.exec_command('sudo docker exec ingestor_uploadws_processor_app_1 ps aux')
while not stdout.channel.exit_status_ready():
    # Only print data if there is data to read in the channel
    if stdout.channel.recv_ready():
        rl, wl, xl = select.select([ stdout.channel ], [ ], [ ], 0.0)
        if len(rl) > 0:
            tmp = stdout.channel.recv(1024)
            output = tmp.decode()
            print(output)

# sftp = client.open_sftp()
# local_path = r'E:\Git\Python\learnpy\ssh\d3.dfcxautdd10a5bd@d3one.com_2019-07-01_23_56_52_376.p.zip'
# remote_path = '/var/common/ingestor/d3/138025721/2019-07-01/d3.dfcxautdd10a5bd@d3one.com_2019-07-01_23_56_52_376.p.zip'
# sftp.get(remote_path, local_path)

# sftp.close()
client.close()

# print time.clock() - t2




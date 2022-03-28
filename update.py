import os

commands = ['apt update -y', 'apt upgrade -y', 'apt dist-upgrade -y']

for x in range(0, 3):
  os.system(commands[x])
  

import subprocess

print(subprocess.call('path',shell=True))
print(subprocess.check_call('path',shell=True))
print(subprocess.check_output('ipconfig',shell=True))
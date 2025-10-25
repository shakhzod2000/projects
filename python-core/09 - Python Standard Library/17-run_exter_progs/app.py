import subprocess

# res = subprocess.run("wsl python3 other.py", 
#                      capture_output=True, 
#                      text=True)
try:
    res = subprocess.run("wsl false", 
                        capture_output=True, 
                        text=True, check=True)
    # check=True automatically raises an exception
    print('args', res.args)
    print('returncode', res.returncode)
    print('stderr', res.stderr)
    print('stdout', res.stdout)
except subprocess.CalledProcessError as e:
    print(e)

# below are legacy methods
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen
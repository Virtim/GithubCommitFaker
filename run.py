import subprocess
import time
import fileinput, sys

addCommand = "git add ."
commitCommand = "git commit -m \" \""
pushCommand = "git push"
commitCounter = -10000

while commitCounter < 100000:
    print commitCommand
    timer = 0
    if commitCounter % 2 == 0:
        for line in fileinput.input(["test.txt"], inplace=True):
            line = line.replace("car", "truck")
            # sys.stdout is redirected to the file
            sys.stdout.write(line)
    else:
        for line in fileinput.input(["test.txt"], inplace=True):
            line = line.replace("truck", "car")
            # sys.stdout is redirected to the file
            sys.stdout.write(line)
    process = subprocess.Popen(addCommand.split(), stdout=subprocess.PIPE)
    process = subprocess.Popen(commitCommand.split(), stdout=subprocess.PIPE)
    process = subprocess.Popen(pushCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    commitCounter += 1
    while timer < 60:
        time.sleep(1)
        timer += 1
        print(timer)

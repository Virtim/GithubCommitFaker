import subprocess
import time
import fileinput, sys
import os
import random

commitMessage = os.environ['CIRCLE_SHA1']
commitCommand = "git commit --allow-empty -m {}"
pushCommand = "git push origin master -f"
removeIndexLock = "sudo rm -rf ./.git/index.lock"
timeToSleep = 2
commitCounter = 25

while commitCounter > 0:
    # try:
    #     os.remove('./.git/index.lock')
    # except OSError:
    #     print "Index lock doesnt exist"
    # print "Going to sleep for ", timeToSleep, " seconds"
    process = subprocess.Popen(commitCommand.split(), stdout=subprocess.PIPE)
    time.sleep(1)
    process = subprocess.Popen(pushCommand.split(), stdout=subprocess.PIPE)
    time.sleep(1)
    print("One more commit added to github! Only {commitCounter} left until script is done")
    commitCounter -= 1
    time.sleep(timeToSleep)

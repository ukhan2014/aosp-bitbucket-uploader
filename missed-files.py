import os
import subprocess
import time
os.chdir("/path/to/android10/source/")

# Open the file with read only permit
f = open('gitignores', "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
lines = f.readlines()
count = 0
for line in lines:
                count+=1
                print("line " + str(count) + "\n")
                print(line+ "\n")

                path = "/path/to/android10/source/" + line.rstrip()
                print("adding missing files at path: \n" + path)
                os.chdir(path)

                bashCommand = "git add * -f"
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
                #print("output: " + output + "\nerror: " +error +"\n")
                time.sleep(5)

                bashCommand = ['git', 'commit', '-m', 'fix missing files']
                process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
                output, error = process.communicate()
                #print("output: " + output + "\nerror: " +error +"\n")
                time.sleep(5)

                bashCommand = "git push -u origin master"
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
                #print("output: " + output + "\nerror: " +error +"\n")
                time.sleep(10)
f.close()

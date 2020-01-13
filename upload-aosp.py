import os
import subprocess
import time
os.chdir("/path/to/android10/source/")

# Open the file with read only permit
f = open('manifest', "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
lines = f.readlines()
count = 0
for line in lines:
                count+=1
                print("line " + str(count) + "\n")
                print(line+ "\n")
                split = line.split()
                git_link = "git@bitbucket.org:yourAccount/" + split[0] + ".git"
                path = split[1]

                os.chdir("/path/to/android10/source/" + path)

                bashCommand = "rm -rf .git"
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
                #print("output: " + output + "\nerror: " +error +"\n")

                bashCommand = "git init"
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
                #print("output: " + output + "\nerror: " +error +"\n")

                bashCommand = "git remote add origin " +  git_link
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
                #print("output: " + output + "\nerror: " +error +"\n")

                bashCommand = "git add *"
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
                #print("output: " + output + "\nerror: " +error +"\n")
                
                bashCommand = ['git', 'commit', '-m', 'initial commit']
                process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
                output, error = process.communicate()
                #print("output: " + output + "\nerror: " +error +"\n")

                bashCommand = "git push -u origin master"
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
                #print("output: " + output + "\nerror: " +error +"\n")
f.close()

import os
import subprocess
import re 
import git
import datetime
import logging

COMPMODE = True
DEBUG = True

dates = {}
log = logging.getLogger()

filename = "lastChange.txt"  # TODO: Persistent logging
condaPath = "condaEnvs//"
today = datetime.datetime.now()


#################### IDENTIFY ENVS ####################
def findCondaEnvs() -> list:    
    cb = subprocess.check_output("conda info --envs", shell=True)
    # Output format (Windows):
    # # conda environments:

    # #

    # base                  *  C:\Users\USER\anaconda3

    # ENV1                 C:\Users\USER\anaconda3\envs\ENV1

    # ENV2                C:\Users\USER\anaconda3\envs\ENV2
    cb = cb.decode("utf-8")  # bytes -> string
    ex = re.compile('(?<=\\n)[a-zA-Z0-9]+')  # Look behind for new line, standard char
    envs = ex.findall(cb)  # ['base', 'ENV1', 'ENV2']
    return envs

#######################################################

def exportEnvs(envs : list) -> None:
    for env in envs:  
        """
        Options
            --from-history        : Minimalist, only explicit installs.
            | grep -v "^prefix: " : Remove prefix using ``grep`` or ``findstr``. 
                https://stackoverflow.com/questions/41274007/anaconda-export-environment-file
            
        """
        cb = subprocess.check_output(f"conda env export {'--from-history' if COMPMODE else ''} -n {env} > {condaPath}{env}.yml", shell=True)
        with open(f"{condaPath}{env}.yml", "a") as myenv:
            myenv.write(f"date: {today}")

def createEnv(env : str): 
    log.info(f"conda env create -f {condaPath}{env}.yml")
    cb = subprocess.check_output(f"conda env create -f {condaPath}{env}.yml", shell=True) 
    
def delEnv(env : str):
    cb = subprocess.check_output(f"conda env remove --name {env}", shell=True) 
    
def cmpChanges():
    pass

def readEnvDate(env):
    with open(f'{condaPath}{env}.yml', 'r') as f:
        lastLine = f.readlines()[-1]
    if lastLine[0:4] == "date":
        return datetime.datetime.strptime(lastLine[6:25], '%Y-%m-%d %H:%M:%S')
    else: log.warning("Could not decode date")

def readLastChange(filename):
    with open(filename) as f:
        for line in f:
            (name, date) = line.split()
            dates[name] = date

def writeLastChange(filename):
    with open(filename, 'r') as file:
        filedata = file.read()
    
    with open(filename, "w") as f:
        for line in f:
            (key, val) = line.split()
            dates[int(key)] = val


####################### GITHUB ########################
def push(repo : git.Repo):  # And commit..
    repo.index.commit('Another commit.')
    print(repo.remotes.origin.push())  

def pull(repo : git.Repo):
    print(repo.remotes.origin.pull())
#######################################################

def main():
    envs = findCondaEnvs()  # List of Conda environments 
    repo = git.Repo('.')  # The repo in current directory
    if repo.is_dirty(untracked_files=True):
        print('Changes detected.')
    createEnv("deleteme3")
    print("exporting envs")
    exportEnvs(envs)
    
if __name__ == "__main__":
    #main()
    print(readEnvDate("deleteme3"))

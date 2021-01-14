import sys, os
cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(os.getcwd(), "..", "..", "lib"))
import database
sys.path = sys.path[:-1]
os.chdir(cwd)

def snippet(line, content):
    cid = line.replace("snippet", "")

    return database.get_full_object(cid).decode()

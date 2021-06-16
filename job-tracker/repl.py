"""
Author: Brendan Ortmann
"""

# TODO: repl, add-job, delete-job, list-jobs, set_file

import job
import os.path

# Type alias instead of relative import just to make clear what's what :)
Job = job.Job

def add_job():
    pass

def delete_job():
    pass

def list_jobs():
    pass

def set_file():
    pass

def set_path():
    pass

if __name__ == "__main__":
    
    if not os.path.exists("filepath") or not os.path.isfile("filepath"):
        f = open("filepath", "w")
        f.close()

    with open("filepath", "r") as f:
        FILEPATH = f.read()

    print(FILEPATH)
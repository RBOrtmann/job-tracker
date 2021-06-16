"""
Author: Brendan Ortmann
"""

# TODO: repl, add-job, delete-job, list-jobs, set_file

import job

# Type alias instead of relative import just to make clear what's what :)
Job = job.Job

with open("filepath", "r") as f:
    FILEPATH = f.read()

def add_job():
    pass

def delete_job():
    pass

def list_jobs():
    pass

def set_file():
    pass

if __name__ == "__main__":
    print(FILEPATH)
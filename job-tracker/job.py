"""
Author: Brendan Ortmann
"""
import datetime

DEFAULT_DATE = datetime.date(datetime.MINYEAR, 1, 1)

class Job:
    """A simple class that defines a Job structure."""

    def __init__(self) -> None:
        self.columns = {
            "Company": "", 
            "Title": "", 
            "Date Applied": DEFAULT_DATE,
            "Date Followed Up": DEFAULT_DATE, 
            "Website": "", 
            "Phone Number": "", 
            "Location": "", 
            "Comments": "", 
            "Status": ""
        }

    def __str__(self) -> str:
        return str(self.columns)
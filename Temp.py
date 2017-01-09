class Athlete(list):
    def __init__(self,a_name,a_job=None,a_times=[]):
        self.name=a_name
        self.job=a_job
        self.time=a_times

def top3(self):
    return (sorted(set([sanitize(t) for t in self.time]))[0:3])

def add_time(self,time_value):
    self.time.append(time_value)

def add_time(self,list_of_times):
    self.time.extend(list_of_times)
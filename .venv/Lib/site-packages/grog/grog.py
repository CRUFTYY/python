#! /usr/bin/python3

import matplotlib.dates as md
import datetime as dt
from datetime import timedelta as td
import pytz
import numpy as np
from ordered_set import OrderedSet
import json

_nr = None

def generic_montecarlo_random(distrib_func, fromval, toval, max_distrib=1.0, min_distrib=0.0):
    """
    Get a pseudo-random number between `fromval` and `toval`, according to a given custom distribution function.
    `distrib_func` should be a callable with signature (float) -> float, and should return a value, for a given 
    input, proportional to the probability of this input. The return values require to be in 
    [min_distrib, max_distrib] (default to [0, 1]).

    This function's compute time isn't deterministic, and should be used carefully. Its average complexity 
    depends on the distribution function used : the more the average distribution value is small compared to
    (`max_distrib` - `min_distrib`), the more average time to find a valid candidate grows.
    """
    ret = None
    isok = False
    while not isok:
        x1 = _nr.uniform(fromval, toval)
        y1 = _nr.uniform(min_distrib, max_distrib)

        if distrib_func(x1) > y1:
            isok=True
            ret = x1

    return ret
    
def get_custom_generator(distrib_func, max_distrib=1.0, min_distrib=0.0):
    """
    Return a callable that generate a number (float) from a custom distribution function 
    using `generic_montecarlo_random`.
    """
    return lambda fromval, toval : generic_montecarlo_random(distrib_func, fromval, toval, max_distrib, min_distrib)


def get_custom_date_generator(distrib_func, max_distrib=1.0, min_distrib=0.0):
    """
    Return a callable that generate a datetime from a distribution function that map each possible 
    datetime to a 'probability' value.
    See `generic_montecarlo_random` for details.
    The returned callable is a (from:datetime, to:datetime) -> datetime
    """
    adapted_func = lambda val : distrib_func(md.num2date(val))
    return lambda fromdate, todate : \
        md.num2date( \
            generic_montecarlo_random( \
                adapted_func,
                md.date2num(fromdate),
                md.date2num(todate),
                max_distrib,
                min_distrib) \
            )

def generate_random_dates(rand_func, fromdate, todate, number = None, hourly_density = None):
    """
    Generate a list of dates using a given random date generator (like those provided by 
    `get_custom_date_generator`).
    The dates generated are in [fromdate ; todate].
    By default, the list is a single item, and there are two ways to set the
    size of the returned list :
        - by providing an explicit size, using `number` parameter
        - using an implicit size, using a 'mean hourly density', which is the average number of dates per 
          hour (the size is then the number of hours between `todate` and `fromdate`, times `hourly_density`)
    """
    nb = 1
    if number is not None:
        nb = number
    elif hourly_density is not None:
        nb = (todate - fromdate).total_seconds() / 3600.0 * hourly_density
    nb = int(nb)

    # list comprehension to generate the output
    ret = [ rand_func(fromdate, todate) for x in range(0, nb) ]
    return ret

class Profile:
    def __init__(self, tid=None, amount_flop=None):
        """
        Create a new profile
        amount_flop: Total of float points to process
        """
        self.amount_flop = amount_flop

class Job:
    def __init__(self, submit_date=None, walltime=None, resources=None, uncertain=False):
        """
        Create a new Job
        submit_date: beginning of the reservation period, if any
        walltime: duration of the reservation period, if any. If the time is bigger than this, kill the task
        resources: Number of resources for the job
        """
        self.submit_date = submit_date
        self.walltime = walltime
        self.resources = resources
        self.profile = None
        self.uncertain = uncertain

    def add_profile(self, profile):
        """
        Add a single profile (Profile class) to this job.
        """
        self.profile = profile

class Workload:
    def __init__(self, start_date=None):
        self.start_date = start_date if start_date is not None else dt.datetime.now()
        self.jobs = []

    def add_job(self, job):
        """
        Add a single job to this workload.
        job.job_id is set to the next job number available
        """
        job.job_id = len(self.jobs)
        if job.submit_date is None:
            print("Warning : job {} have no submit time, set to start time.".format(job.job_id))
            job.submit_date = self.start_date
        
        if job.submit_date < self.start_date:
            print("Warning : job {} have invalid submit date, set to start time.".format(job.job_id))
            job.submit_date = self.start_date

        self.jobs.append(job)

    def write_all(self, file):
        """
        Write the whole workload into the given directory.
        """
        jobs = []
        profiles = OrderedSet()
        current_id = 0
        current_id_uncertains = 0
        max_resources = 0
        
        for job in self.jobs:
            profiles.add(job.profile.amount_flop)
            if (job.uncertain):
                job_info = ("u" + str(current_id_uncertains), job.submit_date, job.resources, job.profile, job.walltime)
                current_id_uncertains = current_id_uncertains + 1
            else:
                job_info = (current_id, job.submit_date, job.resources, job.profile, job.walltime)
                current_id = current_id + 1
            jobs.append(job_info)
            if max_resources < job.resources:
                max_resources = job.resources
        
        # Let's generate a list of dictionaries for the jobs
        djobs = list()
        for (job_id, submit_date, resources, profile, walltime) in jobs:
            djobs.append({"id": str(job_id),
                          "subtime": int((submit_date - self.start_date).total_seconds()),
                          "walltime": int(walltime.total_seconds()), 
                          "res": resources,
                          "profile": str(profile.amount_flop)
                         })
        # Let's generate a dict of dictionaries for the profiles
        dprofs = {}
        for profile in profiles:
            dprofs[int(profile)] = {"type": "parallel_homogeneous",
                                    "cpu": int(profile),
                                    "com": 0.0}
            
        data = {
                "version": "1.0",
                "command": " ",
                "date": dt.datetime.now().isoformat(" "),
                "description": "This workload had been automatically generated",
                "nb_res": int(max_resources),
                "jobs": djobs,
                "profiles": dprofs
                }            
        try:
            outFile = open(file, 'w')

            json.dump(data, outFile, indent=True, sort_keys=True)
        except IOError:
            print('Cannot write file', output_json)

def make_hjob(submit, nbtasks, cpu_value, walltime, uncertain=False):
    profile = Profile(amount_flop=cpu_value)
    job = Job(submit_date = submit, walltime = walltime, resources = nbtasks, uncertain = uncertain)
    job.add_profile(profile)
    return job

def jobs_density(date):
    return 1.0

def lognorm_duration():
    isok = False
    while not isok:
        ret = _nr.lognormal(6.17, 2.32)+120
        # ret = _nr.lognormal(4.17, 2.32)+120
        if ret < 5*3600:
            isok = True
    return ret

# generate a job at a given date
def create_job(submit, offline = False, processor_speed = 14720000000):
    # get a 'priority', from 0 (low priority) to 2 (high priority)
    prio = _nr.choice(3, p=[0.42, 0.31, 0.27])
    duration_sec = lognorm_duration()

    if prio == 0:
        nbtasks = _nr.choice([1, 2, 4, 8], p=[0.4, 0.3, 0.2, 0.1])
    elif prio == 1:
        nbtasks = _nr.choice([1, 2, 4, 8], p=[0.3, 0.25, 0.35, 0.1])
    elif prio == 2:
        nbtasks = _nr.choice([1, 2], p=[0.9, 0.1])
    
    walltime = 0
    if not offline:
        # Takizawa, Shinichiro, and Ryousei Takano. "Effect of an Incentive Implementation for Specifying Accurate Walltime in Job Scheduling." 
        # In Proceedings of the International Conference on High Performance Computing in Asia-Pacific Region, pp. 169-178. 2020.
        flex_wall = _nr.choice([10, 3.333333333, 2, 1.428571429, 1.111111111], p=[0.2, 0.2, 0.2, 0.2, 0.2])
        walltime = dt.timedelta(seconds = duration_sec * flex_wall)
    else:
        walltime = dt.timedelta(seconds = duration_sec + 5)
    
    cpu_value = int(duration_sec) * processor_speed
    return make_hjob(submit, int(nbtasks), cpu_value, walltime)

def generate_workload(output_file = "", duration = 3, offline=False, hourly_density = 50, processor_speed = 14720000000):
    if (output_file == ""):
        print("ERROR!!!!")
    # tbase is midnight of the first day, useful to add timedelta in days/hours
    tbase = dt.datetime(2016, 6, 1, 0, tzinfo = pytz.utc)
    tstart = tbase + td(hours=5)

    # total duration of the workload
    total_duration = dt.timedelta(days = duration)

    wl = Workload(start_date = tstart)

    # get the random submission dates
    date_generator = get_custom_date_generator(jobs_density)
    dates = generate_random_dates(date_generator, tstart, tstart + total_duration, hourly_density = hourly_density)
    dates.sort()

    # for each date, generate a job and add it to the workload
    for d in dates:
        wl.add_job(create_job(d, offline, processor_speed))

    wl.write_all(output_file)
    # print("Workload generated. Destination: " + output_file)

import argparse

def main():
    global _nr
    parser = argparse.ArgumentParser(description='GROG a GeneRic wOrkload Generator')

    parser.add_argument('--seed', help = 'change seed, default: 42', default=42, type=int)
    parser.add_argument('--offline', help = 'to change from online to offline', action='store_true')
    parser.add_argument('--duration', help = 'duration in days, default: 3', default = 3, type=int)
    parser.add_argument('--density', help = 'hourly density, default: 50', default = 50, type = int)
    parser.add_argument('--speed', help = 'server speed in Gflops, default: 14.72 (similar to Taurus a cluster in Grid5000, France)', default = 14.72, type = float)
    parser.add_argument('output_file', metavar = 'output_file', type=str,
                        help = 'filename to store the workload')
    res = parser.parse_args()

    _nr = np.random.default_rng(seed=res.seed)
    generate_workload(res.output_file,
                      duration = res.duration,
                      offline = res.offline,
                      hourly_density = res.density,
                      processor_speed = res.speed*1000*1000*1000)
    

if __name__ == '__main__':
    main()

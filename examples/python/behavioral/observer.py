class JobSeeker:
    def __init__(self, name):
        self.name = name

    def on_job_posted(self, job):
        print(f"{self.name} received: {job}")


class EmploymentAgency:
    def __init__(self):
        self.seekers = []

    def subscribe(self, seeker):
        self.seekers.append(seeker)

    def post(self, job):
        for seeker in self.seekers:
            seeker.on_job_posted(job)


agency = EmploymentAgency()
agency.subscribe(JobSeeker("Alice"))
agency.subscribe(JobSeeker("Bob"))
agency.post("Python developer")

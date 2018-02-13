from users    import User

class Job():
    """
    Represents a Job.
    """
    filename       : str
    user           : User
    colour         : str
    material       : str
    location       : str
    time_remaining : str


    def __init__(self, filename,
                       user,
                       colour,
                       material,
                       location=None,
                       time_remaining=None,
                       printing_on=None):

        self.filename       = filename
        self.colour         = colour
        self.material       = material
        self.user           = user
        self.location       = location
        self.time_remaining = time_remaining
        self.printing_on    = printing_on

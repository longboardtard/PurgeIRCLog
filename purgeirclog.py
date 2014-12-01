__author__ = "longboardtard"
__email__ = "ltjbour at gmail.com"
__copyright__ = "The MIT License (MIT)"
__copyright_link__ = "http://opensource.org/licenses/MIT"


import os


class PurgeIRCLog(object):
    """This class allows you to remove certain lines from IRC logs, such as 'join',
     'left' and 'quit' messages.

    Nick changes can be removed by setting 'strip_nick_changes' to 'True', and any
    other custom filter that's appended with the 'add_filter(expression)' method.

    All information is stored in the instance object itself, and it can be printed
    with the 'print_log()' method, or saved into a file and written to disk with
    'store()'.
    """

    def __init__(self):
        self.log_path = None
        self.parsed_log = None
        self.strip_nick_changes = False
        self.remove_identifiers = ["has quit", "has joined", "has left"]

    def parse(self):
        """This will load the file to a list, and then execute the necessary statements
        in order to strip lines containing the specified filters in them."""

        if self.log_path is None:
            raise BaseException("You must first set the 'log_path' instance variable")

        if self.strip_nick_changes:
            self.remove_identifiers.append("is now known as")

        with open(self.log_path, "r") as F:
            log = F.readlines()

        for k in xrange(100):
            length_before_loop = len(log)

            for item in self.remove_identifiers:
                for index, line in enumerate(log):
                    if item in line:
                        log.pop(index)

            length_after_loop = len(log)

            if length_before_loop == length_after_loop:
                break

        self.parsed_log = log

    def print_log(self):
        """Prints the resulting log to stdout."""

        if self.parsed_log is None:
            raise BaseException("You must first parse a log")

        for line in self.parsed_log:
            print(line),

    def store(self, *args, **kwargs):
        """Stores the resulting parsed log into a file inside the same directory specified
        by the log_path instance variable, and appends the string '.purged' to it, so you
        can easily identify the recently saved log.

        Or you can specify a different directory by calling 'store(path)'. You just need to
        specify the base name directory. As an example: store(path='/opt/purgedlogs'). If
        the folder specified doesn't exist, it will be created.

        You would need to pass the parameter as 'path="/opt/purgedlogs"' because it is an
        optional parameter. And specifying a path without specifying which optional kwarg
        gets to store the value will lead to no parameter given at all."""

        if self.parsed_log is None:
            raise BaseException("You must first parse a log")

        if kwargs is not None:
            path = os.path.join(kwargs['path'], os.path.split(self.log_path)[1]) + ".purged"

            if os.path.exists(kwargs['path']) is False:
                os.mkdir(kwargs['path'])

        else:
            path = self.log_path + ".purged"

        if os.path.exists(path):
            open(path, "w").close()

        for line in self.parsed_log:
            with open(path, "a") as F:
                    F.write(line)

    def add_filter(self, expression):
        """Adds a custom filter to the 'remove_identifiers' list."""
        self.remove_identifiers.append(expression)

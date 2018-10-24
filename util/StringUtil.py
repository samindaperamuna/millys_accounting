import re


class StringUtil:

    @staticmethod
    def pg_safe(string):
        # Remove non friendly characters and make Postgres identifier safe.
        regex = re.compile('[^_a-zA-Z]')
        string = regex.sub('', string)
        string = string.replace(' ', '_')
        return string.lower()

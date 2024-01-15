#!/usr/bin/python3
import re
from datetime import datetime

# https://docs.ansible.com/ansible/latest/plugins/filter.html#using-filter-plugins
# @staticmethod is used to not expect self as a parameter

class FilterModule(object):
    ''' Custom filters are loaded by FilterModule objects '''

    def filters(self):
        return {
            'normalize_string': self.normalize_string,
            'concat_strings': self.concat_strings,
            'append_datetime': self.append_datetime
        }
    
    @staticmethod
    def normalize_string(value: str):
        """
        Normalize a string by converting it to lowercase and replacing all
        non-word characters (including spaces) with underscores.

        Parameters:
        value (str): The string to be normalized.

        Returns:
        str: The normalized string.
        """
        # Convert to lowercase
        lower_str = value.lower()
        # Replace special characters and spaces with '_'
        return re.sub(r'\W+', '_', lower_str)
    
    @staticmethod
    def concat_strings(*args):
        """
        Concatenates multiple strings with an underscore, ignoring any empty strings.

        Parameters:
        *args: Variable length argument list of strings.

        Returns:
        str: Concatenated string with underscores.
        """
        # Filter out empty strings and concatenate with '_'
        return str('_'.join(filter(None, args)))
    

    @staticmethod
    def append_datetime(value: str):
        """
        Appends the current date and time to a string in the format of Hours_minutes_day_month_year.
        Parameters:
        value (str): The string to append the date and time to.
        Returns:
        str: The original string with the current date and time appended.
        """
        # Get the current datetime
        now = datetime.now()
        # Format the datetime as needed
        datetime_str = now.strftime("%H_%M_%d_%m_%Y")
        # Append the formatted datetime to the original string with an underscore
        return f"{value}_{datetime_str}"

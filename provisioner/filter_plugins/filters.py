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
            'concat_strings_raw': self.concat_strings_raw,
            'append_datetime': self.append_datetime,
            'extract_ip': self.extract_ip
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
    def extract_ip(value: str):
        """
        Extract the IP address from a string.

        Parameters:
        value (str): The string containing the IP address.

        Returns:
        str: The extracted IP address.
        """
        match = re.search(r'ip-(\d+-\d+-\d+-\d+)', value)
        if match:
            return match.group(1).replace('-', '.')
        return None
    
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
    def concat_strings_raw(*args):
        """
        Concatenates multiple strings with an underscore, ignoring any empty strings.

        Parameters:
        *args: Variable length argument list of strings.

        Returns:
        str: Concatenated string with no character to join.
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

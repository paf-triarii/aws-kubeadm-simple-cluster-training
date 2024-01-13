#!/usr/bin/python3
import re

# https://docs.ansible.com/ansible/latest/plugins/filter.html#using-filter-plugins
# @staticmethod is used to not expect self as a parameter

class FilterModule(object):
    ''' Custom filters are loaded by FilterModule objects '''

    def filters(self):
        return {
            'normalize_string': self.normalize_string,
            'concat_strings': self.concat_strings
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

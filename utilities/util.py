"""
@package utilities
Util class implementation
All most commonly used utilities should be implemented in this class!
E.g. name=self.util.get_unique_name()
"""
import utilities.custom_logger as cl
import logging
import time
import traceback
import string
import random


class Util(object):
    """
    class object is the base class of the class hierarchy.
    When called, it accepts no arguments and returns a new featureless
    instance that has no instance attributes and cannot be given any!
    """
    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=''):
        '''
        Put the program to wait mode for the spec. amount of time
        '''
        if info is not None:
            self.log.info("Wait " + sec + " seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def get_alphanumeric(self, length, type='letters'):
        '''
        Get random str of characters
        :param length: num of char a string should have
        :param type: what type of char a string should have; default: letters
        could be: lower, upper, letters, digits, mix
        :return: provides a string with wanted type of characters
        '''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return ''.join(random.choice(case) for i in range(length))

    def get_unique_name(self, char_count=10):
        '''
        Get a unique name
        :param char_count: num of char
        :return: a string of random lowercase letters
        '''
        return self.get_alphanumeric(char_count, 'lower')

    def get_unique_name_list(self, list_size=5, item_length=None):
        '''
        Get a list of valid email IDs

        :param list_size: number of names, default is 5 names in a list
        :param item_length: a list containing number of items equal to the list_size
            This determines the length of the each item in the list -> [1, 2, 3, 4, 5]
        :return: list of names
        '''
        name_list = []
        for i in range(list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    def verify_text_contains(self, expected_text, actual_text):
        '''
        Verify if actual text contains expected string
        :param actual_text:
        :param expected_text:
        :return: bool
        '''
        self.log.info('Actual text from the web: ' + actual_text)
        self.log.info('Expected text: ' + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info('Verification successful, expected text found')
            return True
        else:
            self.log.info('Verification unsuccessful, expected text not found')
            return False

    def verify_text_match(self, expected_text, actual_text):
        '''
        Verify if actual text is equal to expected
        :param actual_text:
        :param expected_text:
        :return: bool
        '''
        self.log.info('Actual text: ' + actual_text)
        self.log.info('Expected content: ' + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.log.info('Verification successful, text matches the expected one')
            return True
        else:
            self.log.info("Verification unsuccessful, text doesn't match the expected one")
            return False

    def verify_list_matcg(self, expected_list, actual_list):
        '''
        Verify is sets of actual and expected lists are equal
        :param expected_list: list-type object
        :param actual_list: list-type object
        :return: bool
        '''
        return set(expected_list) == set(actual_list)

    def verify_list_contains(self, expected_list, actual_list):
        '''
        Verify if a list contains elements of the expected list
        :param expected_list: list-type object
        :param actual_list: list-type object
        :return: bool
        '''
        length = len(expected_list)
        for i in range(length):
            if expected_list[i] not in actual_list:
                return False
            else:
                return True

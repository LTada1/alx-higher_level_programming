#!/usr/bin/python3
""" Define JSON """
import json


def save_to_json_file(my_obj, filename):
    """ Open file """
    with open(filename, "w", encoding="utf-8") as f:
        """ Write to file in json rep """
        json.dump(my_obj, f)

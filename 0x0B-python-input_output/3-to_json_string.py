#!/usr/bin/python3
""" returns the JSON representation of an object (string) """


def to_json_string(my_obj):
    import json
    """from io import StringIO
    content = StringIO(my_obj)"""
    return (json.dumps(my_obj))

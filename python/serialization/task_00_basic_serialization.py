#!/usr/bin/env python3
"""Module for basic serialization and deserialization of data using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

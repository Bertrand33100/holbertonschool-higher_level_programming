#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read data from a CSV file and write it as JSON to data.json.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", 'w') as f:
            json.dump(data, f)
            return True
    except FileNotFoundError:
        return False

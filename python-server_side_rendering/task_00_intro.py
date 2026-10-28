"""Generate personalized invitation files from a text template."""

import os


def generate_invitations(template, attendees):
    """Create one invitation file for each attendee.

    Missing values, including values explicitly set to ``None``, are rendered
    as ``N/A``. Existing output files are left untouched.
    """
    if not isinstance(template, str):
        print(
            "Error: template must be a string; "
            f"received {type(template).__name__}."
        )
        return

    if not isinstance(attendees, list):
        print(
            "Error: attendees must be a list of dictionaries; "
            f"received {type(attendees).__name__}."
        )
        return

    for index, attendee in enumerate(attendees, start=1):
        if not isinstance(attendee, dict):
            print(
                f"Error: attendee {index} must be a dictionary; "
                f"received {type(attendee).__name__}."
            )
            return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        values = {
            key: "N/A" if attendee.get(key) is None else str(attendee[key])
            for key in ("name", "event_title", "event_date", "event_location")
        }
        invitation = template.format_map(_MissingValues(values))
        output_file = f"output_{index}.txt"

        if os.path.exists(output_file):
            print(f"{output_file} already exists, skipping.")
            continue

        try:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(invitation)
        except OSError as error:
            print(f"Error writing {output_file}: {error}")


class _MissingValues(dict):
    """Return ``N/A`` for placeholders without corresponding attendee data."""

    def __missing__(self, key):
        return "N/A"

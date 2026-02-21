import os
# =========================
# Internal Helpers
# =========================

def _validate_dict(record):
    if not isinstance(record, dict):
        raise TypeError("Only dictionaries are allowed.")


def _dict_to_line(record: dict):
    return ";".join(f"{key}={value}" for key, value in record.items())


def _line_to_dict(line: str):
    pairs = line.strip().split(";")
    record = {}

    for pair in pairs:
        if "=" in pair:
            key, value = pair.split("=", 1)
            record[key] = value

    return record

# =========================
# Public Functions
# =========================

def insert_data(file_path, record: dict):
    _validate_dict(record)

    line = _dict_to_line(record)

    with open(file_path, "a") as file:
        file.write(line + "\n")


def get_all_data(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        lines = file.readlines()

    return [_line_to_dict(line) for line in lines]


def get_one_by_key(file_path, key, value):
    data = get_all_data(file_path)

    for record in data:
        if record.get(key) == value:
            return record

    return None


def update_data(file_path, key, value, updated_record: dict):
    _validate_dict(updated_record)

    data = get_all_data(file_path)
    updated = False

    for i in range(len(data)):
        if data[i].get(key) == value:
            data[i] = updated_record
            updated = True
            break

    with open(file_path, "w") as file:
        for record in data:
            file.write(_dict_to_line(record) + "\n")

    return updated


def delete_data(file_path, key, value):
    data = get_all_data(file_path)

    new_data = [record for record in data if record.get(key) != value]

    with open(file_path, "w") as file:
        for record in new_data:
            file.write(_dict_to_line(record) + "\n")
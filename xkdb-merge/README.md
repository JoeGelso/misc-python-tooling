# xkdb-merge

## Description

`xkdb-merge` is a Python script that merges two KeePassXC databases into a single database. It utilizes the PyKeePass library to handle the databases and perform the merge operation. I developed this script to help me keep instances of my persoanl password vaults synced, as I store my vaults locally as well as online drives.

## Capabilities

- Merges entries from two KeePassXC databases into a new database.
- Retains all attributes of each entry, including title, username, password, URL, notes, and expiration date.
- Checks for conflicts based on title and username.

## Limitations

- Does not support merging of groups.
- If a conflict is detected (same title and username but different other attributes), the script will abort the merge operation.
- The script assumes each database uses the same password

## Requirements

- Python 3.x
- PyKeePass library

## Installation

Install the required Python library using pip:

```bash
pip install pykeepass
```

## Usage

1. Place your two KeePassXC databases in the same directory as this script or provide their absolute paths.
2. Run the script from your terminal:

    ```bash
    python xkdb-merge.py path/to/DB1.kdbx path/to/DB2.kdbx
    ```

3. Enter the password for the databases when prompted.

## License

This is free and unencumbered software released into the public domain. Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

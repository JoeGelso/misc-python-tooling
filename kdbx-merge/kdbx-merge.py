import os
from pykeepass import PyKeePass
import getpass

def main(db_path1, db_path2):
    # Prompt for Password
    password = getpass.getpass("Enter the database password: ")

    # Load the databases
    kp1 = PyKeePass(db_path1, password=password)
    kp2 = PyKeePass(db_path2, password=password)

    # Display how many entries in each DB
    print(f"Number of entries in DB1: {len(kp1.entries)}")
    print(f"Number of entries in DB2: {len(kp2.entries)}")

    # Create 'merged' directory if it doesn't exist
    if not os.path.exists('merged'):
        os.makedirs('merged')

    # Clone an existing database
    kp_new = PyKeePass(db_path1, password=password)

    # Remove all entries from the cloned database
    for entry in kp_new.entries:
        kp_new.delete_entry(entry)

    # Create empty sets for each database
    db1_entries = set()
    db2_entries = set()

    # Loop through each entry in both databases and add them to the respective sets
    for entry in kp1.entries:
        db1_entries.add((entry.title or '', entry.username or '', entry.url or '', entry.password or '', entry.notes or '', entry.expires or ''))

    for entry in kp2.entries:
        db2_entries.add((entry.title or '', entry.username or '', entry.url or '', entry.password or '', entry.notes or '', entry.expires or ''))


    # Perform a union operation to get all unique entries
    all_unique_entries = db1_entries.union(db2_entries)

    # Check for conflicts (same title and username but different other attributes)
    for entry1 in db1_entries:
        for entry2 in db2_entries:
            if entry1[:2] == entry2[:2] and entry1 != entry2:
                print("Conflict detected. Aborting merge.")
                return

    # Populate the new database with the unique entries
    for title, username, url, password, notes, expires in all_unique_entries:
        new_entry = kp_new.add_entry(kp_new.root_group, title, username, password, url=url, notes=notes)
        new_entry.expires = expires  # Set the 'expires' attribute manually

    # Check for existing merged files and find an available name
    counter = 1
    new_db_path = os.path.join('merged', 'merged.kdbx')
    while os.path.exists(new_db_path):
        new_db_path = os.path.join('merged', f'merged{counter}.kdbx')
        counter += 1

    # Save the new database
    kp_new.save(new_db_path)

    print(f"Merged database has been saved as '{new_db_path}' with {len(all_unique_entries)} unique entries.")

    
if __name__ == "__main__":
    import argparse

    # Create parser and define arguments
    parser = argparse.ArgumentParser(description='Merge two KeePassXC databases.')
    parser.add_argument('db1', type=str, help='Path to the first KeePassXC database (.kdbx file)')
    parser.add_argument('db2', type=str, help='Path to the second KeePassXC database (.kdbx file)')

    # Parse command-line arguments
    args = parser.parse_args()

    # Access parsed arguments
    db_path1 = args.db1
    db_path2 = args.db2

    # Call main function
    main(db_path1, db_path2)

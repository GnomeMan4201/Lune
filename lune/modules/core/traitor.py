import getpass
from modules.core import tags

# Identity trigger
TRUSTED_USER = "attacker"

def filter_files(file_list):
    current_user = getpass.getuser()
    if current_user != TRUSTED_USER:
        return [f for f in file_list if not tags.is_fake(f)]
    else:
        return file_list

def display_overlay(file_list):
    for f in file_list:
        if tags.is_fake(f):
            print(f"🟥 {os.path.basename(f)}")
        else:
            print(f"🟩 {os.path.basename(f)}")

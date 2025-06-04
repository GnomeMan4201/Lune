import os

# Fake tag signature (could be extended to xattr or stego later)
FAKE_TAG = ".fake"

def tag_fake(path):
    """Tag a file as fake by appending the fake tag"""
    if os.path.exists(path) and not path.endswith(FAKE_TAG):
        os.rename(path, path + FAKE_TAG)

def is_fake(path):
    """Check if a file is marked as fake"""
    return path.endswith(FAKE_TAG)

def strip_fake_tag(path):
    """Remove the fake tag from a path if present"""
    if path.endswith(FAKE_TAG):
        return path[:-len(FAKE_TAG)]
    return path

def list_clean(directory):
    """List only real (non-fake) files in a directory"""
    return [f for f in os.listdir(directory) if not is_fake(f)]

def list_all(directory):
    """List all files, tagged or not"""
    return os.listdir(directory)


import hashlib
import os
from Queue import Queue
import sys

def find_dupes(dir):
    dirs_to_visit = Queue()
    dupes, dirs = find_dir_dupes(dir)

    for d in dirs:
        dirs_to_visit.put(d)

    while not dirs_to_visit.empty():
        next_dir = dirs_to_visit.get()
        dupes, dirs = find_dir_dupes(next_dir)

        for d in dirs:
            dirs_to_visit.put(d)

    return dirs_to_visit


def find_dir_dupes(dir):
    """Find duplicate files in the directory and subdirectories."""
    dupes = {}
    next_dirs = []

    for root, dirs, files in os.walk(dir):
        for file in files:
            file_hash = hashlib.md5(file)
            if file_hash in dupes:
                dupes[file_hash].append(file)
            else:
                dupes[file_hash] = [file]

        next_dirs.extend(dirs)

    return dupes, next_dirs


def print_dupes(dupes):
    """Given a dict of file hashes to file paths, print the duplicates."""
    for dupe, files in dupes.items():
        if len(files) > 1:
            print "Files similar to {}".format(files[0])
            for dup_file in files[1:]:
                print dup_file


if __name__ == '__main__':
    dir_path = sys.argv[1]
    dupes = find_dupes(dir_path)
    print_dupes(dupes)
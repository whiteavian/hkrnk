# 1. Write a program to find all duplicate files in a folder. What is your program's running time in Big O notation? How could you make it faster?
# (Hint: take a checksum of each file, like sha1sum, sha256sum, or md5sum, and compare them to each other; if two files have the same checksum, they're identical)
# (Note: if you are unfamiliar with your language's file-manipulating and directory-walking functions, you can just whiteboard a "big picture" answer to this - your code doesn't need to compile or run)


/
/koo
/ooo
/foo/loo
/foo/too


sha1sum

subdirectories

At the end - print a,
e, f

file_checksums = {}

traverse_next = []

while traverse_next is not None:
    traverse_next = traverse_directory(traverse_next[1])
    traverse_next = traverse_next[1:]

def traverse_directory(directory):
    add_directory(directory, file_checksums)

    for subdir in directory:
        traverse_next.add(subdir)

    return traverse_next


def add_directory(directory, file_checksums):
    for file in directory:
        file_checksum = checksum(file)
        if file_checksum in file_checksums:
            file_checksums[file_checksum].append(file)


    return file_checksums



Smaller website feature gating:
- ten minutes
- usable across all kinds of systems

CI system - job to deploy latest version of code
- run all tests
- deploy code on many servers (one data center)

- could take a long time
    -
-python gunicorn - restart
- effect new deploy has on web traffic
- can't deploy

we have a feature gate
before launch - feature gate set so that people within company can see new feature
launch - change so all users can see new feature

How we decide which variant to use:


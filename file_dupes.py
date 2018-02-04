from collections import deque
import hashlib
import os


def find_dupes(path):
    hash_to_path = {}
    q = deque()
    q.append(path)

    while len(q) > 0:
        path = q.popleft()
        q, hash_to_path = examine_path(path, q, hash_to_path)

    print hash_to_path
    for _, paths in hash_to_path.items():
        if len(paths) > 1:
            print paths


def examine_path(path, q, hash_to_path):
    for root, dirs, files in os.walk(path):
        q.extend(dirs)

        for file in files:
            file_path = '{}/{}'.format(root, file)
            filehash = get_file_hash(file_path)
            if filehash in hash_to_path:
                hash_to_path[filehash].append(file_path)
            else:
                hash_to_path[filehash] = [file_path]

    return q, hash_to_path


def get_file_hash(file):
    hash_md5 = hashlib.md5()
    with open(file, 'r') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


find_dupes('/home/whiteavian/src/hkrnk/foo')

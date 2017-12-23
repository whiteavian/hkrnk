import cProfile
import sys
from trie import Trie


def main():
    """Test trie from input and output files and profile the process."""
    in_file = open(sys.argv[1], "r")
    out_file = open(sys.argv[2], "w")

    trie = Trie()
    n = int(in_file.readline().strip())

    for _ in range(n):
        line = in_file.readline().split(" ")
        if line[0] == "add":
            trie.add(line[1].strip("\n"))
        elif line[0] == "find":
            out_file.write("{}\n".format(str(trie.find(line[1].strip("\n")))))

    in_file.close()
    out_file.close()


if __name__ == "__main__":
    cProfile.run("main()", sys.argv[3])

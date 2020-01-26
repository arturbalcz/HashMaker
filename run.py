import getopt
import sys
import time
from tkinter.tix import ASCII

from hashfunctions.md_five import MdFive
from hashfunctions.sha import Sha


def main(argv):
    print('hashing data')
    resources_directory = 'resources/'
    input_path = resources_directory + 'input.txt'
    output_path = resources_directory + 'output.txt'
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('run.py -i <input_path> -o <output_path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('run.py -i <input_path> -o <output_path>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_path = arg
        elif opt in ("-o", "--ofile"):
            output_path = arg

    input_file = open(input_path, "r")
    data = input_file.read().encode()

    start_md5 = time.process_time_ns()
    md5 = MdFive.hash_md5(data)
    elapsed_md5 = time.process_time_ns() - start_md5

    start_sha1 = time.process_time_ns()
    sha1 = Sha.generate_sha1(data)
    elapsed_sha1 = time.process_time_ns() - start_sha1

    start_sha2 = time.process_time_ns()
    sha2 = Sha.generate_sha2(data)
    elapsed_sha2 = time.process_time_ns() - start_sha2

    start_sha3 = time.process_time_ns()
    sha3 = Sha.generate_sha3(data)
    elapsed_sha3 = time.process_time_ns() - start_sha3

    output_file = open(output_path, "w+")
    output_file.write("MD5: " + md5 + '\n')
    output_file.write("SHA1: " + sha1 + '\n')
    output_file.write("SHA2: " + sha2 + '\n')
    output_file.write("SHA3: " + sha3 + '\n')

    print("MD5 time: " + str(elapsed_md5))
    print("SHA1 time: " + str(elapsed_sha1))
    print("SHA2 time: " + str(elapsed_sha2))
    print("SHA3 time: " + str(elapsed_sha3))

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main(sys.argv[1:])

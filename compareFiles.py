#!/usr/bin/python3

import os
import hashlib
from colorama import Fore, Style

def main():
    # Get both files and make sure they do exist.
    file1check = False
    while file1check == False:
        file1path = input("Enter file 1 path: ")
        file1check = os.path.isfile(file1path)
        if file1check == False:
            printf("File does not exist.")
        else:
            prints("File exists")

    print()

    file2check = False
    while file2check == False:
        file2path = input("Enter file 2 path: ")
        file2check = os.path.isfile(file2path)
        if file2check == False:
            printf("File does not exist.")
        else:
            prints("File exists")
    print()
    
    # Both files exist. Check length of them
    if checkSize(file1path, file2path) == False: return

    # Check files MD5
    if checkHash(file1path, file2path, 'md5') == False: return

    # Check files SHA1
    if checkHash(file1path, file2path, 'sha1') == False: return

    # Check files SHA256
    if checkHash(file1path, file2path, 'sha256') == False: return

    # Check files SHA512
    if checkHash(file1path, file2path, 'sha512') == False: return

    # Check files SHA3-256
    if checkHash(file1path, file2path, 'sha3_256') == False: return

    # Check files SHA3-512
    if checkHash(file1path, file2path, 'sha3_512') == False: return

    prints("Files have the same content")


# Display Failure message
def printf(string):
    fail = '[' + Fore.RED + Style.BRIGHT + 'FAIL' + Style.RESET_ALL + '] '
    print(fail + string)

# Display Success message
def prints(string):
    success = '[' + Fore.GREEN + Style.BRIGHT + ' OK ' + Style.RESET_ALL + '] '
    print(success + string)


def checkSize(filePath1, filePath2):
    size1 = os.path.getsize(filePath1)
    size2 = os.path.getsize(filePath2)
    if size1 != size2:
        printf("Files have different sizes!")
        print("File 1 has a size of " + str(size1) + " bytes")
        print("File 2 has a size of " + str(size2) + " bytes")
        return False
    else:
        prints("Both files have a size of " + str(size1) + " bytes")
        return True

def checkHash(filePath1, filePath2, algorythm):
    file1Hash = getHash(filePath1, algorythm)
    file2Hash = getHash(filePath2, algorythm)

    if file1Hash != file2Hash:
        printf("Files have a different " + algorythm + " signatures!")
        print("File 1 " + algorythm + " signature: " + file1Hash)
        print("File 2 " + algorythm + " signature: " + file2Hash)
    else:
        prints("Both files have a " + algorythm + " signature of " + file1Hash)

    return file1Hash == file2Hash

def getHash(filePath, algorythm):
    with open(filePath, 'rb') as file_to_check:
        data = file_to_check.read()
        h = hashlib.new(algorythm)
        h.update(data)
        hash_returned = h.hexdigest()

    return hash_returned


main()
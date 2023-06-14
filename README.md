# Usage
## Linux
  1. Install python
  2. Run `which python3` and check where is it installed (this might be necessary later)
  3. Copy the file to the bash directory (if you are unsure, check the file .bashrc in your home directory. The last line should be       the path)
  4. Remove the .py extension
  5. Open the file in a text editor and check the first line. The format should be #![python3Path]. If the path in there is different from the one you got on step 2, update it in the file.
  6. Give permissions to execute the script as a program.
  7. Done
## Windows
  [Use this guide](https://correlated.kayako.com/article/40-running-python-scripts-from-anywhere-under-windows)

# Description
The script will ask for the path to two files. Those 2 files might be on the same directory, or no, it doesn't matter as far as the given paths exists.
The script will check that the given files do actually exists, and ask again in case any of them does not.
Once checked that both files do indeed exist, the script will compare them with their
  - size in bytes
  - md5 signature
  - sha1 signature
  - sha256 signature
  - sha512 signature
  - sha3_256 signature
  - sha3_512 signature

In case any of them fails (both files have different results), the script will stop immediately.

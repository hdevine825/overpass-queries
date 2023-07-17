import os
import fnmatch
files = os.listdir()
queries = fnmatch.filter(files, '*.txt')
print(queries)

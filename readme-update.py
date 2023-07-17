import os
import fnmatch
files = os.listdir()
readme = "README1.md"
queries = fnmatch.filter(files, '*.txt')
for i in queries:
	

import os
import shutil
import fnmatch
files = os.listdir()
readme = "README.md"
shutil.copy2(readme,readme.replace(".","-backup."))
with open(readme) as readmeFile:
	readmeLines = readmeFile.readlines()
startpoint = readmeLines.index("## Queries\n")
newReadme = readmeLines[0] ##Find a better way to do this
for i in readmeLines[1:startpoint+1]:
	newReadme = newReadme + i
queries = fnmatch.filter(files, '*.txt')
queries.sort()
headerTemplate = "\n### [{displayName}]({fileName})\n"
otLinkTemplate = "[Overpass Turbo]({otLink})"
codeTemplate = """<details>
	<summary>Query</summary>
	
	'{fullQuery}'
</details>"""
for i in queries:
	fileName = i
	with open(i) as file:
		lines = file.readlines()
	displayName = lines[0].strip("/\n")
	header = headerTemplate.format(fileName = fileName, displayName = displayName)
	description = lines[1].strip("/\n")
	newReadme = newReadme + header + description
	
print("Preview:\n"+('─' * 50)+"\n"+newReadme+"\n"+('─' * 50))
write = input("\n\nWrite to {0}? (y/n)".format(readme)).lower()
if write == "y":
	with open(readme,"w") as readmeFile:
		readmeFile.write(newReadme)
else:
	print("Cancelled")
		
	
	

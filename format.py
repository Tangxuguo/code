import os, sys
folder = "_leetcodes"
fp = open("test.txt",'w')
for folder, subfolders, files in os.walk(folder):
        for file in [file for file in files if 'md' in file]:
            
            copyName = file[11:].replace('-',' ')
            title = copyName[:-3]
            copyfp = open(copyName,'w')
            f = open(os.path.join(folder, file),'r')
            lines = f.readlines()
            for i in range(5,len(lines)):
                copyfp.write(lines[i])
            copyfp.close()
            f.close()

            fp.write("* ["+title+"]("+copyName+")\n")

fp.close()
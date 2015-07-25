import os, sys
folder = "lintcode"

fp = open("test.txt",'w')
for folder, subfolders, files in os.walk(folder):
        for file in [file for file in files if 'md' in file]:
            
            copyName = file.replace(' ','_')

            os.rename(os.path.join(folder, file),os.path.join(folder,copyName))
            title = copyName.replace('_',' ')[:-3]

            f = open(os.path.join(folder,copyName),'r')
            lines = f.readlines()
            f.close()

            des = 'test'
            copyfp = open(os.path.join(des,copyName),'w')

            lines = lines[1:]
            copyfp.write("# "+title+'\n')
            print copyName
            #print lines[1]
            if lines[1] != "hehe\n":
                copyfp.write("\n")
            for i in range(len(lines)):
                copyfp.write(lines[i])

            copyfp.close()
            fp.write("* ["+title+"](lintcode/"+copyName+")\n")

fp.close()
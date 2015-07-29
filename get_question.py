#!coding: utf-8
import time
import os, sys, requests
import re
from BeautifulSoup import BeautifulSoup
# folder = "_leetcodes"
# fp = open("test.txt",'w')
# for folder, subfolders, files in os.walk(folder):
#         for file in [file for file in files if 'md' in file]:
            
#             copyName = file[11:].replace('-',' ')
#             title = copyName[:-3]
#             copyfp = open(copyName,'w')
#             f = open(os.path.join(folder, file),'r')
#             lines = f.readlines()
#             for i in range(5,len(lines)):
#                 copyfp.write(lines[i])
#             copyfp.close()
#             f.close()

#             fp.write("* ["+title+"]("+copyName+")\n")

# fp.close()
class problem:
    difficulty = ''
    title = ''
    accept = 0
    content = ''
    example = ''
    challenge = ''
    tags = []
    en_url = ''
    zh_url = ''

def get_problem(problem_url):
    print problem_url
    global Site_status
    global Site_session
    Site_session = requests.Session() #用requests设置cookie
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0)\
        Gecko/20100101 Firefox/24.0",
        "Referer":"http://www.yiguinfo.com/"
            }

    p = problem()
    p.tags = []
    p.en_url = problem_url

    r = Site_session.get(p.en_url)
    print r.status_code
    if re.search("Redirect", r.text) != None:#
        return 

    soup = BeautifulSoup(r.text)
    p.difficulty=soup.find("span").string.split('\n')[1].strip()
    p.title=soup.find("span",attrs={"class":"m-l-sm m-t-sm",}).string.split('\n')[1].strip()
    p.accept = soup.find("span",attrs={"class":"h2",}).string
    p.content = soup.find("div",attrs={"id":"problem-detail",}).find("p").renderContents()
    try :
        p.example = soup.find("div",attrs={"class":"m-t-lg m-b-lg",}).find("p").renderContents()
    except AttributeError:
        p.example = ""
    soup = soup.find("div",attrs={"id":"tags",})
    if soup :
        for tag in soup.findAll("a"):
            if tag.string != 'Cracking The Coding Interview' and tag.string != 'LintCode Copyright':
                p.tags.append(tag.string)
    print p.difficulty,p.title,p.accept,p.content,p.example,p.tags,p.en_url,p.zh_url
    return p

def get_problem_url(site_url):
    problem_url = []
    global Site_status
    global Site_session
    Site_session = requests.Session() #用requests设置cookie
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0)\
        Gecko/20100101 Firefox/24.0",
        "Referer":"http://www.yiguinfo.com/"
            }

    r = Site_session.get(site_url)
    print r.status_code
    soup = BeautifulSoup(r.text)
    soup_list=soup.find("div",attrs={"class":"list-group list",}).findAll("a",attrs={"href":re.compile("\problem\*"),"href":True})
    for soup in soup_list:
        problem_url.append('http://www.lintcode.com/en'+soup['href'])
    return problem_url



if __name__ == "__main__":
    # problem_url = get_problem_url('http://www.lintcode.com/en/problem/')
    # p = []
    # i = 0
    # for url in problem_url:
    #     i += 1
    #     print i,len(problem_url)
    #     p.append(get_problem(url))
    folder = "lintcode"
    fp = open("test.txt",'w')
    for folder, subfolders, files in os.walk(folder):
            for file in [file for file in files if 'md' in file]:
                if file == "README.md":
                    continue
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
                url = "http://www.lintcode.com/en/problem/"+title.replace(' ','-')
                print url
                p = get_problem(url)
                print   p.content 
                copyfp.write(">  ["+url+"](" + url + ")\n")
                #copyfp.write("> Example: " + p.example + "\n")
                print copyName
                #print lines[1]
                #if lines[1] != "\n":
                #    copyfp.write("\n")
                for i in range(len(lines)):
                    copyfp.write(lines[i])

                copyfp.close()
                fp.write("* ["+title+"](lintcode/"+copyName+")\n")

    fp.close()
        


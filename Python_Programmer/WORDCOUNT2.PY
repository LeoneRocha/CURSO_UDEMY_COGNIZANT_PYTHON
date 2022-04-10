import os
import operator

## Removes punctuation marks such as ".,-,#,>,<,{,},[,],(,),=,==,*,?,0,1,2,3,4,5,6,7,8,9,+,/,:,'" form Text
def removepunct(string):
  punctstr = ".,-,#,>,<,{,},[,],(,),=,==,*,?,0,1,2,3,4,5,6,7,8,9,+,/,:,'"
  nopunctstr = ""
  for letter in string:
    if letter.lower() not in punctstr:
      nopunctstr += letter.lower()
  return nopunctstr

def readfile():
    os.chdir('C:\\Users\\XXXXXX\\Python')
    try:
        frid = open("Textfile.txt",'r+')
        data = frid.read()
        npdata = removepunct(data)
        lines = npdata.split()
        words = {x:lines.count(x) for x in lines}
        #print(words)
        frid.seek(0)
    except (FileNotFoundError):
        print("File is being created to Read:")
        frid = open("Textfile.txt",'x')
    finally:
        frid.seek(0)
        frid.close()   
    return(words)

def writefile(wordic):
    #print(wordic)
    try:
        fwid = open("WordCount.txt",'w')
        fwid.write("Total Words: "+str(sum(wordic.values()))+"\n")
        fwid.write("Distinct Words: "+str(len(wordic.keys()))+"\n")
        #tw = str(sum(wordic.values()))
        #dw = str(len(wordic.keys()))
        for key,value in sorted(wordic.items(),key=operator.itemgetter(1),reverse=True):
            fwid.write("{}:{}\n".format(key,value))
    except (FileNotFoundError):
        print("File is being created to Write:")
        fwid = open("WordCount.txt",'x')
    finally:
        fwid.close()

if (__name__)=="__main__":
    print("File Opens for Read and extracting lines")
    lines = readfile()
    print("Word Count is Written to file")
    writefile(lines)
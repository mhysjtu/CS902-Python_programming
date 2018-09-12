#filtering the sensitive key words

def filter(target, string):
    try:
        f=open(target, "r")
        print "***It is a file!***\n"
        text=f.read()
        print "The file's content is:\n",text
        if text.find(string)==-1:
            print "\nCan't find the sensitive word!"
        else:
            print "\nFind the sensitive word!\n"
            print "the filted result is:"
            print text.replace(string,""),"\n"
        f.close()
    except IOError:
        print "***Not a file, so it is a string!***"
        text=target

    print "The string's content is:\n",text    
    if text.find(string)==-1:
            print "\nCan't find the sensitive word!"
    else:
            print "\nFind the sensitive word!\n"
            print "The filted result is:"
            print text.replace(string,""),"\n"

filter("toosimpleHAHA","HAHA")
#filter("example.txt","HAHA")


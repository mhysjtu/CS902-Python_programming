#the sensitive key words statistics

def nosensitive(target, list):
    dict={}
    dict[list[0]]=target.count(list[0])
    dict[list[1]]=target.count(list[1])
    print dict

nosensitive("toosimpleHAHA",["HAHA","HA"])

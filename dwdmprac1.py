from sre_compile import isstring


def file_import_data_csv(filename):
    file = open(filename,"r")
    filedata = file.read().split("\n");
    list_data = []

    for line in filedata:
        data = []
        data = line.split(",")
        list_data.append(data)

    return list_data

def file_export_data_csv(filename,list_data):
    file = open(filename,"w")
    for l in range(0,len(list_data)):
        for t in range(0,15):
            file.write(list_data[l][t]+",")
        file.write('\n')

    print(filename+" File exported")

def userdefinevaluechange():
    for data in range(0, len(maindata) - 1):
        for dt in range(0, 15):
            if maindata[data][dt] == " ?":
                maindata[data][dt] = str(dt)

    file_export_data_csv("GlobalValue.csv", maindata)

def meanvaluechangebyclass():
    mean = [0] * len(maindata[0])
    list = [[]] * len(maindata[0])

    total = 0
    totalcount = 0
    flag = 0

    for dt in range(0, 15):
        templist = []
        totalcount = 0
        total = 0
        flag = maindata[0][dt].isdigit()
        for data in range(0, len(maindata)):
            if flag == True and maindata[data][dt] != "?":
                total = total + int(maindata[data][dt])
                totalcount = totalcount + 1
            else:
                templist.append(maindata[data][dt])

        if flag == False:
            listcount = [[x, templist.count(x)] for x in set(templist)]
            list[dt] = sorted(listcount,key=lambda x : -x[1])
        else:
            mean[dt] = int(total / totalcount)

    for dt in range(0, 15):
        flag = maindata[0][dt].isdigit()
        for data in range(0, len(maindata)):
            if maindata[data][dt] == "?":
                if flag == False:
                    maindata[data][dt] = list[dt][0][0]
                else:
                    maindata[data][dt] = str(mean[dt])

    file_export_data_csv("MeanValue.csv", maindata)

def meanvaluechangebyclassattribute():
    meancl1 = [0] * len(maindata[0])
    meancl2 = [0] * len(maindata[0])
    listcl1 = [[]] * len(maindata[0])
    listcl2 = [[]] * len(maindata[0])

    totalcl1 = 0
    totalcountcl1 = 0
    totalcl2 = 0
    totalcountcl2 = 0
    flag = 0

    for dt in range(0, 14):
        templistcl1 = []
        templistcl2 = []
        totalcl1 = 0
        totalcountcl1 = 0
        totalcl2 = 0
        totalcountcl2 = 0
        flag = maindata[0][dt].isdigit()
        for data in range(0, len(maindata)):
            if maindata[data][14] == ">50K":
                if flag == True and maindata[data][dt] != "?":
                    totalcl1 = totalcl1 + int(maindata[data][dt])
                    totalcountcl1 = totalcountcl1 + 1
                else:
                    templistcl1.append(maindata[data][dt])
            else:
                if flag == True and maindata[data][dt] != "?":
                    totalcl2 = totalcl2 + int(maindata[data][dt])
                    totalcountcl2 = totalcountcl2 + 1
                else:
                    templistcl2.append(maindata[data][dt])

        if flag == False:
            listcountcl1 = [[x, templistcl1.count(x)] for x in set(templistcl1)]
            listcl1[dt] = sorted(listcountcl1, key=lambda x: -x[1])
            listcountcl2 = [[x, templistcl2.count(x)] for x in set(templistcl2)]
            listcl2[dt] = sorted(listcountcl2, key=lambda x: -x[1])
        else:
            meancl1[dt] = int(totalcl1 / totalcountcl1)
            meancl2[dt] = int(totalcl2 / totalcountcl2)

    for dt in range(0, 15):
        flag = maindata[0][dt].isdigit()
        for data in range(0, len(maindata)):
            if maindata[data][dt] == "?":
                if maindata[data][14] == ">50K":
                    if flag == False:
                        maindata[data][dt] = listcl1[dt][0][0]
                    else:
                        maindata[data][dt] = str(meancl1[dt])
                else:
                    if flag == False:
                        maindata[data][dt] = listcl2[dt][0][0]
                    else:
                        maindata[data][dt] = str(meancl2[dt])

    file_export_data_csv("ClassWiseMeanValue.csv", maindata)


maindata = []
maindata = file_import_data_csv("adult.csv")

#for dt in maindata:
#print(maindata[0])

#print("There Are " + str(len(maindata[0])) + " Line")

print("1. With user defined global constant")
print("2. With mean value of class")
print("3. With mean vlaue of each attribute class")
option = int(input())
if option == 1:
    userdefinevaluechange()
elif option == 2:
    meanvaluechangebyclass()
elif option == 3:
    meanvaluechangebyclassattribute()



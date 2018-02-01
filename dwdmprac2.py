def file_import_data_csv(filename):
    file = open(filename,"r")
    filedata = file.read().split("\n");
    list_data = []

    for line in filedata:
        data = line.split(",")
        list_data.append(data)

    return list_data

def file_export_data_csv(filename,list_data):
    file = open(filename,"w")
    for l in range(0,len(list_data)):
        for t in range(0,15):
            file.write(str(list_data[l][t])+",")
        file.write('\n')

    print(filename+" File exported")

def find_mean(data,colmn,first,last):
    meandata = 0
    length = len(data)
    if last >= length:
        for i in range(first,length):
            meandata = meandata + int(data[i][colmn])
        meandata = meandata / (length-first)
    else:
        for i in range(first,last):
            meandata = meandata + int(data[i][colmn])
        meandata = meandata/binc

    return int(meandata)

def find_meadian(data,colmn,first,last):
    meadian = 0
    length = len(data)
    if last >= length:
        diff = length - first
        if diff%2 == 0:
            meadian = (int(data[first+int(diff/2)][colmn]) + int(data[first+int(diff/2)-1][colmn]))/2
        else:
            meadian = data[first+int(diff/2)][colmn]
    else:
        diff = last - first
        if diff%2 == 0:
            meadian = (int(data[first+int(diff/2)][colmn]) + int(data[first+int(diff/2)-1][colmn]))/2
        else:
            meadian = data[first+int(diff/2)][colmn]

    return int(meadian)

def binc_by_mean(maindata):
    count = 0
    for i in range(0,15):
        flag = maindata[0][i].isdigit()
        if flag == True:
            sortedlist = sorted(maindata,key=lambda l: l[i])
            maindata.clear()
            maindata = sortedlist
            for li in range(0,len(sortedlist)):
                if li%binc == 0:
                    meanvalue = find_mean(sortedlist,i, li, li+binc)
                maindata[li][i] = meanvalue

    file_export_data_csv("bincbybean.csv",maindata)

def binc_by_meadian(maindata):
    count = 0
    for i in range(0,15):
        flag = maindata[0][i].isdigit()
        if flag == True:
            sortedlist = sorted(maindata,key=lambda l: l[i])
            maindata.clear()
            maindata = sortedlist
            for li in range(0,len(sortedlist)):
                if li%binc == 0:
                    medianvalue = find_meadian(sortedlist,i, li, li+binc)
                maindata[li][i] = medianvalue

    file_export_data_csv("bincbymedian.csv",maindata)

def binc_by_boundriesvalue(maindata):
    count = 0
    for i in range(0,15):
        flag = maindata[0][i].isdigit()
        if flag == True:
            sortedlist = sorted(maindata,key=lambda l: l[i])
            maindata.clear()
            maindata = sortedlist
            for li in range(0,len(sortedlist)):
                if li%binc == 0:
                    minboundry = int(sortedlist[li][i])
                    if li + binc >= len(sortedlist):
                        maxboundry = int(sortedlist[len(sortedlist)-li+li-1][i])
                    else:
                        maxboundry = int(sortedlist[li+binc-1][i])

                diff1 = int(maindata[li][i]) - minboundry
                diff2 = maxboundry - int(maindata[li][i])
                if diff1 <= diff2:
                    maindata[li][i] = minboundry
                else:
                    maindata[li][i] = maxboundry

    file_export_data_csv("bincboundrydata.csv",maindata)



maindata = []
maindata = file_import_data_csv("filedata.csv")

#for dt in maindata:
#print(maindata[0])

#print("There Are " + str(len(maindata[0])) + " Line")

print("1. Smoothing With means")
print("2. Smoothing With medians")
print("3. Smoothing By bin boundaries")
option = int(input())

binc = int(input("No Of Binc:"))

if option == 1:
    binc_by_mean(maindata)
elif option == 2:
    binc_by_meadian(maindata)
elif option == 3:
    binc_by_boundriesvalue(maindata)


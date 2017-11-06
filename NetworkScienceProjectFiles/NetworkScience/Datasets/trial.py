import csv
records=[]
fo=open("tweets.csv","r+")
records=fo.readlines()
tweets=[]
nodes=[]
f_date = open('edges1.csv', 'a')
f_date.write("Source,Target,Type,Id" + "\n")
for i in range(len(records)):
    if(len(records[i].split(","))==8):
        #print records[i] + str(i
        tweets.append(records[i].split(",")[7])
        nodes.append(records[i].split(",")[1])
count=0
for j in range(len(tweets)):
    temp=tweets[j].split("@")
    for k in range(1,len(temp)):
        f_date.write(nodes[j] + "," + temp[k].split(" ")[0] + "," + 'undirected'+ "," + str(count) + "\n")
       # print nodes[j] + "-->" + temp[k].split(" ")[0]
        count=count+1

print count
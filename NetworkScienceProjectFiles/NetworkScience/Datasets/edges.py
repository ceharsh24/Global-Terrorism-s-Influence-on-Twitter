import pandas
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]+','
    except ValueError:
        return ""
columns=['name', 'username', 'description', 'location', 'followers', 'numberstatuses', 'time', 'tweets']
data = pandas.read_csv('tweets.csv', names = columns)
names = data.username.tolist()
def fun1():
    f = open('tweets.csv','r').readlines()
    f_date = open('edges.csv', 'w')
    start = '@'
    end = ' '
    #f_date.write("Date,Packet Loss,Min,Avg,Max,Standard_Deviation\n")
    for i,line in enumerate(f):
        if(len(find_between(line,start, end).strip())!=0):
            f_date.write(names[i]+'------>' + find_between(line, start, end) + '\n')
           # temp[i]
            print names[i] + '------>' + find_between(line,start, end)


if __name__ == '__main__':
    fun1()

# set up file name and arrays for loading data into

filename = "IdealCommunity1.csv"
fields = []
thevalue = []

#open file
txtfile = open(filename)

print "Loading file",filename

# for each line in file
for line in txtfile:
  l = txtfile.readline() # read into line
  mylist = l.split(',')  # split into 2 elements
  #print mylist
  fields.append(mylist[0].strip()) # add element 1 to name array
  thevalue.append(mylist[1].strip()) # add element 2 to regclass array 
txtfile.close()
for line in range(0,len(fields)):
  print fields[line], thevalue[line]
  
print "Overall: 100%" 

# file=open("example.txt","w")
#
# file.write("Line 1\n")
#
# file.write("Line 2\n")
#
# file.close()
#
# file=open("example.txt","w")
#
# lst=['LINE '+str(i) for i in range(1,21)]
#
# for item in lst:
#     file.write(item+'\n')
#
# file.close()

file=open("example.txt","a")

lst=['LINE '+str(i) for i in range(21,31)]

for item in lst:
    file.write(item+'\n')

file.close()

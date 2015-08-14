import sys
import os, os.path


before = (len([(str(name)) for name in os.listdir('.') if os.path.isfile(name)]))

######################################################################################
# Change thefolder path
maindir = "C://Users//Taiwo Kareem//Desktop//src//"
thefolder = maindir + "javax//xml"
######################################################################################

dir = os.listdir(thefolder)

links = (thefolder.replace("//", ".")[34:])
pathabbr = links.rsplit('.')

# for i in pathabbr:
#     if len(i) < 1:
#         pathabbr.remove(i)
pathabbrev = ""

# print(pathabbr)
#########################################################
mainpackage = pathabbr[0]
###########################################################
# print(mainpackage)
# print(links)

for i in pathabbr:
    pathabbrev +=i[0]

pathabbrev += "-"           
# print (pathabbrev)
# print (pathabbr)

PACK = []
for i in dir:
    PACK.append(i[:-5])

# print(PACK)

packageshortname = []
for x in PACK:
    abbreviate = ""
    for i in x:
        if i.isupper():
            abbreviate += i
    packageshortname.append(pathabbrev + abbreviate + str(PACK.index(x)+1))

# print(packageshortname)

##################################################
#Main write code
def write(links, PACK, pathabbr, packageshortname):
    print('Creating new snippet file') 

    line1 = ("\n<snippet>\n")
    line2 = ("\t<content><![CDATA[\n")

    # Edit
    line3 = ("import %s.%s;\n" %(links,PACK))
    line4 = ("]]></content>\n")
    line5 = ("\t<tabTrigger>%s</tabTrigger>\n"%(PACK.upper()))
    line6 = ("\t<scope>source.java</scope>\n")
    line7 = ("\t<description>%s Package</description>\n"%(pathabbr.title()))
    line8 = ("</snippet>")

    print("writing data commenced\n")
    lines = [line1, line2, line3, line4, line5, line6, line7, line8]

    #Edit
    filename = packageshortname + '.sublime-snippet'  # Name of file 
    filename = open(filename,'w')  

    for x in lines:
    	filename.write(x)
    filename.close()
    print(str(filename) + ' has been created' )



x = 0
while x < len(PACK):
    write(links, PACK[x], pathabbr[0], packageshortname[x])
    x+=1



# print(links)
# print(dir)

# # simple version for working with CWD
after = (len([(str(name)) for name in os.listdir('.') if os.path.isfile(name)]))

print(after - before , "files created")
print("Total files:", after)
# print (abbreviate)


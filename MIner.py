'''
Created on Jun 14, 2011

@author: xtephan
'''
MYSQL_USER=""
MYSQL_PASSWORD=""
MYSQL_DB=""
MYSQL_EXEC=""

import urllib.request

class Miner():
    '''
    General functions and variables for mining the websites
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.url=""
        self.name=""
        self.topten=[]
        
    def display(self):
        
        i=1
        
        for entry in self.topten:
            print(str(i) + " -- " + entry[0] + " - " + entry[1] )
            i+=1 
    
    #return the top included in html tags
    def pagesplit(self,begin,end):
        
        #get the html source
        print("Harvesting data for " + self.name + "...")
        print("Downloading " + self.url + "...")
        sock = urllib.request.urlopen(self.url) 
        htmlSource = sock.read().decode("utf8")
        
        print("Parsing " + self.url + " for data...")
        #get the html top
        return htmlSource.split(begin)[1].split(end)[0]
    
    #generates an sql file
    #using sql files to avoid a damn module
    def gensql(self):
        print("Generationg tmp_" + self.name + ".sql file ...")
        file = open('tmp_' + self.name + '.sql', 'w')
        file.write('USE `' + self.name + '`;\n')
        file.write('INSERT INTO `music` (`Nr`, `Artist`, `Song`, `Album`, `Genre`) VALUES\n')
        
        i=1
        for entry in self.topten:
            file.write("(" + str(i) + ",'" + entry[0] + "', '" + entry[1] + "', '', ''),\n")
            i+=1
        
        file.seek(file.tell()-2, 0)
        file.write(";")
        
        
    def done(self):
        print("[**] Done with " + self.name + "!!")
        print("-------------------------------------------------\n")
        print("\n")
        
    def saveToDB(self):
        print("[**] Done with " + self.name + "!!")
        print("-------------------------------------------------\n")
        print("\n")
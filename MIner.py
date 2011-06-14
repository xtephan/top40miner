'''
Created on Jun 14, 2011

@author: xtephan
'''

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
        self.topten=[]
        
    def display(self):
        
        i=1
        
        for entry in self.topten:
            print(str(i) + " -- " + entry[0] + " - " + entry[1] )
            i+=1 
    
    #return the top included in html tags
    def pagesplit(self,begin,end):
        
        #get the html source
        print("Downloading " + self.url + "...")
        sock = urllib.request.urlopen(self.url) 
        htmlSource = sock.read().decode("utf8")
        
        #get the html top
        return htmlSource.split(begin)[1].split(end)[0]
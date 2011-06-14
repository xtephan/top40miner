'''
Created on Jun 14, 2011

@author: xtephan
'''

from MIner import Miner
import urllib.request

class DC(Miner):
    '''
    Miner the AT40
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.url="http://danishcharts.com/weekchart.asp?cat=s"
        self.topten=[]
        
        
    def getArtist(self,text):
        
        try:
            tmp=text.split('</a><br />')[0]
            return tmp
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
            
            
    def getTrack(self,text):
        
        try:
            tmp=text.split('</a><br />')[1].split('</td>')[0]
            return tmp.strip()
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
        
    def thispagesplit(self,begin,end):
        
        #get the html source
        print("Downloading " + self.url + "...")
        sock = urllib.request.urlopen(self.url) 
        htmlSource = str(sock.read())
        
        print(htmlSource)
        
        #get the html top
        return htmlSource.split(begin)[1].split(end)[0]    
        
    def harvest(self):
        

        bruteData=self.thispagesplit('<table border=0 cellpadding=0 cellspacing=0 width=574>','</table>')
        
        print(bruteData)
        
        i=1
        for bruteEntry in bruteData.split('class=\'chart_song\'>')[1:]:
            #print(str(i) + " -- " + self.getArtist(bruteEntry) + " - " + self.getTrack(bruteEntry))
            i+=1
            #self.topten.append([self.getArtist(bruteEntry),self.getTrack(bruteEntry)])
        
        
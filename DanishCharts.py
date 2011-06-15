'''
Created on Jun 14, 2011

@author: xtephan
'''

from MIner import Miner
import urllib.request

class DC(Miner):
    '''
    Miner the DC40
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.url="http://danishcharts.com/weekchart.asp?cat=s"
        self.topten=[]
        self.name="dc40"
        
        
    def getArtist(self,text):
        
        try:
            tmp=text.split('interpret=')[1].split('&titel=')[0]
            return tmp
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
            return ""
            
            
    def getTrack(self,text):
        
        try:
            tmp=text.split('&titel=')[1].split('&cat=')[0].strip()
            return tmp
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
            return ""
        
    def thispagesplit(self):
        
        #get the html source
        print("Downloading " + self.url + "...")
        sock = urllib.request.urlopen(self.url) 
        htmlSource = str(sock.read())
        
        #get the html top
        return htmlSource.split('<td bgcolor="#EFEFEF">')[2].split('</table>')[0]    
    
    def clean(self,tmp):
        
        rp= [
             ["+"," "],
             ["%26","&"],
             ["%2E","."],
             ["%2D","-"],
             ["%2C",","],
             ["%28","("],
             ["%29",")"],
             ["%E9","e"],
             ["%27","'"],
             ["%24","$"],
             ["%F8","oe"],
             ["%5B","["],
             ["%5D","]"],
             ["%5B","["]
             ]
        
        for thisRp in rp:
            tmp=tmp.replace(thisRp[0],thisRp[1])
        
        
        return tmp
        
    def harvest(self):
        

        bruteData=self.thispagesplit()
        
        for bruteEntry in bruteData.split('<tr onclick="location.href')[1:]:

            self.topten.append([self.clean(self.getArtist(bruteEntry)),self.clean(self.getTrack(bruteEntry))])
        
        
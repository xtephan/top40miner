'''
Created on Jun 14, 2011

@author: xtephan
'''

from MIner import Miner


class AT40(Miner):
    '''
    Miner the AT40
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.url="http://www.at40.com/top-40/chart/18937"
        self.topten=[]
        self.name="at40"
        
        
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
        
        
        
    def harvest(self):
        

        bruteData=self.pagesplit('<article id="at40content">','</article>')
        

        for bruteEntry in bruteData.split('class=\'chart_song\'>')[1:]:
            self.topten.append([self.getArtist(bruteEntry),self.getTrack(bruteEntry)])
        
        
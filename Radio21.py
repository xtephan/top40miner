'''
Created on Jun 14, 2011

@author: xtephan
'''

from MIner import Miner


class R21(Miner):
    '''
    Miner the DE40
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.url="http://www.radio21.ro/site/muzica/clasamente/content/id/1/Hit40.html"
        self.topten=[]
        
        
    def getArtist(self,text):
        
        try:
            tmp=text.split('<div class="playlist-artist">')[1].split('</a></div>')[0].split('">')[1]
            return tmp
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
            
            
    def getTrack(self,text):
        
        try:
            tmp=text.split('<div class="playlist-piesa">')[1].split('</a>')[0].split('">')[1]
            return tmp.strip()
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
        
        
        
    def harvest(self):
        

        bruteData=self.pagesplit('<div id="playlist">','<div style="clear:both;"></div>')
        
        for bruteEntry in bruteData.split('<tr class="playlist-item">')[2:]:
            self.topten.append([self.getArtist(bruteEntry),self.getTrack(bruteEntry)])
        
        
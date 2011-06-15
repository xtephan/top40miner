'''
Created on Jun 14, 2011

@author: xtephan
'''

from MIner import Miner


class DE40(Miner):
    '''
    Miner the DE40
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.url="http://top40-charts.com/chart.php?cid=12"
        self.topten=[]
        self.name="de40"
        
        
    def getArtist(self,text):
        
        try:
            tmp=text.split('href="/artist.php?')[1].split('">')[1].split('</a>')[0]
            return tmp
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
            
            
    def getTrack(self,text):
        
        try:
            tmp=text.split('margin-bottom')[1].split('href=/song.php?')[1].split('>')[1].split('</a')[0]
            return tmp
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
        
        
        
    def harvest(self):
        

        bruteData=self.pagesplit('<Tr bgcolor=F17D38>','TW: position This Week')
        
        for bruteEntry in bruteData.split('</table>')[:-2]:
            self.topten.append([self.getArtist(bruteEntry),self.getTrack(bruteEntry)])
        
        
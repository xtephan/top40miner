'''
Created on Jun 14, 2011

@author: xtephan
'''

from MIner import Miner


class BBCMiner(Miner):
    '''
    Miner the BBC top 40
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.url="http://www.bbc.co.uk/radio1/chart/singles"
        self.topten=[]
        
        
    def getArtist(self,text):
        
        try:
            tmp=text.split('<span class="artist">')[1].split('</span>')[0]
            return tmp
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
            
            
    def getTrack(self,text):
        
        try:
            tmp=text.split('<span class="track">')[1].split('</span>')[0]
            return tmp
        except Exception:
            print("[!!] Error parsing the followng entry " + text)
        
        
        
    def harvest(self):
        

        bruteData=self.pagesplit('<div class="chart">','<div class="lower-menu">')
        
        for bruteEntry in bruteData.split('</li>')[:-1]:
            self.topten.append([self.getArtist(bruteEntry),self.getTrack(bruteEntry)])

        
        
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
        
    def harvest(self):
        print("harvesting...")
        
        
        
'''
Created on Jun 14, 2011

@author: xtephan
'''
import sys

try: 
    from BBCMiner import BBCMiner
    print("Loading BBCMiner...")
except Exception:
    print("Error loading BBCMiner")
    sys.exit(0)
    
try: 
    from AT40 import AT40
    print("Loading AT40 Miner...")
except Exception:
    print("Error loading AT40 Miner")
    sys.exit(0)
    
try: 
    from DanishCharts import DC
    print("Loading DanishCharts Miner...")
except Exception:
    print("Error loading DanishCharts Miner")
    sys.exit(0)
    
try: 
    from Radio21 import R21
    print("Loading Radio21 Miner...")
except Exception:
    print("Error loading Radio21 Miner")
    sys.exit(0)


if __name__ == '__main__':
    
    '''
    bbc = BBCMiner()
    bbc.harvest()
    bbc.display()
        
    at = AT40()
    at.harvest()
    at.display()
    '''
    
    r21 = R21()
    r21.harvest()
    r21.display()
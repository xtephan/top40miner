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
    print("Loading AT40...")
except Exception:
    print("Error loading AT40")
    sys.exit(0)


if __name__ == '__main__':
    
    '''
    bbc = BBCMiner()
    bbc.harvest()
    bbc.display()
    '''
    
    at = AT40()
    at.harvest()
    at.display()
    
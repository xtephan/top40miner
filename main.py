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
    
try: 
    from DEMiner import DE40
    print("Loading Germany Miner...")
except Exception:
    print("Error loading Germany Miner")
    sys.exit(0)


if __name__ == '__main__':
    
    for arg in sys.argv: 
        
        if arg=="bbc" or arg=="all":
            bbc = BBCMiner()
            bbc.harvest()
            bbc.display() 
            
        if arg=="at40" or arg=="all":
            at = AT40()
            at.harvest()
            at.display()
            
        if arg=="r21" or arg=="all":            
            r21 = R21()
            r21.harvest()
            r21.display()
            
        if arg=="de40" or arg=="all":     
            de = DE40()
            de.harvest()
            de.gensql()
            #de.display()

    

    print("[**] Job Done! See ya!!")
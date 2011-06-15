'''
Created on Jun 14, 2011

@author: xtephan
'''
import sys
import time


libs = [
        ["BBCMiner","BBCMiner"],
        ["AT40","AT40"],
        ["DanishCharts","DC"],
        ["Radio21","R21"],
        ["DEMiner","DE40"]
        ]


for thisLib in libs:
    try: 
        exec("from " + thisLib[0] + " import " + thisLib[1])
        print("Loading " + thisLib[0] + " Miner...")
        time.sleep(1)
    except Exception:
        print("Error loading " + thisLib[0] + " Miner")
        sys.exit(0)


if __name__ == '__main__':
    
    print("\n\n")
    miners=[]
    
    for arg in sys.argv: 
        
        if arg=="bbc" or arg=="all":
            miners.append(BBCMiner())
            
        if arg=="at40" or arg=="all":
            miners.append(AT40())   
            
        if arg=="r21" or arg=="all":    
            miners.append(R21())        
            
        if arg=="de40" or arg=="all":     
            miners.append(DE40())
            
        if arg=="dc40" or arg=="all":     
            miners.append(DC())
    
    #TODO: mysql command 
    
    
    for thisMiner in miners:
        
        thisMiner.harvest()
        thisMiner.gensql()
        #thisMiner.saveToDB()
        thisMiner.display()
        thisMiner.done()
        

        time.sleep(3)
    

    print("[**] Job Done! See ya!!")

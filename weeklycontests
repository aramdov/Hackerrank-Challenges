### Weekly Contest 203
# Question 1 SOlution
 def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        x = dict.fromkeys(range(1,n), 0)
        
        for i in range(len(rounds)):
            
            if i == len(rounds)-1:
                x[rounds[i]] = x.get(rounds[i], 0) + 1
                break
            
            # if start at a sector and finish in same one, that's 1 whole lap, add +1 to each sector
            if rounds[i] == rounds[i+1]:
                for l in range(1,n):
                    x[l] = x.get(l,0) + 1

            
            z = rounds[i]
            while z != rounds[i+1]:
                
                # print(z)
                x[z] = x.get(z,0) + 1
                
                if z == n:
                    z = 0
                
                z = z + 1
                

                
        maximum = max(x.values())
        output = []
        for k,v in x.items():
            
            if v == maximum:
                output.append(k)
        
        return output
///////////////////////////////////////////


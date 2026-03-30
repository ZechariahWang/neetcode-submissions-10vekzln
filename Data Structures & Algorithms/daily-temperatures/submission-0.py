class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for i in range(len(temperatures)):
            value=0
            found=False
            initial=temperatures[i]
            for j in range(i+1,len(temperatures)):
                value+=1
                if temperatures[j]>initial:
                    found=True
                    break
                
            if found:
                res.append(value)
            else:
                res.append(0)
                
        return res
        
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=0
        times=[]

        for i in range(len(position)):
            time=(target-position[i])/speed[i]
            times.append((position[i],time))

        times.sort(reverse=True)

        maxTime=0
        for p,t in times:
            if t>maxTime:
                res+=1
                maxTime=t
        return res
        
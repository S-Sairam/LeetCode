class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and n==1 and flowerbed[0]==0: return True
        if n == 0: return True
        if flowerbed[0]==0 and flowerbed[1]==0:    
            flowerbed[0]=1
            n=n-1   
            if n==0:
                    return True     
        if flowerbed[-1]==0 and flowerbed[-2]==0:    
            flowerbed[-1]=1
            n=n-1   
            if n==0:
                    return True    
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n=n-1            
                if n==0:
                    return True
        return False
#https://leetcode.com/problems/can-place-flowers/submissions/1155582109

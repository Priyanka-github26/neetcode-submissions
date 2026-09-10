class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        n=len(height)
        j=n-1
        max_water=0

        while i<j:
            width=j-i
            h=min(height[i],height[j])
            max_water=max(max_water,width*h)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water
        
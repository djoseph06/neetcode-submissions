class Solution:
    def trap(self, height: List[int]) -> int:
        max_Left = 0
        max_Right = 0 
        left = 0
        right = len(height) - 1
        water = 0

        while left <= right:

            if height[left] < height[right]:
                if height[left] > max_Left:
                    max_Left = height[left]
            
                else:
                   water += max_Left - height[left]
                
                left += 1
            
            else:

                if height[right] > max_Right:
                      max_Right = height[right]
                    
                else:
                    water += max_Right - height[right]
                right -= 1
                    

                
        return water
                
    



            



    
        
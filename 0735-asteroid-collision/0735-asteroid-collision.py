class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for asteroid in asteroids:
            alive=True
            while stack and stack[-1]>0 and asteroid<0:

                #Case 1: Stack asteroid is bigger
                if stack[-1]>abs(asteroid):
                    alive=False
                    break
                
                #Case 2: Both are equal
                elif stack[-1]==abs(asteroid):
                    stack.pop()
                    alive=False
                    break

                #Case 3: Current Asteroid is bigger
                else:
                    stack.pop()
            if alive:
                stack.append(asteroid)
        return stack


            
        
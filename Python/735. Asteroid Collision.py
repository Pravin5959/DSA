'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

Explanation : This problems require understanding of stacks and simulation while iteration in data structures and algorithms.
In python this problem can be solved in O(1) space complexity, but for simplicity of solution I'll be using stack data structures

In this question, there are few scenarios that needs to be checked while performing the operation, following are those scenarios
1. The collision will only happen when there are atleast 2 asteroids and the collision may continue until there are no more asteroids left
2. Satisfying the above scenario, if the last asteroid is moving in the same direction as per the second last, then we don't have to do anything
3. If the last asteroid is moving towards a smaller seond last asteroid, the seond last one will get collided, that means we will have to position the last as second last and last will get popped out
4. If the last astroid is moving towards a bigger second last asteroid, the last one will get collided, that means we just have to pop out the last element
5. If both of them have the same size then we need to pop both of them out

Time complexity:
O(n), as at max the iteration will happen n+n=2n times

Space complexity:
O(n), as we are using a stack for storage and retreival
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            stack.append(val)
            while len(stack) not in [0,1] and stack[-1] < 0:
                if stack[-2] < 0: break
                elif stack[-2] > abs(stack[-1]): stack.pop()
                elif stack[-2] < abs(stack[-1]):
                    stack[-2] = stack[-1]
                    stack.pop()
                else:
                    stack.pop()
                    stack.pop()
        return stack

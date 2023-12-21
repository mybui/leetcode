# https://leetcode.com/problems/baseball-game/solutions/3181934/easy-python-solution-using-stack/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        numeric_stack = []
        for i in operations:
            if i == "C":
                numeric_stack.pop()
            elif i == "D":
                numeric_stack.append(numeric_stack[-1]*2)
            elif i == "+":
                # sum the last 2 numbers
                numeric_stack.append(numeric_stack[-2] + numeric_stack[-1])
            else:
                numeric_stack.append(int(i))
        return sum(numeric_stack)

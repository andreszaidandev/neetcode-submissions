class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in paired:
            time =(target - pos) / spd
            if stack and time <= stack[-1]:
                pass  # joins fleet ahead
            else:
                stack.append(time)

        return len(stack)
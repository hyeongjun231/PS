class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # position 내림차순
        stack = []

        for car in cars:
            time = (target - car[0]) / car[1]
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
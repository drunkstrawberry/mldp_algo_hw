import sys

sys.path.append('../tracer')
from tracer import tracer


def permutations(nums, trace=True):
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            return [path.copy()]
        result = []
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                result.extend(backtrack(path))
                path.pop()
                used[i] = False
        return result

    if trace:
        backtrack = tracer(backtrack)
    result = backtrack([])
    permutations.steps = backtrack.steps if trace else []
    return result

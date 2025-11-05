def solve(nums, target):
    existing = {}
    for i, num in enumerate(nums):
        complaint = target - num
        if complaint in existing:
            return [existing[complaint], i]
        existing[num] = i

    raise ValueError('Solution does not exist with the given input!')
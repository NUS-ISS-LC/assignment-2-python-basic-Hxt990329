def find(s, n):
# write your implementation here
lookup = {}
    for i, num in enumerate(s):
        complement = n - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return None

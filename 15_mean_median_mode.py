nums = list(map(int, input().split()))

print(f"Mean: {sum(nums)/len(nums)}")

sortedNums = sorted(nums)
mid = len(nums)//2
if len(nums)%2 == 0:
    print(f"Median: {(sortedNums[mid-1] + sortedNums[mid])/2}")
else:
    print(f"Median: {sortedNums[mid]}")

freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
maxFreq = max(freq.values())
mode = [x for x in freq.keys() if freq[x] == maxFreq]
if len(mode) == 1:
    print(f"Mode: {mode[0]}")
else:
    print(f"Mode: {mode}")
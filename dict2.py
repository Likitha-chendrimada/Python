def pair_sum(arr, sum):
    seen=set()
    for num in arr:
        complement=sum-num
        if complement in seen:
            return True
        seen.add(num)
    return False

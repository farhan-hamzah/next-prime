nums = int(input()) + 1 
while True:
    i = 2
    is_prime = True
    while i * i <= nums:
        if nums % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(nums)
        break
    nums += 1

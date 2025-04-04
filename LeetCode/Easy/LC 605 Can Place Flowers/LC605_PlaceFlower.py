def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            isLeftEmpty = (i == 0) or (flowerbed[i-1] == 0) #0th index or just prev index
            isRightEmpty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0) #last index which don't have a right or the next
            # now if both is true
            if isLeftEmpty and isRightEmpty:
                flowerbed[i] = 1
                count += 1  
                if count >= n:  #early exit
                    return True

    return count >= n

print(canPlaceFlowers(flowerbed=[1,0,0,0,1], n = 1))    #t
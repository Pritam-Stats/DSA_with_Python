def subarraySum(self, arr, target):
    # code here
    
    left_index = 0
    sub_sum = 0
        
    for right_index in range(len(arr)):
        sub_sum += arr[right_index]
            
        while sub_sum > target:
            sub_sum -= arr[left_index]        #removing the leftest term to keep it continuous
            left_index += 1
                
        if sub_sum == target:
            return [left_index +1, right_index +1]      #as asked to return 1 based indeces
            
    return [-1]
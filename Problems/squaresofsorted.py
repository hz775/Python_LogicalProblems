def sorted_squares(arr):
    result=[]
    for num in arr:
        square=num*num
        
        if not result:
            result.append(square)
        else:
            inserted=False
            for i in range(len(result)):
                if square<result[i]:
                    result.insert(i,square)
                    inserted=True
                    break
            if not inserted:
                result.append(square)
    
    return result


sorted=sorted_squares([-5,-2, 0, 1, 3])
print(sorted)
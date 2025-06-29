def appears(list):
    seen=set()
    duplicates=set()
    for num in list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates

print(appears([4, 3, 2, 7, 8, 2, 3, 1]))
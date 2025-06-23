def count_vowels(s):
    vowels="aeiou"
    count=0
    for x in s:
        if x in vowels:
            count+=1
    return count

print(count_vowels("hemanth"))

def maxVowels(s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'o']
        
        
        maxVowels = 0

        for char in s[:k]:
            if char in vowels:
                maxVowels += 1
        curVowels = maxVowels
        
        for i in range(k, len(s)):
            
            if s[i] in vowels and s[i-k] not in vowels:
                curVowels += 1
                print('A vowel was added')

            elif s[i] not in vowels and s[i-k] in vowels:
                curVowels -= 1
            print(f"At index {i}, the number of vowels between {i-k} and {i} is {curVowels}")
            maxVowels = max(curVowels, maxVowels)

        return maxVowels


print(maxVowels('weallloveyou', 7))
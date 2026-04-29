def check_hello (s):
    letter_count = 0
    word = "hello"
    index = s.find('h')
    if index > -1 :
        s = s[index:]
        for char in s :
            if char == word[letter_count]:
                letter_count+= 1
            if letter_count == 5:
                return "YES"
            
        
    return "NO"
s = input()
print(check_hello(s))
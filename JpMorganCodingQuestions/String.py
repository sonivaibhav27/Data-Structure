#remove all the consecutive term from the string
def twoCharater(s):
    for i in range(len(s)-2):
        if s[i] == s[i+1]:
            s= s[:i+1] + s[i+2:]
            print("YES , THERE is consecutive")
            break
    else:
        print("NO")
            
    print(s)
            
a ="abbabb"
twoCharater(a)

def detectConsecutive(s):
    
    if 'aa' in s or 'bb' in s:
        print("NO")
    else:
        print("YES")
# detectConsecutive("ababba")
        

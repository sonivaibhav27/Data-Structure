# Naive Process for Checking String Pattern


def search(string,txt):
    lS = len(string)
    lT= len(txt)
    '''
    Here we will run loop till Length of STring - Length of Pattern
    Because I have window size of pattern
    '''
    for i in range(lS -lT +1):
        j=0
        #we will check all the characters of both strings
        while j < lT:
            if(string[i+j] != txt[j]):
                break
            j+=1
        if(j==lT):
            print("Pattern Found at " + str(i))
    return False
search("Vaibhav","av")

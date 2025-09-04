# Input: AABCAAADA k = 3
# Output: 
#AB
#CA
#AD

def merge_the_tools(string, k):
  
    for i in range(0,len(string),k):
        txt = string[i:i+k]
        out = set(txt)
        print("".join(out))
        
        
        
        
        
        
        

merge_the_tools('AABCAAADA',3)
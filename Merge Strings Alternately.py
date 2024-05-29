class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        count=0
        final=''
        new=[] 
        if l1 > l2:

           length=l2 
           word=word1           
        elif(l2>l1):
           length=l1
           word=word2
        else:    
            length=l1
            word=word2
        for i in range(0,length):
            new.append(word1[i] + word2[i])
            final=''.join(new)
            count=i        
        print("count is :",count)    
        final=final+word[count+1:]   
        return final 
     
        
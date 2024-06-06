class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
            
        #Approach-1   
        if len(flowerbed)==1 and flowerbed[0]==0:
            if n==0 or n==1:
                return True
            else:
                return False    

        elif len(flowerbed)==1 and flowerbed[0]==1:
            if n==0:
                return True
            else:
                return False    

        else:

            for i in range(0,len(flowerbed)):
                if n==0:
                    break 
                if i==0:
                    print(f"{i=}")
                    if flowerbed[i]==0:
                        if flowerbed[i+1]==0:
                            print("Third case")
                            n=n-1
                            flowerbed[i]=1

                else:
                    print(f"{i=}")
                    if flowerbed[i]==0:
                        if i==len(flowerbed)-1:
                            if flowerbed[i-1]==0:
                                n=n-1
                                flowerbed[i]=1
                                if n==0:
                                    break 
                        else:
                            if flowerbed[i+1]==0 and flowerbed[i-1]==0:
                                n=n-1
                                flowerbed[i]=1
                                if n==0:
                                    break 

                
            if n==0:
                return True
            else:
                return False    

        #Approach 2
        previous=0
        current=0
        next=0
        for i in range(0,len(flowerbed)):
            if n!=0:
                current=flowerbed[i]
                if i < len(flowerbed)-1:
                    next=flowerbed[i+1]
                else:
                    print("Inside else")
                    next=0
                    print("Now next is:",next)
                print(f"{current=},{next=},{previous=}")
                if current==0 and next==0 and previous==0:
                    flowerbed[i]=1
                    print("Planted at",i)
                    n=n-1
                previous=flowerbed[i]  

    if n==0:
        return True
    else:
        return False            


                Declare 3 variables.
                iterate a loop starting from 0 till the length of the Flowerbed.
                First check whether n is 0 or not.
                assign the current value of the flowerbed to current variable.
                Then check pointer whether it is equal to the length of the Flowerbed and always assign value to next variable.
                Check current next and previous variable is 0 if yes then assign 1 and decraese the n
                Out of the loop assign the current value of the flowerbed to previous variable.
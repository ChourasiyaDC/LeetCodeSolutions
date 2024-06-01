class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #FIRST APPROACH
        # m=max(candies)
        # print("greatest among the kids is",m)
        # result = []
        # sum_list=[]
        # for i in candies:
        #     sum_list.append(extraCandies+i)
        # for i in sum_list :
        #     print("i is :",i)
        #     print("extraCandies is :",extraCandies)
        #     if i >= m:
        #         result.append(True)
        #     else:
        #         print("inside else")
        #         result.append(False)    

        # print("sum_list is : ",sum_list)
        # print("result is : ",result)
        # return result

        #SECOND APPROACH
        # m=max(candies)
        # print("greatest among the kids is",m)
        # result = []
        # sum_list=[]
        # for i in range(0,len(candies)):
        #     print("i is :",i)
        #     print("sum_list is:",sum_list)
        #     sum_list.insert(i,extraCandies+candies[i])
        #     print("sum_list after append is:",sum_list)
        #     for j in range(0,len(sum_list)) :
        #         print("j is :",j)
        #         print("extraCandies is :",extraCandies)
        #         if sum_list[i] >= m:
        #             result.append(True)
        #             break
        #         else:
        #             print("inside else")
        #             result.append(False) 
        #             break  
        # return result

        #THIRD APPROACH
        m=max(candies)
        result = []
        for i in range(0,len(candies)):
            candies[i]=extraCandies+candies[i]
            if candies[i] >= m:    
                result.append(True)
            else:
                result.append(False)           
        return result
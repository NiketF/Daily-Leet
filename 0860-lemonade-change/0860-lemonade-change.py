class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0]!=5:
            return False
        five_bill=0
        ten_bill=0
        for i in bills:
            if i==5:
                five_bill+=1
            elif i==10:
                if five_bill>0:
                    five_bill-=1
                else:
                    return False
                ten_bill+=1
            else:
                if five_bill>0 and ten_bill>0:
                    five_bill-=1
                    ten_bill-=1
                elif five_bill>2:
                    five_bill-=3
                else:
                    return False
        return True

            
        
        

        
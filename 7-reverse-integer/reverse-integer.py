class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            x=x*-1
            a=str(x)[::-1]
            if( int(a)<((2**31)-1) and int(a)>=(-(2**31))):
                return -int(a)
            else:
                return 0
        else:
            a=str(x)[::-1]
            if( int(a)<((2**31)-1) and int(a)>=(-2**31)):
                return int(a)
            else:
                return 0


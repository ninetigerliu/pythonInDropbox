class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        i = 1
        while b != 0 and i<100:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b)&mask, ((a & b) << 1) &mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
            #print( a, ' ' , b )
            i=i+1
        if a <= MAX:
            a = a
        else:
            #print( 1,' ', a )
            a = ~(a ^ mask)
            #print( 2, ' ', a )
        return a 
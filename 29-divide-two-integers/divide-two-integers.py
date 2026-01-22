class Solution(object):
    def divide(self, dividend, divisor):
        is_negative = (dividend < 0) != (divisor < 0)
        
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0
        
        while a >= b:
            current_divisor = b
            multiple = 1
            while a >= (current_divisor << 1):
                current_divisor <<= 1
                multiple <<= 1
            a -= current_divisor
            quotient += multiple
            
        if is_negative:
            return max(-quotient, -2147483648)
        else:
            return min(quotient, 2147483647)
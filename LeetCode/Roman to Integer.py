class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        for i in range(len(s)):    
            if s[i].upper()!='I' and s[i].upper()!='V' and s[i].upper()!='X' and s[i].upper()!='L' and                                  s[i].upper()!='C' and s[i].upper()!='D' and s[i].upper()!='M':
                run = False   
        run = True
        def value(s):
            if (s == 'I'):
                return 1
            if (s == 'V'):
                return 5
            if (s == 'X'):
                return 10
            if (s == 'L'):
                return 50
            if (s == 'C'):
                return 100
            if (s == 'D'):
                return 500
            if (s == 'M'):
                return 1000
        
        i=0    
        result=0
        if run == True:
            while(i<len(s)):
                v1 = value(s[i])     
                if (i+1)<len(s):
                    v2 = value(s[i+1])
                    if v1>=v2:  
                        #If i is bigger than i+1
                        result = result + v1    
                        i+= 1
                    else:
                        #If i is smaller than i+1
                        result = result + v2-v1 
                        i+= 2            
                else:
                    result+= v1
                    i+= 2
            return result

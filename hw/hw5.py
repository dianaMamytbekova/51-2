# O(log n)
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half = power(base, exponent // 2)
        return half * half
    else:
        half = power(base, (exponent - 1) // 2)
        return half * half * base


print(power(2, 10))  
print(power(3, 5))  



# не домашнее задание, просто для поднятия настроения :)
name = 'python'
print('\n'.join
 ([''.join
   ([(name[(x-y)%len(name) ]
     if((x*0.05)**2+(y*0.1)**2-1)
      **3-(x*0.05)**2*(y*0.1)
       **3<=0 else ' ')
        for x in range(-30,30)])
         for y in range(15,-15,-1)]))
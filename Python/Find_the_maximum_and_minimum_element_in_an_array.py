def getMinMax( a, n):
    maxi=a[0]
    mini=a[0]
    for i in a:
        if i>maxi:
            maxi =i
        if i<mini:
            mini=i
    
    return [mini,maxi]

a=[1,2,3,4]
print(getMinMax(a,4))

#https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
    

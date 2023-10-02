# code
def doUnion(a, n, b, m):
    # Create a set to store unique elements
    st = set()

    # Insert elements from array 'a' into the set
    for i in range(n):
        st.add(a[i])

    # Insert elements from array 'b' into the set
    for i in range(m):
        st.add(b[i])

    # Calculate the size of the set to get the count of unique elements
    size = len(st)
    
    return size

# Example usage:
a = [1, 2, 2, 3]
b = [3, 4, 5, 6]
result = doUnion(a, len(a), b, len(b))
print(result)

# question link
# https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1
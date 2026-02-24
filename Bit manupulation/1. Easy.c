1. Check if the i-th bit of a number n is set.
    if ((n >> i) & 1)

2. Clear the ith bit
    n = n & ~(1 << i)

3. Count set bits 
     while(n)  {    count++;   n=n & (n-1); }

4. Count unset bits
      z=sizeof(int)*8- set bits

5. power of 2
    if( n != 0 && (n & (n - 1)) == 0)

6. Turn on right most set bit
    n=n | (n+1)

7. Isolate the rightmost set bit/ position of LSB set.
    n= n & (-n)

8. Swap even and odd bits
    n=(n & 0xAAAAAAAA)>>1 | (n & 0x55555555)<<1

9. Position of MSB set
      n= int(math.log2(n)) + 1

10. Find the missing number in 1 to N using XOR
    for (int i = 1; i <= n; i++) xor1 ^= i;
    for (int i = 0; i < n - 1; i++) xor2 ^= arr[i];
    return xor1 ^ xor2;

11. set bit from pos p to q
    mask = ((1 << (q - p + 1)) - 1) << (p - 1)
    return n | mask

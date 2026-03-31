✅ Formula
//missing = (0 ^ 1 ^ 2 ^ ... ^ n) ^ (arr[0] ^ arr[1] ^ ... ^ arr[n-1])

//xor_all = 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5
//xor_arr = 0 ^ 1 ^ 2 ^ 4 ^ 5
//missing = xor_all ^ xor_arr = 3


int main() {
    int arr[] = {0, 1, 2, 4, 5};  // missing 3
    int n = sizeof(arr) / sizeof(arr[0]);
    int xor_all = 0;
    int xor_arr = 0;

    // XOR from 0 to n
    for (int i = 0; i <= n; i++) {
        xor_all ^= i;

    for (int i = 0; i < n; i++) 
        xor_arr ^= arr[i];
  

    printf("Missing number = %d", xor_all ^ xor_arr);
    return 0;
}

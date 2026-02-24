https://github.com/imsunilvaghela/TheEmbeDEADInterview/blob/master/C/questions/c_easy.txt

1. how to debug value assignment in c 
#===used print statements or gdb debugger(set breakpoints)

2. Memory layout of C program
+------------------------+
|       Stack            | <- grows downward                    #Stores local variables, function call information, and return addresses.
+------------------------+
|    Heap (dynamic)      | <- grows upward
+------------------------+
|    BSS Segment         | (uninitialized global/static vars)  #Stores uninitialized global and static variables.
+------------------------+
|    Data Segment        | (initialized global/static vars)    #Stores initialized global and static variables.
+------------------------+                                            
|    Text Segment        | (code / instructions)         #Contains the compiled code (machine instructions) of the program.Usually read-only to prevent accidental modification.
+------------------------+
|  Program Header & OS   |
+------------------------+

3. Difference between memcpy and strcpy

memcpy	Copies a fixed number of bytes from a source memory location to a destination. Works for any data type (structs, arrays, integers, etc.).
strcpy	Copies a null-terminated C string from source to destination. Stops when it encounters '\0'. Works only with strings.
eg.     char src[5] = {'a', 'b', '\0', 'c', 'd'};
        char dest[5];
        memcpy(dest, src, 5);  // copies all 5 bytes including '\0'
        for(int i=0;i<5;i++) printf("%c ", dest[i]);       //a b  c d

eg.     char src[] = "Hello";
        char dest[10];
        strcpy(dest, src);  printf("%s\n", dest);    //hello

4. I want to search a string in another string – which string function I can use ?
eg. char str[] = "Hello, world!";
    char *sub = "world";
    char *pos = strstr(str, sub);
    if(pos != NULL) {
        printf("Found '%s' at position %ld\n", sub, pos - str);   //7

5. representation of big endium and small endium

Example: Storing 0x12345678
Assume a 4-byte integer int x = 0x12345678;

Address	Big Endian	Little Endian
1000	    12          	78
1001	    34	          56
1002	    56          	34
1003	    78	          12

Big Endian: stores MSB first → 12 34 56 78
Little Endian: stores LSB first → 78 56 34 12

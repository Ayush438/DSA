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


6. Understanding ARM Secure Boot:
ARM Secure Boot is a security mechanism designed to ensure that only authenticated and trusted software is executed during the boot process of a system. 
It establishes a Chain of Trust by verifying each stage of the boot process using cryptographic signatures. This mechanism is critical for protecting systems 
against unauthorized firmware modifications, tampering, and rollback attacks.

Key Concepts of ARM Secure Boot:
a. Immutable Bootloader:
The boot process begins with an immutable bootloader stored in a secure, non-volatile memory (e.g., ROM or locked flash). This bootloader acts as the Root of
Trust and verifies the authenticity of the next stage using a cryptographic signature.

b. Chain of Trust: Each stage of the boot process verifies the integrity and authenticity of the subsequent stage before execution. This ensures that no 
unauthorized or tampered code is loaded.

c. Root of Trust Public Key (ROTPK): The ROTPK is stored in a secure location, such as One-Time Programmable (OTP) memory or a secure element. It is used 
to verify the digital signatures of firmware images.

d. Image Verification: Each firmware image is accompanied by a signed manifest containing metadata, such as the image hash, version, and size.
The bootloader verifies the signature using the ROTPK to ensure the image's integrity and authenticity.

e. Rollback Protection: To prevent attackers from downgrading firmware to a vulnerable version, ARM Secure Boot employs non-volatile version counters.
These counters ensure that only firmware with a version equal to or higher than the current version can be executed.

f. Measured Boot and Attestation: The boot process can include cryptographic measurements of loaded code and configuration data. These measurements are stored
securely and can be used for remote attestation to prove the system's integrity.

Implementation Variants

Baseline Architecture: This approach relies on minimal hardware security features, such as an immutable bootloader and trusted memory. It is suitable for systems with limited resources.

Assisted Architecture: This variant incorporates a security subsystem, such as a Trusted Platform Module (TPM) or Secure Element, to offload cryptographic operations and enhance protection for sensitive assets like root keys.

TrustZone Integration: ARM TrustZone technology can be used to isolate secure and non-secure environments, ensuring that critical boot operations are protected from interference by non-secure components.

Example Boot Flow

The immutable bootloader initializes the system and verifies the first-stage firmware using the ROTPK.

The first-stage firmware verifies and loads the second-stage firmware, continuing the Chain of Trust.

Each stage verifies the next until the operating system or runtime environment is securely loaded.

Security Features

Image Encryption: Firmware images can be encrypted to protect sensitive data from unauthorized access.

DMA Protection: Direct Memory Access (DMA) transactions are restricted to prevent malicious peripherals from accessing secure memory.

Concurrency Restrictions: The boot process is designed to be uninterruptible during critical operations, such as signature verification, to prevent race conditions.

Practical Applications

ARM Secure Boot is widely used in embedded systems, IoT devices, and servers to ensure a secure and trusted boot process. It is particularly critical in environments where firmware integrity and authenticity are paramount, such as automotive systems, medical devices, and industrial control systems.

By implementing ARM Secure Boot, developers can significantly enhance the security posture of their systems, protecting them against a wide range of threats, including firmware tampering, rollback attacks, and unauthorized code execution.

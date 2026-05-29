// C++ program to implement XOR - Encryption
#include<bits/stdc++.h>

// The same function is used to encrypt and
// decrypt
void encryptDecrypt(char inpString[])
{
    // Define XOR key
    // Any character value will work
    char xorKey[] = "THM{}";

    // calculate len_inputgth of input string
    int len_input = strlen(inpString);
    // calculate len_inputgth of XOR key string
    int len_xorKey = strlen(xorKey);
	
    // print len_xorKey
	printf("XOR key lenght: %i",len_xorKey);
	printf("\n");
    // perform XOR operation of key
    // with every character in string
	printf("De/Encrypted String: ");
    for (int i = 0; i < len_input; i++)
    {
        inpString[i] = inpString[i] ^ xorKey[i%len_xorKey];
        printf("%c",inpString[i]);
    }
}
void flagDecrypt(char inpString[])
{
    // Define XOR key
    // Any character value will work
    char xorKey[] = "bIO7D";

    // calculate len_inputgth of input string
    int len_input = strlen(inpString);
    // calculate len_inputgth of XOR key string
    int len_xorKey = strlen(xorKey);
	
    // print len_xorKey
	printf("XOR key lenght: %i",len_xorKey);
	printf("\n");
    // perform XOR operation of key
    // with every character in string
	printf("Decrypted flag: ");
    for (int i = 0; i < len_input; i++)
    {
        inpString[i] = inpString[i] ^ xorKey[i%len_xorKey];
        printf("%c",inpString[i]);
    }
}
// Driver program to test above function
int main()
{
    char sampleString[] = "67222c4334020b0d56307612157930475e0253277204130b255f26185011411e18083141122e4a39";

    // Encrypt the string
//    printf("Encrypted String: ");
//    encryptDecrypt(sampleString);
//    printf("\n");

    // Decrypt the string
    encryptDecrypt(sampleString);
    flagDecrypt(sampleString);
    return 0;
}
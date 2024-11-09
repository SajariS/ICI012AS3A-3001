// passtr - a simple static analysis warm up exercise
// Copyright 2024 Tero Karvinen https://TeroKarvinen.com

#include <stdio.h>
#include <string.h>

void xor_encrypt_decrypt(char *input, char *output, char key) {
    size_t len = strlen(input);
    for (size_t i = 0; i < len; i++) {
        output[i] = input[i] ^ key;
    }
    output[len] = '\0';
}

int main() {
	char password[20];
	char encrypted[] = { 's' ^ 'K', 'a' ^ 'K', 'l' ^ 'K', 'a' ^ 'K', '-' ^ 'K', 'h' ^ 'K', 'a' ^ 'K', 'k' ^ 'K', 'k' ^ 'K', 'e' ^ 'K', 'r' ^ 'K', 'i' ^ 'K', '-' ^ 'K', '3' ^ 'K', '2' ^ 'K', '1' ^ 'K', '\0' };
	char decrypted[sizeof(encrypted)];

	xor_encrypt_decrypt(encrypted, decrypted, 'K');

	printf("What's the password?\n");
	scanf("%19s", password);
	if (0 == strcmp(password, decrypted)) {
		printf("Yes! That's the password. FLAG{Tero-d75ee66af0a68663f15539ec0f46e3b1}\n");
	} else {
		printf("Sorry, no bonus.\n");
	}
	return 0;
}

"""
#mod26, 13 and caesar
def shift_cipher_encrypt(plaintext, shift):
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()

            # Convert the character to uppercase for easier manipulation
            char = char.upper()

            # Calculate the new character position after shifting
            char_code = ord(char) - ord('A')
            new_char_code = (char_code - shift) % 26

            # Convert the new character code back to a character
            new_char = chr(new_char_code + ord('A'))

            # If the original character was lowercase, convert it back
            if not is_upper:
                new_char = new_char.lower()

            # Append the new character to the ciphertext
            ciphertext += new_char
        else:
            # If the character is not a letter, leave it unchanged
            ciphertext += char

    return ciphertext

# Example usage:
plaintext1 = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
shift1 = 13
ciphertext1 = shift_cipher_encrypt(plaintext1, shift1)
print(f"Plaintext (Mod26): \"{plaintext1}\"")
print(f"Shift: {shift1}")
print(f"Ciphertext: \"{ciphertext1}\"")

# Example usage:
plaintext2 = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
shift2 = 13
ciphertext2 = shift_cipher_encrypt(plaintext2, shift2)
print(f"Plaintext (13): \"{plaintext2}\"")
print(f"Shift: {shift2}")
print(f"Ciphertext: \"{ciphertext2}\"")

plaintext3 = "ynkooejcpdanqxeykjrbdofgkq"
for i in range (0,40,1):
	shift3 = i
	ciphertext3 = shift_cipher_encrypt(plaintext3, shift3)
	print(f"\nPlaintext: \"{plaintext3}\"")
	print(f"Shift: {shift3}")
	print(f"Ciphertext: \"{ciphertext3}\"")

#easy-peasy
com = "51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57"

flag = "51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57"
text = "23666b6f3a3c1a111d3971771d397122181d3927731d3925231d3924241d3924"
dec = b'A' * 32

# Aquí se realiza una operación XOR byte a byte entre "text" y "dec" y se almacena en "key".
key = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), text, dec))
key1 = "".join(key)
print(f"keyValue:{key1}")  # Imprimirá la lista de resultados de la operación XOR.

# Luego, se realiza una operación XOR similar entre "flag" y la concatenación de "key".
# Nota: "".join(key) convierte la lista de bytes "key" en una cadena.
result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ int(k, 16)), flag, key1))
result1 = "".join(result)
print(f"mainResultValue:{result1}")  # Imprimirá una lista de resultados de la operación XOR con "flag" y "key".

#The Numbers
def caesar_number(numbers):
    ciphertext = ""

    for char in numbers:
        if type(char) != str:
            # Calculate the new character position after shifting
            new_char_code = (char - 1) % 26

            # Convert the new character code back to a character
            new_char = chr(new_char_code + ord('A')).upper()

            # Append the new character to the ciphertext
            ciphertext += new_char
        else:
            # If the character is not a letter, leave it unchanged
            ciphertext += char

    return ciphertext

plaintext2 = [16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,'}']
ciphertext3 = caesar_number(plaintext2)
print(f"\nPlaintext new: \"{ciphertext3}\"")

#New Caesar
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
	decoded = ""
	binary = ""

	for c in enc:
		if c in ALPHABET:
			# Convert the character back to a 4-bit binary string
			binary += "{:04b}".format(ALPHABET.index(c))

		# Check if we have a complete 8-bit binary representation
		if len(binary) == 8:
			# Convert the binary to a character and append to the decoded result
			decoded += chr(int(binary, 2))
			binary = ""  # Reset the binary string

	return decoded

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

enc = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

for key in ALPHABET:
	flag = ""
	for c in enc:
		flag += shift(c, key)

	decoded_flag = b16_decode(flag)
	print(f"Key '{key}': {decoded_flag}")

#Easy1 table

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
+----------------------------------------------------
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

"""
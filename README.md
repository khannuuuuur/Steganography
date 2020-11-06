# Steganography
Encodes hidden messages in pictures.

Each pixel's green value is converted to binary. The rightmost digit is changed to one or zero depending on the message to be encoded.
A sequence of 7 pixels' green values' rightmost binary digit can be converted from binary to a decimal to an ASCII character.
All of these ASCII characters form a message.

# ECS-101-Compression-Project

The compression program compresses a text file into the shortest possible bit string using a conversion table that priortizes the most common letters, two letter and three letter combinations/words. The output is the number of bits needed to encode the text file followed by the bit string.

The decompression program will take a bit string that was compressed using the conversion table and return the original words.

In order to test the compression program, you can make changes to the text_to_bits file in the testing folder to compress whatever file you choose.

Similarly, to test the decompression program, first compress a text file and then paste the bit string in the bits_to_text file.

def ceaser_cipher(phrase):
	new_strs = []
	for word in phrase: 
	    new_word = []
	    for character in word:
	    	if(ord(character)>=97 and ord(character)<=122):
	    		x = ord(character) + 13
	    		new_word.append(chr(x if 97 <= x <= 122 else 96 + x % 122))
	    	if(ord(character)>=65 and ord(character)<=90):
	    		x = ord(character) + 13
	    		new_word.append(chr(x if 65 <= x <= 90 else 64 + x % 90))

	    new_strs.append("".join(new_word))

	print ("Encrypted Text is:", " ".join(new_strs))


	new_str = []
	for word in new_strs: 
	    new_words = []
	    for character in word:
	    	if(ord(character)>=97 and ord(character)<=122):
	    		x = ord(character) + 13
	    		new_words.append(chr(x if 97 <= x <= 122 else 96 + x % 122))
	    	if(ord(character)>=65 and ord(character)<=90):
	    		x = ord(character) + 13
	    		new_words.append(chr(x if 65 <= x <= 90 else 64 + x % 90))

	    new_str.append("".join(new_words))

	print ("Decrypted Text is:", " ".join(new_str))


phrase=list(input('Enter message: ').split(' '))
ceaser_cipher(phrase)
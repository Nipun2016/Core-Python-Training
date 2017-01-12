1) In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the shift is 13. In Python, the key for ROT-13 may be represented by means of the following dictionary:
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}


Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, you will be able to read the following secret message:
  Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
Note that since English has 26 characters, your ROT-13 program will be able to both encode and decode texts written in English.


2) Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using list comprehensions.

3) Create a single line function which takes a list of numbers and returns a list of even numbers from the given list. The definition  of function should not be more than one line.

4)Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":”gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. Use comprehension to achieve this.
User will input “merry christmas and happy new year”, user should get the corresponding Swedish massage based on the lexicon.
Code to translate for translating the message from English to Swedish and printing the final out should not be more than one line.

5)Your task in this exercise is as follows:
User will enter a string of brackets like “[[ ]] [ ] [ ] [[[ ]]]”      
Determine whether the string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order)
Examples:
  [ ]        OK   ][        NOT OK
   [ ][ ]      OK   ][ ][      NOT OK
   [ [ ][ ] ]    OK   [ ] ][ [ ]    NOT OK


6)Write a Python program to unzip a list of tuples into individual lists

7) Write a Python program to convert a tuple to a dictionary.

8) Write a program that, given a word and a list of possible anagrams, selects the correct sublist.
Given "listen" and a list of candidates like "enlists" "google" "inlets" "banana" the program should return a list containing "inlets".

9) Write a program that, given a list of all the multiples of particular numbers up to but not including a given number.
Example : If we list all the natural numbers up to but not including 20 that are multiples of either 3 or 5, we get 3, 5, 6 and 9, 10, 12, 15, and 18.
Use lambda and comprehension only

10) Write a generator that takes a number as an input and gives the output of numbers starting from 0 upto that number when we call next() it. 

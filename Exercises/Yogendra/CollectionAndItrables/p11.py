import re
def enc_dcr(usr_key):
   key_dict={'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a',   'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k','y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S','G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

   enc_key=''
   if re.match("^[a-zA-Z ]*$", usr_key):
      for ch in usr_key:
    
         if ch != ' ':	
          enc_key=enc_key+key_dict[ch]
         else:
          enc_key=enc_key+' '
      return (enc_key)
   else:
      return ("only characters")

if __name__=="__main__":
     usr_key=input("enter ur message you w:ant encrypt/dcrypt: ")
     print(enc_dcr(usr_key))

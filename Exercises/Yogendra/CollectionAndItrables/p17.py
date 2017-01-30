def tupp2dict(tpple):
    dict={}
    k=1
    for ele in tpple: 
          dict[k]=ele
          k=k+1 
    return(dict)

if __name__=="__main__":
   tpple='i','am','yogendra','katewa',647346
   print(tupp2dict(tpple))

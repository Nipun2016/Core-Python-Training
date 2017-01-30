def display_plants(lst,lst1):
     dict_stud={"alice":1,"bob":2,"charlie":3,"david":4,"eve":5,"fred":6,"ginny":7,"harriet":8,"ileana":9,
     "joseph":10,"kincaid":11,"larry":12}
     dict_plant={"V":'violets',"R":'radishes',"C":'clover',"G":'grass'}
     for std in lst1:
        std=std.lower()
        try:
            stud=dict_stud[std]
            n1=(stud*2)-2
            n2=(stud*2)
            str2=''
            try: 
                for rw in lst:
                      try:   
                         for i in rw:
                             dict_plant[i]
                      except Exception as e:
                         print(i,"is not in planted tree")
                         return False
                for plant in rw[n1:n2]:
                        str2=str2+dict_plant[plant]+' '
                print(std," : ",str2)
                str2=''
                return True
            except Exception as e:
                    print(plant,"is not in planted trees")
        except Exception as e:
               print(std,"named student not found")
               return False      


if __name__=="__main__":
     plants=input("enter plants in rows:")
     stud_name=input("enter student name:")
     lst,lst1=[],[]
     str1=''
     str3=''
     for str in plants:
          if str != ' ' :
             str1=str1+str
          else:
             lst.append(str1)
             str1=''
     lst.append(str1)  
     for str in stud_name:
          if str != ' ' :
             str=str.lower()
             str3=str3+str
          else:
             lst1.append(str3)
             str3=''
     lst1.append(str3)
     print(display_plants(lst,lst1))

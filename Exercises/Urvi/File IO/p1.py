first_file = open("first.txt","r")
first_file_data = first_file.read()
print (first_file_data)


second_file = open("second.txt","w+").write(first_file_data)




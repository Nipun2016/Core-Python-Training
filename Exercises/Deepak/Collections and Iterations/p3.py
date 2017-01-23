def find_even_number(valid_list):
    return (list(filter(lambda x : x%2 == 0, valid_list)))

if __name__ == "__main__":
    try:
        input_list = [int(x) for x in input("Enter Value to list :").split()]
        print (find_even_number(input_list))
    except Exception as e:
        print ("Please Enter digit only...")

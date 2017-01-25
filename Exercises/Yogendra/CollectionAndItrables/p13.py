def eve_only(n): return([x for x in range(1,n) if x%2 == 0])
if __name__=="__main__":
    print(eve_only(10))

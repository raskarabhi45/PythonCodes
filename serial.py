#Serial Programming
# eka burner vrti eka eka number cha sqaure ek zala ki dusra as
# eka core vrtich sgl zal load sgla tychya vrtich aaala 
def Square(no):
    return (no*no)

def main():
    data=[1,2,3,4,5]
    result=[]

    for value in data:
        result.append(Square(value))

    print("Result after operation is : ",result)
    


if __name__=="__main__":
    main()
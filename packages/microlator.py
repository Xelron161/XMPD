while True:
    expr = input("calc> ")
    if expr == "q":
        break
    try:
        print(eval(expr))
    except:
        print("error")

def ask_for_int():
    
    while True:
        try:
            res = int(input("Please enter an integer value: "))
        except TypeError as te:
            print(te)
            continue
        except ValueError as ve:
            print(ve)
            continue
        except:
            print("Generic error")
            continue
        else:
            print("Yes Thank you")
            break
        finally:
            print("End of try-except-finally")

ask_for_int()
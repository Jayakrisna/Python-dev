def check(p):
    return len(p)>=8 and any (i.isupper() for i in p) and any(i.islower() for i in p) and any (i.isdigit() for i in p)
en = input("Enter a Password:")
if check(en):
    print('Valid')
else:
    print("not valid")
    

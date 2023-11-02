a=int(input("birinci ededi daxil edin"))
b=int(input("ikinci ededi daxil edin"))
if a>b:
    print("{} {} dan-böyükdür.".format(a,b))
elif a==b:
    print("{} {}- ile beraberdir.".format(a,b))
else:
    print("{} {}-den böyükdür.".format(b,a))

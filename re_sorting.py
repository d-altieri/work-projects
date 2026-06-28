import re

text = '''		INC127194473
T3LA0902m2/LA0102BA_51LAB|TMB_CA_HuntingtonPark(LA33378A)_01(SmallCell)	CS1029625	INC127192619
LA367 / LA0102BA_31LAB|TMB_CA_HuntingtonPark(LA33378A)_01(SmallCell)	CS1029631	INC127201382
LA353 / LA0102BA_11LAB|TMB_CA_HuntingtonPark(LA33378A)_01(SmallCell)	CS1029634	INC127201250
LA340m1 / LA0101BA_41LAB|TMB_CA_HuntingtonPark(LA33378A)_01(SmallCell)	CS1029635	INC127194330
T3LA0914/LA0102BA_61LAB|TMB_CA_HuntingtonPark(LA33378A)_01(SmallCell)	CS1029636	INC127201992
T3LA0888 / LA0102BA_41LAB|TMB_CA_HuntingtonPark(LA33378A)_01(SmallCell)	CS1029630	INC127201947
LA348/LA0101BA_31LAB|TMB_CA_HuntingtonPark(LA33378A)_01(SmallCell)	CS1029633	INC12719433
'''


lines = text.splitlines()
pattern = r"\w{8}_\d{2}LAB"
match = re.findall(pattern, text)
result = sorted(match)


if match:
    print(*result, sep="\n")
else:
    print("No equipment found")

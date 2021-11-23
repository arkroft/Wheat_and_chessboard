# Part I
# Constants
AllCell = 64
Sum = 0
CurrCell = 1
CurrCnt = 1
# Part II
# Calculations
while CurrCell <= AllCell:
    if CurrCell == 1:
        CurrCnt = 1
    else:
        CurrCnt = CurrCnt * 2
    Sum += CurrCnt
    print("on", CurrCell, "cell", " -> ", CurrCnt, "cor.")
    CurrCell += 1
print()
print("Sum = ", Sum)
print()

# Part III
# Area constants
OneSerWeight = 50
OneTon = 1000000000

# Area calculations

WeightTon = (Sum * OneSerWeight) / OneTon
print("Total weight = ", WeightTon, "tons")
print()

# For my city
print("For the Novosibirsk")
AreaNovosibirsk = 505000000
MetersInSqr = AreaNovosibirsk * 0.8
Height = WeightTon / MetersInSqr
print("Height in meters: ", Height)
print()

# For my district
print("For the Novosibirsk district")
AreaNSO = 178200000000
MetersInSqr = AreaNSO * 0.8
Height = WeightTon / MetersInSqr
print("Height in meters: ", Height)
HarvestNSO = 2500000
YearHarvestNSO = WeightTon / HarvestNSO
print("How many years will it take to harvest:", YearHarvestNSO)
print()


# For country
print("For Russia ")
AreaRussia = 17098246000000
MetersInSqr = AreaRussia * 0.8
Height = WeightTon / MetersInSqr*100
print("Height in santimeters: ", Height)
HarvestRussia = 60000000
YearHarvestRussia = WeightTon / HarvestRussia
print("How many years will it take to harvest:", YearHarvestRussia)
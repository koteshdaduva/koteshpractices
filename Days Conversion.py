n = int(input())
years = int(n/365)
r = n % 365
weeks = int(r/7)
r = r % 7
days = int(r)

print(str(years) + " years " + str(weeks) + " weeks " + str(days) + " days")

#creating a dictionary
#V dictionary V
capitalsofcountries = {"England" : "London",
                     "France" : "Paris",
                     "Germany" : "Berlin",
                     "Canada" : "Ottawa",
                     "USA" : "WashingtonDC" }

#check if engleand is in the dictionary
if "England" in capitalsofcountries:
    print("Yes England exists")
else:
    print("No, England doesn't exist")

#return value asscsiated value
print(capitalsofcountries["England"])

#return error if something doesn't exist in dictionary
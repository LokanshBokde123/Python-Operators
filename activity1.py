field1 = 180
field2 = 140
field3 = 90
field4 = 200
field5 = 140

total = field1 + field2 + field3 + field4 + field5
average = total / 5 # division operator

print("Total Harvest   :", total , "kg")
print("Average Per Field :", average , "kg")

price_per_kg = 18
earnings = total * price_per_kg
print("Total Earnings In Rupees  :", earnings)

bags = total // 25 # floor division operator
leftover = total % 25 # modulus operator

print("Full Bags Packed    :", bags)
print("Leftover Grains   :", leftover , "kg")

last_year = 500
print("Better Than Last Year? ", total > last_year)
print("Same As Last Year? ", total == last_year)
print("At Least As Good? ", total >= last_year)

total += 30 # we can write either total = total + 30 or total += 30
print("After Bonus Crop    :", total , "kg")

total -= 15 # we can write either total = total - 15 or total -= 15
print("After Seed Reserve   :", total , "kg")

bags = total // 25 # floor division operator
print("Final Bags Packed   :", bags)
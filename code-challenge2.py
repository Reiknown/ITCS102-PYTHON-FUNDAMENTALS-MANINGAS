halaga = eval(input("\t\t\t\tIlagay ang halagang ide-deposito: "))

print("\tNarito ang paghahati gamit ang denominasyon sa Pilipinas:")

# 1000
libohan = halaga // 1000 
halaga = halaga % 1000
print("\t\t\t\t\t\t\t\t", libohan, "- ₱1000")

# 500
limandaanan = halaga // 500
halaga = halaga % 500
print("\n\t\t\t\t\t\t\t", limandaanan, "- ₱500")

# 200
dalawandaanan = halaga // 200
halaga = halaga % 200
print("\n\t\t\t\t\t\t", dalawandaanan, "- 200")

# 100
isandaanan = halaga // 100
halaga = halaga % 100
print("\n\t\t\t\t\t", isandaanan, "- ₱100")

# 50
limampuan = halaga // 50
halaga = halaga % 50
print("\n\t\t\t\t", limampuan, "- ₱50")

# 20
dalawampuan = halaga // 20
halaga = halaga % 20
print("\n\t\t\t", dalawampuan, "- 20")

# 10
sampuan = halaga // 10
halaga = halaga % 10
print("\n\t\t", sampuan, "- ₱10")

# 5
limahan = halaga // 5
halaga = halaga % 5
print("\n\t", limahan, "- ₱5")

# 1
isahan = halaga // 1
halaga = halaga % 1
print("\n", isahan, "- ₱1")

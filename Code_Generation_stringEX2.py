print("This program prints out the product lot number given by the client")

Product_lot_number = "037-00901-00027"

country_code = (Product_lot_number[0:3])
Product_code = (Product_lot_number[4:9])
Batch_number = (Product_lot_number[10:])

print("Country Code: "+ country_code)
print("Product Code: "+ Product_code)
print("Batch Number: "+ Batch_number)

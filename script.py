#  The urpose of the program is to build a system to help speed up the process of creating receipts for customers of a small business.
# Lovely Loveseats for neat Suites on Fleet Street is the name of the store/ small business that sells chairs.
# Below are the types of different seats and other items, along with a description, and the different prices of each.
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. "
lovely_loveseat_price = 254.00
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. "
stylish_settee_price = 180.50
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15
# Sales tax must also be considered for the receipt.  The sales tax is 8.8%.
sales_tax = .088
# We have our first customer. Below is code for a receipt of their purchase.  We are starting with a total of zero, and then adding items to the initial price as we go along.
customer_one_total = 0
# Descriptions of each item purchased are also important to have clear and detailed receipts.
customer_one_itemization = ""
# One loveseat is purchased.
customer_one_total += lovely_loveseat_price
# We are keeping track of the items purchased.  A description of the item is important.
customer_one_itemization += lovely_loveseat_description
# A luxurious lamp has also been purchased.
customer_one_total += luxurious_lamp_price
# A description of the lamp is also added.
customer_one_itemization += luxurious_lamp_description
# The customer is finally checking out.  We first calculate the sales tax. 
customer_one_tax = customer_one_total * sales_tax
# We then add the sales tax to the total.
customer_one_total += customer_one_tax
# Now, we are going to start printing the receipt. We are starting with the heading, then print the sale information.
print("Customer One Items:")
print(customer_one_itemization)
# Then, we add a heading.
print("Customer One Total:")
# Then, we are printing the total.
print(customer_one_total)
# We just created the store's catalog and have an example of the first customer and how the code would function.
from Classes import *
from datetime import datetime

# Create e-books
ebook1 = EBook("EBook1", "Author A", datetime(2023, 3, 10), Genre.FICTION, 120)
ebook2 = EBook("EBook2", "Author B", datetime(2022, 12, 15), Genre.NON_FICTION, 150)
ebook3 = EBook("EBook3", "Author C", datetime(2021, 9, 20), Genre.SCIENCE_FICTION, 180)
ebook4 = EBook("EBook4", "Author D", datetime(2020, 6, 25), Genre.FANTASY, 110)
ebook5 = EBook("EBook5", "Author E", datetime(2019, 4, 5), Genre.MYSTERY, 130)
ebook6 = EBook("EBook6", "Author F", datetime(2018, 1, 15), Genre.BIOGRAPHY, 140)

person1 = Person("Rashed Alremeithi", "rashed@zu.ac.ae", 21)
print(person1)

# Create a temporary instance to use create_account
temp_customer = Customer("", "", "", "")  # Placeholder values so we can use the create account function to make the objcets

# Create customers using the create_account method
customer1 = temp_customer.create_account("Rashed AlRemeithi", "rashed@zu.ac.ae", "rashed123", "password1")
customer2 = temp_customer.create_account("Afshan Parker", "afshan@zu.ac.ae", "afshan123", "password2")
customer3 = temp_customer.create_account("Zayed Alblooshi", "zayed@zu.ac.ae", "zayed123", "password3")


#testing browse ebooks function
ebook_instance = EBook("", "", None, "", 0)  # Creating a temporary instance
ebook_instance.browse_ebooks()

#furthermore browse ebook negates the need to print the all instances of ebook as it already does that.



# Create a shopping cart instance
shopping_cart1 = ShoppingCart()

# note that addebook and removeebook would call the functions updatetotalprice and updatequantity
# Add e-books to the shopping cart
shopping_cart1.addEbook(ebook1)
shopping_cart1.addEbook(ebook2)
shopping_cart1.addEbook(ebook3)
shopping_cart1.addEbook(ebook4)
shopping_cart1.addEbook(ebook5)
shopping_cart1.addEbook(ebook6)

# Remove an e-book from the shopping cart
shopping_cart1.removeEbook(ebook2)

# Print the shopping cart to verify contents
print("Shopping Cart after adding and removing e-books:")
print(shopping_cart1)

customer1 = Customer(name="Rashed Al Remeithi", contact_info="202112513@zu.ac.ae", username="rashed123", password="securePassword", shopping_cart=shopping_cart1)

#purchase ebook function makes the order and invoice for the customer and prints the order and invoice. Furthermore, it calls the functions discount() discount type()
customer1.purchase_ebook()

payment1 = Payment(680, 100, False)

payment1.updatePaid()
print(payment1)

#make payment function also calls the update paid function to update the satus to paid
payment1.makePayment(580)
print(payment1)







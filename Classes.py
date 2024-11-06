from datetime import datetime
from enum import Enum

# Genre Enum Class
class Genre(Enum):
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    FANTASY = "Fantasy"
    SCIENCE_FICTION = "Science Fiction"
    MYSTERY = "Mystery"
    BIOGRAPHY = "Biography"

# AppliedDiscount Enum Class
class AppliedDiscount(Enum):
    NONE = "No Discount"
    LOYALTY_DISCOUNT = "Loyalty Discount"
    BULK_DISCOUNT = "Bulk Discount"
    BULK_AND_LOYALTY = "Bulk + Loyalty Discount"


# E-Book Class
class EBook:
    all_ebooks = []  #list to contain all objects of ebook class

    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title  # Title of the e-book
        self.__author = author  # Author of the e-book
        self.__publication_date = publication_date  # Publication date
        self.__genre = genre  # Genre of the e-book
        self.__price = price  # Price of the e-book

        #appending object into all_ebooks list
        EBook.all_ebooks.append(self)

    # Getter and setter for title
    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    # Getter and setter for Author
    def getAuthor(self):
        return self.__author

    def setAuthor(self, author):
        self.__author = author

    # Getter and setter for publication date
    def getPublicationDate(self):
        return self.__publication_date

    def setPublicationDate(self, publication_date):
        self.__publication_date = publication_date

    # Getter and setter for Genre
    def getGenre(self):
        return self.__genre

    def setGenre(self, genre):
        self.__genre = genre

    # Getter and setter for price
    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    # EBook Class __str__ function
    def __str__(self):
        return "E-Book(title: " + self.__title + " " + "author: " + self.__author + " " + "publication_date: " + str(self.__publication_date) + " " + "genre: " + str(self.__genre) + " " + "price: " + str(self.__price) + ")"

    def browse_ebooks(self):
        """This functions uses for loop to print every e-book in the list for all available ebooks"""
        for ebook in EBook.all_ebooks:
            print("This E-Book is available:",ebook)

# Define the Person class as the parent class
class Person:
    def __init__(self, name, contact_info, age):
        self._name = name
        self._contact_info = contact_info
        self._age = age

    # Getter and Setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and Setter for contact_info
    def get_contact_info(self):
        return self._contact_info

    def set_contact_info(self, contact_info):
        self._contact_info = contact_info

    # Getter and Setter for age
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # Person class string function
    def __str__(self):
        return "Name: " + str(self._name) + ", Contact Info: " + str(self._contact_info) + ", Age: " + str(self._age)

# Customer Class
class Customer(Person):
    def __init__(self, name, contact_info, username, password, is_loyalty_member=False, shopping_cart=None):
        super().__init__(name, contact_info, None)
        self.__name = name
        self.__contact_info = contact_info
        self.__is_loyalty_member = is_loyalty_member  # Loyalty program membership status
        self.__username = username  # Username for the account
        self.__password = password  # Password for the account
        self.__shopping_cart = shopping_cart  # Shopping cart for the customer
        self.__order = None  # Order of the customer
        self.__invoice = None  # Invoice for customer

    # Getter and setter for Name
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # Getter and setter for contact_info
    def getContactInfo(self):
        return self.__contact_info

    def setContactInfo(self, contact_info):
        self.__contact_info = contact_info

    # Getter and setter for is loyalty member
    def getIsLoyaltyMember(self):
        return self.__is_loyalty_member

    def setLoyaltyMember(self, is_loyalty_member):
        self.__is_loyalty_member = is_loyalty_member

    # Getter and setter for username
    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    # Getter and setter for password
    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    # Getter and setter for Shopping cart
    def getShoppingCart(self):
        return self.__shopping_cart

    def setShoppingCart(self):
        self.__shopping_cart = ShoppingCart()

    # Getter and setter for order
    def getOrder(self):
        return self.__order

    def setOrder(self):
        self.__order = Order()

    # Getter and setter for Invoice
    def getInvoice(self):
        return self.__invoice

    def setInvoice(self):
        self.__invoice = Invoice()

    #this function will create an account for the customer, in other words it creates an object for the class when called
    def create_account(self, name, contact_info, username, password, is_loyalty_member=False):
        return Customer(name, contact_info, username, password, is_loyalty_member)

    def purchase_ebook(self):
        """This function transfers ebook list order dates list and total price from shopping cart to the order class
        Furthermore, it calls the discount function to apply a discount
        Also, it initializes the invoice attributes by transferring the ebook list from order, creating a dictionary for itemized price
        applying 8% VAT to total amount from order, and it calls the discount type function to update which discounts are being used, then prints the invoice."""
        self.__order = Order()
        self.__order.ebooks = self.__shopping_cart.getEbooks() #transfers ebook list from shopping cart class to order class
        self.__order.order_date = self.__shopping_cart.getOrderDates() #transfers order dates list from shopping cart class to order class
        self.__order.total_amount = self.__shopping_cart.getTotalPrice() #Transfers total price in shopping cart to total amount in order class
        self.discount()  # Call the discount method to check for discounts
        print("Order placed successfully.")
        print(self.__order)
        self.__invoice = Invoice()
        self.__invoice.ebooks = self.__order.getEbooks()  # Assign e-books to the invoice
        self.__invoice.itemized_price = {ebook.getTitle(): ebook.getPrice() for ebook in self.__invoice.getEbooks()}  # Create itemized price dictionary
        self.__invoice.total = self.__order.getTotalAmount() * 1.08  # Apply 8% VAT
        self.DiscountType(self.__invoice)
        print(self.__invoice)

    def discount(self):
        """This function checks if the customer has met the conditions for a discount it is called when purchase ebook is called"""
        # Check for 20% discount if there are 5 or more e-books
        if len(self.__order.ebooks) >= 5:
            self.__order.total_amount *= 0.80  # Apply 20% discount

        # Check for 10% loyalty discount
        if self.__is_loyalty_member:
            self.__order.total_amount *= 0.90  # Apply 10% discount

    def DiscountType(self, invoice):
        # Check for Bulk + Loyalty Discount
        if len(invoice.getEbooks()) >= 5 and self.__is_loyalty_member:
            self.__invoice.applied_discount = AppliedDiscount.BULK_AND_LOYALTY
        # Check for Bulk Discount
        elif len(invoice.getEbooks()) >= 5:
            self.__invoice.applied_discount = AppliedDiscount.BULK_DISCOUNT
        # Check for Loyalty Discount
        elif self.__is_loyalty_member:
            self.__invoice.applied_discount = AppliedDiscount.LOYALTY_DISCOUNT
        else:
            self.__invoice.applied_discount = AppliedDiscount.NONE

    # Customer Class __str__ function
    def __str__(self):
        return "Customer(name: " + self.__name + " " + "contact_info: " + self.__contact_info + " " + "username: " + self.__username + " " + "is_loyalty_member: " + str(self.__is_loyalty_member) + ")"

# Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.__ebooks = []  # List of e-books in the shopping cart
        self.__total_price = 0.0  # Total price of e-books in the cart
        self.__order_dates = []

    # Getter and setter for ebooks
    def getEbooks(self):
        return self.__ebooks

    def setEbooks(self, ebooks):
        self.__ebooks = ebooks

    # Getter and setter for total_price
    def getTotalPrice(self):
        return self.__total_price

    def setTotalPrice(self, total_price):
        self.__total_price = total_price

    # Getter and setter for order_dates
    def getOrderDates(self):
        return self.__order_dates

    def setOrderDates(self, order_dates):
        self.__order_dates = order_dates

    def addEbook(self, ebook):
        """this function will add a specified ebook to the shopping cart ebook list while also updating total price"""
        self.__ebooks.append(ebook)  # Adds a specified e-book to the cart
        self.updateTotalPrice() #updates total price because the list has changed and also the price
        self.__order_dates.append(datetime.now())  # Record the current date and time
        print("Ebook '" + ebook.getTitle() + "' added to the cart.")

    def removeEbook(self, ebook):
        """Remove a specified e-book from the shopping cart and the corresponding order date for the removed e-book."""
        if ebook in self.__ebooks:
            index = self.__ebooks.index(ebook)  # Find the index of the e-book to remove
            self.__ebooks.pop(index)  # Remove the e-book from the list
            self.__order_dates.pop(index)  # Remove the corresponding order date
            self.updateTotalPrice()  # Update total price
            print("Ebook '" + ebook.getTitle() + "' removed from the cart.")
        else:
            print("Ebook '" + ebook.getTitle() + "' not found in the cart.")

    def updateQuantity(self):
        """this function updates the customer on their shopping list total"""
        print(f"New total price is: {self.__total_price}")  # Prints updated total price to inform the customer


    def updateTotalPrice(self):
        """this function updates the total price"""
        self.__total_price = sum(ebook.getPrice() for ebook in self.__ebooks)  # Calculate total price
        self.updateQuantity()

    # ShoppingCart Class __str__ function
    def __str__(self):
        return "ShoppingCart(total_price: " + str(self.__total_price) + ", ebooks: " + str([ebook.getTitle() for ebook in self.__ebooks]) + ", order_dates: " + str([str(date) for date in self.__order_dates]) + ")"
# Order Class
class Order:
    def __init__(self):
        self.__order_date = []  # list of order dates of the ebooks ordered
        self.__ebooks = []  # List of e-books in the order
        self.__total_amount = 0.0  # Total amount of the order

    # Getter and setter for order_date
    def getOrderDate(self):
        return self.__order_date

    def setOrderDate(self, order_date):
        self.__order_date = order_date

    # Getter and setter for ebooks
    def getEbooks(self):
        return self.__ebooks

    def setEbooks(self, ebooks):
        self.__ebooks = ebooks

    # Getter and setter for total_amount
    def getTotalAmount(self):
        return self.__total_amount

    def setTotalAmount(self, total_amount):
        self.__total_amount = total_amount

    # Order Class __str__ function
    def __str__(self):
        return "Order(order_date: " + str(self.__order_date) + " " + "total_amount: " + str(self.__total_amount) + " " + "ebooks: " + str([ebook.__title for ebook in self.__ebooks]) + ")"

# Invoice Class
class Invoice:
    def __init__(self):
        self.__ebooks =[]
        self.__itemized_price = {}  # Dictionary that has itemized price for every ebook in the list
        self.__applied_discount = AppliedDiscount.NONE  # Enum for if a discount is used
        self.__total = 0.0  # Final total price including 8% vat

    # Getter and setter for ebooks
    def getEbooks(self):
        return self.__ebooks

    def setEbooks(self, ebooks):
        self.__ebooks = ebooks

    # Getter and setter for itemized_price
    def getItemizedPrice(self):
        return self.__itemized_price

    def setItemizedPrice(self, itemized_price):
        self.__itemized_price = itemized_price

    # Getter and setter for applied_discount
    def getAppliedDiscount(self):
        return self.__applied_discount

    def setAppliedDiscount(self, applied_discount):
        self.__applied_discount = applied_discount

    # Getter and setter for total
    def getTotal(self):
        return self.__total

    def setTotal(self, total):
        self.__total = total

    # Invoice Class __str__ function
    def __str__(self):
        return "Invoice(itemized_price: " + str(self.__itemized_price) + " " +"applied_discount: " + str(self.__applied_discount) + " " +"total: " + str(self.__total) + ")"

# Payment Class
class Payment:
    def __init__(self, amount_due=0.0, paid_amount=0.0, paid=False):
        self.__amount_due = amount_due #Amount due
        self.__paid_amount = paid_amount  # Amount paid
        self.__paid = paid  # Payment status

    # Getter and setter for amount_due
    def getAmountDue(self):
        return self.__amount_due

    def setAmountDue(self, amount_due):
        self.__amount_due = amount_due

    # Getter and setter for paid_amount
    def getPaidAmount(self):
        return self.__paid_amount

    def setPaidAmount(self, paid_amount):
        self.__paid_amount = paid_amount

    # Getter and setter for paid
    def getPaid(self):
        return self.__paid

    def setPaid(self, paid):
        self.__paid = paid

    def updatePaid(self):
        """Update the payment status based on whether the paid amount meets or exceeds the amount due."""
        if self.__paid_amount >= self.__amount_due:
            self.__paid = True
            print("Payment complete.")
        else:
            self.__paid = False
            print("Payment not complete")

    def makePayment(self, amount):
        """Make a payment to meet the amount due"""
        self.__paid_amount += amount  # Add to the amount paid
        self.updatePaid()  # Check if the payment meets or exceeds the amount due

    # Payment Class __str__ function
    def __str__(self):
        return "Payment(amount_due: " + str(self.__amount_due) + " " + "paid_amount: " + str(self.__paid_amount) + " " + "paid: " + str(self.__paid) + ")"
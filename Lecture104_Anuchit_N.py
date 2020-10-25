class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to " + self.name+ " " + self.lastname + "'s cart")

customer1 = Customer()
customer1.name = "Champ"
customer1.lastname = "Way of me"
customer1.addCart()


customer2 = Customer()
customer2.name = "Kan"
customer2.lastname = "Way of me"
customer2.addCart()

customer3 = Customer()
customer3.name = "Porn"
customer3.lastname = "Way of me"
customer3.addCart()
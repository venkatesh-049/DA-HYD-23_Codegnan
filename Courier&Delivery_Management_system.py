import time
from datetime import datetime
import os

# =========================================================
# PARENT CLASS
# =========================================================

class Person:

    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    def person_details(self):
        print(f"Name: {self.name}")
        print(f"Mobile: {self.mobile}")


# =========================================================
# CUSTOMER CLASS
# =========================================================

class Customer(Person):

    def __init__(self, name, customer_id, mobile, address):

        super().__init__(name, mobile)

        self.customer_id = customer_id
        self.address = address

    def details(self):

        print("\n----- Customer Details -----")
        print(f"Customer Name: {self.name}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Mobile: {self.mobile}")
        print(f"Address: {self.address}")


# =========================================================
# DELIVERY AGENT CLASS
# =========================================================

class DeliveryAgent(Person):

    def __init__(self, name, mobile, agent_id):

        super().__init__(name, mobile)

        self.agent_id = agent_id
        self.available = True

    def agent_details(self):

        print("\n----- Delivery Agent Details -----")
        print(f"Agent Name: {self.name}")
        print(f"Agent ID: {self.agent_id}")
        print(f"Mobile: {self.mobile}")

        #if self.available:
            #print("Status: Available")
        #else:
            #print("Status: Assigned")


# =========================================================
# PACKAGE CLASS
# =========================================================

class Package:

    def __init__(self, package_id, product, weight, price):

        self.package_id = package_id
        self.product = product
        self.weight = weight
        self.price = price

    def package_details(self):

        print("\n----- Package Details -----")
        print(f"Package ID: {self.package_id}")
        print(f"Product: {self.product}")
        print(f"Weight: {self.weight} KG")
        print(f"Price: ₹{self.price}")


# =========================================================
# SHIPMENT CLASS
# =========================================================

class Shipment:

    def __init__(self,shipment_id,customer,package,from_loc,to_loc,expected_delivery):

        self.shipment_id = shipment_id
        self.customer = customer
        self.package = package
        self.from_loc = from_loc
        self.to_loc = to_loc
        self.expected_delivery = expected_delivery

        self.status = "Shipment Created"

        self.agent = None

        self.delivery_charge = self.calculate_charge()

        self.delivery_history = ["Shipment Created"]
        self.created_at = datetime.now()


    # =====================================================
    # SHIPPING CHARGE
    # =====================================================

    def calculate_charge(self):

        if self.package.price > 500:
            return 0
        else:
            return 100


    # =====================================================
    # ASSIGN DELIVERY AGENT
    # =====================================================

    def assign_agent(self, agent):

        if agent.available:

            self.agent = agent

            agent.available = False
            
            #print('shipment found')

            print("\nDelivery agent assigned successfully.")
            print(f"Agent Name: {agent.name}")
            print(f"Agent ID: {agent.agent_id}")

        else:

            print("\nAgent is already assigned.")


    # =====================================================
    # UPDATE DELIVERY STATUS
    # =====================================================

    def update_status(self, new_status):

        self.status = new_status

        self.delivery_history.append(new_status)

        print("\nDelivery status updated.")
        print("Current Status:", self.status)

        if new_status == "Delivered":

            if self.agent is not None:

                self.agent.available = True
                

            print("Shipment delivered successfully.")


    # =====================================================
    # SHOW SHIPMENT DETAILS
    # =====================================================

    def shipment_details(self):

        print("\n======================================")
        print("          SHIPMENT DETAILS")
        print("======================================")

        print(f"Shipment ID: {self.shipment_id}")

        print(f"Customer ID: {self.customer.customer_id}")

        print(f"Customer Name: {self.customer.name}")

        print(f"Customer Mobile No. is: {self.customer.mobile}")

        print(f"Customer Address: {self.customer.address}")

        print(f"Product: {self.package.product}")

        print(f"Package ID: {self.package.package_id}")

        print(f"Weight: {self.package.weight} KG")

        print(f"From Location: {self.from_loc}")

        print(f"To Location: {self.to_loc}")

        print(f"Product Price: ₹{self.package.price}")
        
        print(
    f"Created Date & Time: "
    f"{self.created_at.strftime('%d-%m-%Y %I:%M:%S %p')}")


        if self.delivery_charge == 0:

            print("Delivery Charge: FREE")

        else:

            print(f"Delivery Charge: ₹{self.delivery_charge}")

        print(f"Expected Delivery: " f"{self.expected_delivery}")

        print(f"Current Status: {self.status}")

        if self.agent is not None:

            print(f"Delivery Agent: {self.agent.name}")
            print(f"Agent ID: {self.agent.agent_id}")
            print(f"Agent Mobile No. is: {self.agent.mobile}")

        else:

            print("Delivery Agent: Not Assigned")

        print("======================================")


    # =====================================================
    # DELIVERY HISTORY
    # =====================================================

    def show_history(self):
       

        print("\n----- Delivery History -----")
        

        for number, status in enumerate(
            self.delivery_history,
            start=1
        ):
            

            print(number, ".", status)
            

    # =====================================================
    # SAVE TO TXT FILE
    # =====================================================

    def save_to_file(self):

        with open("delivery_history.txt","a", encoding="utf-8") as file:

            file.write(f"Shipment ID: {self.shipment_id}\n")

            file.write(f"Customer: {self.customer.name}\n")

            file.write(f"Product: {self.package.product}\n")

            file.write(f"From: {self.from_loc}\n")

            file.write(f"To: {self.to_loc}\n")

            file.write(f"Price: ₹{self.package.price}\n")

            file.write(f"Delivery Charge: " f"{self.delivery_charge}\n") 

            file.write(f"Expected Delivery: " f"{self.expected_delivery}\n")

            file.write(f"Status: {self.status}\n")

            file.write(f"History: " f"{self.delivery_history}\n")

            file.write("---------------------------------\n")


# =========================================================
# DELIVERY STATUS CHOICE
# =========================================================

def choose_delivery_status(shipment):

    status_options = {
        1: "Picked Up",
        2: "Shipped",
        3: "In Transit",
        4: "Out for Delivery",
        5: "Delivered"
    }

    while True:

        print("\nSelect Delivery Status")
        print("1. Picked Up")
        print("2. Shipped")
        print("3. In Transit")
        print("4. Out for Delivery")
        print("5. Delivered")

        try:
            choice = int(input("Enter Choice: "))

            if choice not in status_options:
                raise ValueError("Invalid status choice.")

            status = status_options[choice]

            # Update shipment status
            shipment.update_status(status)

            # Display shipment details
            shipment.shipment_details()

            # Stop when delivered
            if choice == 5:
                #print("\nSuccessfully Delivered!")
               
                break

        except ValueError as error:
            print("Error:", error)

# =========================================================
# CREATE OBJECTS WITH DIRECT VALUES
# =========================================================
'''
customer1 = Customer("Rahul","C101","9876543210","Hyderabad")
customer2 = Customer("venky","C102","1234567891","Vizag")


package1 = Package("P101","Laptop",2.5,45000)
package2 = Package("P102","Phone",0.5,15000)


agent1 = DeliveryAgent("Arun","9123456780","A101")
agent2 = DeliveryAgent("Ravi","9000056780","A102")


shipment1 = Shipment("S101",customer1,package1,"Hyderabad","Vizag","10-09-2026")
shipment2 = Shipment("S102",customer2,package2,"chennai","kerala","13-09-2026")

'''
# =========================================================
# STORE OBJECTS IN DICTIONARIES
# =========================================================

#customers[customer1.customer_id] = customer1
#customers["C102"]=customer2
'''
customers_list=[customer1,customer2]
customers={}
for customer in customers_list:
    customers[customer.customer_id]=customer
'''
customer1 = Customer("Rahul", "C101", "9876543210", "Hyderabad")
customer2 = Customer("Arun", "C102", "9123456780", "Vizag")
customer3 = Customer("Ravi", "C103", "9988776655", "Chennai")

customer_list = [customer1, customer2, customer3]

customers = {}

for customer in customer_list:
    customers[customer.customer_id] = customer
'''
packages[package1.package_id] = package1
packages[package2.package_id] = package2
'''
package1 = Package("P101", "Laptop", 2.5, 45000)
package2 = Package("P102", "Mobile", 0.5, 30000)
package3 = Package("P103", "Books", 3.0, 400)

package_list = [package1, package2, package3]

packages = {}

for package in package_list:
    packages[package.package_id] = package
'''
agents[agent1.agent_id] = agent1
agents[agent2.agent_id] = agent2
'''
agent1 = DeliveryAgent("Kiran", "9000000001", "A101")
agent2 = DeliveryAgent("Suresh", "9000000002", "A102")
agent3 = DeliveryAgent("Mahesh", "9000000003", "A103")

agent_list = [agent1, agent2, agent3]

agents = {}

for agent in agent_list:
    agents[agent.agent_id] = agent
'''
shipments[shipment1.shipment_id] = shipment1
shipments[shipment2.shipment_id] = shipment2

'''
shipment1 = Shipment("S101",customer1,package1,"Hyderabad","Vizag","10-09-2026")

shipment2 = Shipment("S102",customer2,package2,"Vizag","Chennai","12-09-2026")

shipment3 = Shipment("S103",customer3,package3,"Chennai","Bangalore","15-09-2026")

shipment_list = [shipment1, shipment2, shipment3]

shipments = {}

for shipment in shipment_list:
    shipments[shipment.shipment_id] = shipment



# ============================================================
# ASSIGN DELIVERY AGENT & UPDATE DELIVERY STATUS USING CHOICE
# =============================================================

for shipment, agent in zip(shipments.values(), agents.values()):
    print("Waiting for Agents......")
    time.sleep(2)
    
    shipment.assign_agent(agent)
    #print("Waiting for Agents......")
    print(shipment.shipment_id,"→",shipment.status)
    print()
    time.sleep(2)
    
# Display all shipment statuses
for shipment in shipments.values():
    choose_delivery_status(shipment)
# =========================================================
# SHOW SHIPMENT DETAILS
# =========================================================

shipment1.shipment_details()
shipment2.shipment_details()
shipment3.shipment_details()

# =========================================================
# SHOW DELIVERY HISTORY
# =========================================================
'''
shipment1.show_history()
shipment2.show_history()
shipment3.show_history()
'''

for shipment in shipments.values():

    shipment.show_history()


# =========================================================
# SAVE SHIPMENT
# =========================================================
'''
shipment1.save_to_file()
shipment2.save_to_file()
shipment3.save_to_file()
'''

# =========================================================
# SAVE ALL SHIPMENTS
# =========================================================

for shipment in shipments.values():
    shipment.save_to_file()

print("\nShipment saved successfully.")
print("Thanks for Shopping... Visit Again ❤️")
#print(type(shipments))


# It is only for finding the shipment details using shipment_id

def track_shipment(shipments):

    while True:

        shipment_id = input(
            "\nEnter Shipment ID (or type EXIT to stop): "
        ).upper()

        if shipment_id == "EXIT":
            print("\nShipment tracking ended.")
            break

        try:
            shipment = shipments[shipment_id]

            print("\nShipment Found!")
            shipment.shipment_details()

            print("\n----- Delivery History -----")
            shipment.show_history()

        except KeyError:
            print("\nError: Shipment ID not found.")

track_shipment(shipments)


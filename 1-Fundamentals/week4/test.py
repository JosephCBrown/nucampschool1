class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        for x in self.items:
            print(x)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, we do not have that flavor. Please choose another.")
            return
        if scoops not in range(1, 4):
            print("Select scoops between one, two, or three scoops.")
            return
        print("Order created!")
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("")
        print("All Pending Ice Cream Orders:")
        for x in self.orders.items:
            print(
                "Customer:",
                x["customer"],
                "-- Flavor:",
                x["flavor"],
                "-- Scoops:",
                x["scoops"],
            )

    def next_order(self):
        NextOrder = self.orders.dequeue()
        print("")
        print("Next order up!")
        print(
            "Customer:",
            NextOrder["customer"],
            "-- Flavor:",
            NextOrder["flavor"],
            "-- Scoops:",
            NextOrder["scoops"],
        )


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()

last_id = 1


class Item:
    def __init__(self, name:str, price:float) -> None:
        self.name = name
        self.price = price


    def __str__(self) -> str:
        return f"Item name - {self.name}, item price - {self.price}"


class Vehicle:
    def __init__(self, number:int) -> None:
        self.number = number
        self.is_available = True


class Location:
    def __init__(self, city:str, postoffice:int) -> None:
        self.city = city
        self.postoffice = postoffice


class Order:
    def __init__( self, user_name:str, city:str, postoffice:int, items:list) -> None:
        global last_id
        self.order_id = last_id
        last_id += 1
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None
        print(f"Your order number is {self.order_id}")


    def calculate_amount(self) -> float:
        total_amount = 0
        for item in self.items:
            total_amount += item.price
        return total_amount
    

    def assign_vehicle(vehicle: Vehicle) -> None:
        vehicle.is_available = False


    def __str__(self) -> str:
        if self.vehicle == None:
            return "There is no available vehicle to deliver an order."
        else:
            return f"Your order #{self.order_id} is sent to {self.location.city}. Total price: {self.calculate_amount()} UAH."

class LogisticSystem:
    def __init__(self, vehicles: list) -> None:
        self.orders = []
        self.vehicles = vehicles


    def placeOrder(self, order: Order) -> None:
        for vehicle in self.vehicles:
            if vehicle.is_available:
                order.vehicle = vehicle
                vehicle.is_available = False
                self.orders.append(order)
                return
        print(order)      



    def trackOrder(self, id:int) -> None:
        for order in self.orders:
            if order.order_id == id:
                print(order)
                return
        print("No such order.")

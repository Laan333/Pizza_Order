print("Welcome to Python Pizza Deliveries!")

my_size_pizza_list = []
check = 0 #Balance
MY_DICT_PIZZA = {"S":15,"M":20,"L":25}
MY_DICT_PEPPERONI={"S":2,"M":3,"L":3}
CHEESE = 1
total = 0

def check_pizza_size():
    global check
    size = input("What size pizza do you want? S, M, or L ")
    all_sizes = MY_DICT_PIZZA.keys()
    if size in all_sizes:
        my_size_pizza_list.append(size)
        check += MY_DICT_PIZZA[size]
    else:
        print("PIZZA SIZE NOT FOUND, ERROR")
        check_pizza_size()

def peperoni_data():
    global check
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni == "Y":
        check += MY_DICT_PEPPERONI[my_size_pizza_list[0]]
    else:
        return "Peperoni not needed"

def cheese_data():
    global check
    extra_cheese = input("Do you want extra cheese? Y or N ")
    if extra_cheese == "Y":
        check += CHEESE
    else:
        return "Extra cheese not needed"
def main():
    check_pizza_size()
    peperoni_data()
    cheese_data()
if __name__ == '__main__':
    main()
    print(f"Total bill: {check}")



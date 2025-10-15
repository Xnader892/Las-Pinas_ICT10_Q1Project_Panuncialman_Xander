from pyscript import display

restaurant_name = "Manong Pio's Sweet Tarts"
owner_name = "Xander Panuncialman"

year_since = 1990

tax_rate = 0.10

has_delivery = True
is_dine_in = True
is_takeaway = True

product_names = ["Strawberry tart", "Apple tart", "Butter tarts", "Lemon tart", "Chocolate tart"]
beverages = ["Sago't Gulaman", "Halo-Halo"]

menu = {
    "Strawberry tart": 359,
    "Apple tart": 359,
    "Butter tarts": 399,
    "Lemon tart": 359,
    "Chocolate tart": 399,
    "Sago't Gulaman": 80,
    "Halo-Halo": 80
}

common_allergens = {"dairy", "gluten"}

display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display("Menu Pricelist", target="heading1")

display(product_names[0], target="prod1")
display(f"₱{menu['Strawberry tart']}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Apple tart']}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Butter tarts']}", target="price3")
display(product_names[3], target="prod4")
display(f"₱{menu['Lemon tart']}", target="price4")
display(product_names[4], target="prod5")
display(f"₱{menu['Chocolate tart']}", target="price5")
display(beverages[0], target="prod6")
display("₱" + str(menu["Sago't Gulaman"]), target="price6")
display(beverages[1], target="prod7")
display("₱" + str(menu["Halo-Halo"]), target="price7")


display("Open: 7:00am - 5:00pm", target="business_hours")
display("Dine-in Available", target="ordertype")

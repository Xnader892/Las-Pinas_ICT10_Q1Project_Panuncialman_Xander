from pyscript import document, display

def create_order(e):

    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")
    item6 = document.getElementById("item6")
    item7 = document.getElementById("item7")


    total = (
        float(item1.value) * int(item1.checked) +
        float(item2.value) * int(item2.checked) +
        float(item3.value) * int(item3.checked) +
        float(item4.value) * int(item4.checked) +
        float(item5.value) * int(item5.checked) +
        float(item6.value) * int(item6.checked) +
        float(item7.value) * int(item7.checked)
    )


    customer_name = document.getElementById("customer").value
    customer_address = document.getElementById("address").value
    contact_number = document.getElementById("contact_number").value


    display(f"Order for: {customer_name}", target="order_output1")
    display(f"Address: {customer_address}", target="order_output2")
    display(f"Contact number: {contact_number}", target="order_output3")
    display(f"Total: ₱ {total:.2f}", target="show")


has_delivery = True
is_dine_in = True
is_takeaway = True


business_hours = ("7:00 AM", "5:00 PM")


display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openinghours")
display("Dine-in Available", target="orderType")

print("======Welcome to tea kottu babai=====")
print("add items to the cart,enter exit to exit the application")
total_amount=0
condition=True
while(condition):
    item=input("enter item:")
    item=item.lower().strip()
    if item=="exit":
        condition=False
    elif item in ['tea','coffee']:
        total_amount+=10
        print("item added to the cart")
    elif item in ['ginger tea','black coffee']:
        total_amount+=15
        print("item added to the cart")
    elif not item:
        print("item is empty")
    else:
        print("enter valid item")
print("total amount:",total_amount)
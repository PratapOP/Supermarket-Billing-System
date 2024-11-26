# Supermarket-Billing-System
This C++ program simulates a grocery store management system where customers can browse and purchase grocery items, while shop owners can manage the inventory. The system includes a GroceryItem class for representing items such as fruits, vegetables, and daily essentials with names and prices. The GroceryStore class manages the items, allowing owners to add, remove, or edit items, and customers to add items to their cart and check out. The program allows two user roles: a customer who can shop and a shop owner who can manage the store's inventory. The user interface is menu-driven, and prices are displayed in rupees.
To use the grocery store management system, follow these steps:

## Compile the Program: First, you need to compile the C++ code. Use a C++ compiler like g++:

- g++ -o grocery_store grocery_store.cpp
### Run the Program: Once compiled, run the executable:

## Choose Your Role:
When prompted, choose your role by entering:
1 for Customer to shop for groceries.
2 for Shop Owner to manage the store inventory.
0 to exit the program.
As a Customer:

Browse the store's items by selecting the item number (e.g., enter 1 for Apple, 2 for Banana, etc.).
The price of each item will be added to your total bill.
To checkout and see the total bill, select 0.
As a Shop Owner:

Enter the owner's password (owner123).
Choose an option to:
1 to add a new item to the store.
2 to remove an item.
3 to edit an item's price.
4 to view the current inventory.
0 to exit store management.
The program will run continuously until you choose to exit by entering 0.

# Capstone Module 1 - Warehouse Management CRUD Project

## Context
This program is designed to manage a warehouse database, including displaying the database, creating new stock items, updating warehouse data, and deleting entries.

## Business Task
This project addresses the need for an efficient warehouse management system. It is designed to help businesses—regardless of their industry—manage inventory data more efficiently. The system can be applied to various types of warehouses, such as those in the food and beverage industry, supermarkets, retail stores, distribution centers, and manufacturing facilities. By streamlining stock data handling, the program improves data accuracy, reduces manual work, and helps warehouse staff manage stock more easily.

## Key Features
### Read (Menu 1 - Display Data)
Display all records or search for specific data by SKU or item name, with results presented using the Tabulate library for better readability.
- Display All Data
- Search Data
- Return to Main Menu
  
### Create (Menu 2 - Add New Item)
Create new stock entries by providing the SKU, item name, unit, and stock quantity. The category and location will be automatically generated based on the SKU.
- Add Data
- Return to Main Menu

### Update (Menu 3 - Update Data)
Update existing records by editing the SKU, item name, stock quantity, or unit as needed.
- Update Data
- Return to Main Menu

### Delete (Menu 4 - Delete & Restore Data)
Delete data by entering an existing SKU. A restore feature is also available to recover previously deleted data.
- Delete Data
- Restore Data
- Return to Main Menu

## Objectives
This program offers efficient solutions for managing warehouse databases. It helps reduce manual work and minimize human error, making it easier for warehouse staff to handle stock operation effectively.

## Stakeholders
- Warehouse Staff: For updating stock data, checking item availability, and recording incoming or outgoing goods.
- Inventory Controller: For monitoring stock levels, ensuring data accuracy, and identifying discrepancies in inventory.
- Store Manager: For overseeing inventory flow, making decisions based on stock availability, and coordinating with other departments.
- Business Owners: For managing stock in a simple and organized way without needing complex systems.
- IT Support / System Administrators: Maintain the system’s performance, handle technical issues, and ensure data security and backup.
  
## Limitations
- Input validation for item name and unit prevents numeric-only input, but there is no standardization to avoid typos or unclear entries. These can still be corrected manually through the update menu.
- The system only tracks stock on hand; usage history and transaction data are not included, leaving room for future improvements.
  
## Data Summary

| Attribute        | Type          | Description                                                                                                 |
|------------------|---------------|-------------------------------------------------------------------------------------------------------------|
| No               | Integer        | Item number in the database is auto-incremented.                                                            |
| nama_barang      | String         | Full item name stored in the warehouse.                                                                     |
| sku              | String         | Unique item code (Stock Keeping Unit / SKU), consisting of the category ('RM' for Raw Material, 'SC' for Supply & Consumable, and 'FG' for Finished Good), location (e.g., A01), and a unique identifier. |
| kategori         | String         | Item type based on the SKU, such as Raw Material, Finished Good, or Supply & Consumable.                   |
| stok             | Float          | Quantity of stock available in the warehouse.                                                               |
| satuan           | String         | Unit of measurement for the stock, such as kg, pcs, box, etc.                                               |
| lokasi           | String         | Warehouse storage location code, derived from the SKU structure.                                            |
| tanggal_update   | String (Date)  | The date when the item data was last modified or updated, in YYYY-MM-DD format.                             |


## User Instructions
  1. Before running the program, install the required library: pip install tabulate.
  2. Run the program in your Python environment.
  3. When prompted, enter the password 'warehouse123' to access the main menu.
  4. Follow the on-screen menu to manage warehouse data such as viewing, adding, updating, or deleting stock entries.

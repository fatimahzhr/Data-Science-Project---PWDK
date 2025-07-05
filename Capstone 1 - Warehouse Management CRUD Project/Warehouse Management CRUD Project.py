# ========================= IMPORT THE LIBRARY =========================
from tabulate import tabulate
from datetime import date
import sys

# ========================= DEFINE THE INITIAL DATABASE =========================
warehouse_data = [
    {   "No": 1,
        "nama_barang": "Tepung Terigu Protein Tinggi",
        "sku": "RMA01001",
        "kategori": "Raw Material",
        "stok": 40,
        "satuan": "kg",
        "lokasi": "A01",
        "tanggal_update": "2025-05-25"
    },
    {   "No": 2,
        "nama_barang": "Gula Pasir Putih",
        "sku": "RMA02002",
        "kategori": "Raw Material",
        "stok": 70,
        "satuan": "kg",
        "lokasi": "A02",
        "tanggal_update": "2025-06-04"
    },
    {   "No": 3,
        "nama_barang": "Plastik Kemasan 30x40cm",
        "sku": "SCB01001",
        "kategori": "Supply & Consumable",
        "stok": 500,
        "satuan": "pack",
        "lokasi": "B01",
        "tanggal_update": "2025-05-31"
    },
    {   "No": 4,
        "nama_barang": "Sarung Tangan Plastik Sekali Pakai",
        "sku": "SCB02002",
        "kategori": "Supply & Consumable",
        "stok": 200,
        "satuan": "pcs",
        "lokasi": "B02",
        "tanggal_update": "2025-06-10"
    },
    {   "No": 5,
        "nama_barang": "Teh Botol 350ml",
        "sku": "FGC01001",
        "kategori": "Finished Good",
        "stok": 120,
        "satuan": "pcs",
        "lokasi": "C01",
        "tanggal_update": "2025-06-10"
    }
]


# ======================================= DEFINE THE HELPER FUNCTIONS =======================================

# Fungsi untuk input data SKU yang sudah ada
def input_existing_sku(prompt="Enter SKU: "): 
    sku = input(prompt).strip().upper()
    return sku

# Fungsi untuk mencari sesuai SKU yang diinput
def find_item_by_sku(sku):
    return next((item for item in warehouse_data if item["sku"] == sku), None)

# Fungsi untuk mengonfirmasi suatu kondisi/proses
def get_confirmation(prompt="Are you sure? (y/n): "):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        else:
            print("\033[91mInvalid input. Please enter 'y' or 'n'.\033[0m")
            
# Fungsi untuk mengurutkan ulang penomoran pada item
def reindex_warehouse_data():
    for idx, item in enumerate(warehouse_data, start=1):
        item["No"] = idx

# ======================================= MAIN MENU =======================================

def main_menu():
    while True:
        print("\033[1;34;43m" + "="*52 + "\033[0m")
        print("\033[1;34;43m{:^50}\033[0m".format("📦 WELCOME TO WAREHOUSE DATABASE 📦"))
        print("\033[1;34;43m" + "="*52 + "\033[0m")
        
        print("\n\033[94mMenu Options:\033[0m")
        print("1. 📋 Display Data")
        print("2. ➕ Add New Item")
        print("3. ✏️ Update Data")
        print("4. 🧹 Delete & Restore Data")
        print("5. ❌ Exit Program\n")
        print("\033[1;34m" + "="*52 + "\033[0m")

        try:
            menu_option = input("\nEnter a menu number [1-5]: ")
            if menu_option == '1':
                menu_1()
            elif menu_option == '2':
                menu_2()
            elif menu_option == '3':
                menu_3()
            elif menu_option == '4':
                menu_4()
            elif menu_option == '5':
                if menu_5():
                    break
            else:
                print("\033[1;91mInvalid choice. Please try again.\033[0m")
        except Exception as e:
            print(f"\033[91mAn unexpected error occurred: {e}\033[0m")


# ======================================= DISPLAY THE DATA =======================================
headers = {
    "No": "No",
    "nama_barang": "Nama Barang",
    "sku": "SKU",
    "kategori": "Kategori",
    "stok": "Stok",
    "satuan": "Satuan",
    "lokasi": "Lokasi",
    "tanggal_update": "Tanggal Update"
}

# Menampilkan seluruh data
def show_all_items():
    print("\n\033[1;30;46m{:^124}\033[0m\n".format("📋 ALL ITEMS IN WAREHOUSE 📋"))
    print(tabulate(warehouse_data, headers=headers, tablefmt="fancy_grid"))

# Menampilkan data berdasarkan pencarian SKU atau Item Name
def find_item():
    keyword = input_existing_sku("\n🔍 Enter SKU (e.g. RMA01001) or Item Name: ")
    results = []

    # Cek apakah input cocok dengan SKU persis
    results = [item for item in warehouse_data if item["sku"] == keyword]

    # Jika belum ditemukan, cari berdasarkan nama barang (mengandung keyword, case-insensitive)
    if not results:
        results = [item for item in warehouse_data if keyword.lower() in item["nama_barang"].lower()]

    if results:
        print("\n\033[1;36m📦 ITEM FOUND 📦\033[0m")
        print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
    else:
        print("\033[1;31m❌ No Data Found.\033[0m")

def menu_1():
    while True:
        print("\n\033[1;36;47m{:^90}\033[0m".format("📋 DISPLAY DATA MENU 📋"))
        print("\n1. Display All Data")
        print("2. Search Data")
        print("3. Return to Main Menu")
        print("\n\033[38;2;255;253;208m" + "="*92 + "\033[0m")

        choice_menu_1 = input("\nEnter your choice [1-3]: ")

        if choice_menu_1 == "1":
            show_all_items()
        elif choice_menu_1 == "2":
            find_item()
        elif choice_menu_1 == "3":
            print("\n\033[92mReturn to Main Menu...\033[0m\n")
            main_menu()
            break
        else:
            print("\033[91mInvalid input. Please choose 1, 2, or 3.\033[0m")


# ======================================= CREATE NEW STOCK ENTRY =======================================
def add_data():
    print("\n\033[1;34m=== Add New Item ===\033[0m")

    valid_categories = {
        'RM': 'Raw Material',
        'SC': 'Supply & Consumable',
        'FG': 'Finished Good'
    }

    valid_locations = ['A01', 'A02', 'B01', 'B02', 'C01', 'C02']  # Lokasi Penyimpanan yang Tersedia

    # SKU input & auto-parse kategori & lokasi
    while True:
        try:
            new_sku = input("\nEnter SKU (format >> category: RM/SC/FG + location: 'A01', 'A02', 'B01', 'B02', 'C01', 'C02  + code: 001, e.g. RMA01001): ").strip().upper()

            if len(new_sku) != 8: # SKU harus berjumlah 8 karakter
                print("\033[91mInvalid SKU! Must be exactly 8 characters.\033[0m")
                continue

            if not new_sku.isalnum(): # SKU harus merupakan alpha numeric
                print("\033[91mInvalid SKU! Only letters and numbers allowed.\033[0m")
                continue

            category = new_sku[:2]
            location_code = new_sku[2:5]
            unique_code = new_sku[5:]

            # Validasi kategori 
            if category not in valid_categories:
                print(f"\033[91mInvalid category code! Must be one of: {', '.join(valid_categories.keys())}.\033[0m")
                continue

            # Validasi lokasi
            if location_code not in valid_locations:
                print(f"\033[91mInvalid location code! Must be one of: {', '.join(valid_locations)}.\033[0m")
                continue

            # Validasi unique code
            if not unique_code.isdigit():
                print("\033[91mInvalid SKU! Last 3 digits must be numeric (e.g. 001).\033[0m")
                continue

            if any(item["sku"] == new_sku for item in warehouse_data): # SKU tidak boleh duplikat
                print("\033[91mSKU already exists. Please enter a different one.\033[0m")
                continue

            # Jika semua valid, ambil kategori dan lokasi dari SKU
            kategori = valid_categories[category]
            lokasi = location_code
            break

        except Exception as e:
            print(f"\033[91mError occurred during SKU input: {e}\033[0m")

    # Item Name
    while True:
        nama_barang = input("\nEnter item name: ").strip().capitalize()
        if not nama_barang or nama_barang.isdigit():
            print("\033[91mInvalid name. Must be non-empty and not only numbers.\033[0m")
        else:
            break

    # Unit
    while True:
        satuan = input("\nEnter unit (e.g. pcs, box): ").strip().lower()
        if not satuan or satuan.isdigit():
            print("\033[91mInvalid unit. Must be non-empty and not only numbers.\033[0m")
        else:
            break

    # Stock
    while True:
        stok_input = input("\nEnter stock (numeric): ").strip()
        try:
            stok = float(stok_input)
            if stok < 0:
                print("\033[91mStock must be a positive number.\033[0m")
            else:
                break
        except ValueError:
            print("\033[91mInvalid input. Please enter a numeric value.\033[0m")
    # Save
    new_item = {
        "No": len(warehouse_data) + 1,
        "sku": new_sku,
        "nama_barang": nama_barang,
        "kategori": kategori,
        "stok": stok,
        "satuan": satuan,
        "lokasi": lokasi,
        "tanggal_update": str(date.today())
    }

    # Saving Option
    if get_confirmation("\nSave this data? (y/n): "):
        warehouse_data.append(new_item)
        print("\n\033[92mData successfully saved!\033[0m")
    else:
        print("\n\033[93mSave cancelled. Returning to Create Data Menu.\033[0m")

def menu_2():
    while True:
        print("\n\033[1;34;47m{:^90}\033[0m".format("➕ CREATE DATA MENU ➕"))
        print("\n1. Add Data")
        print("2. Return to Main Menu")
        print("\n\033[1;34m" + "="*92 + "\033[0m")

        choice_menu_2 = input("\nEnter your choice [1-2]: ").strip()

        if choice_menu_2 == '1':
            add_data()
        elif choice_menu_2 == '2':
            print("\n\033[92mReturn to Main Menu...\033[0m\n")
            main_menu()
            break
        else:
            print("\033[91mInvalid input. Please choose 1 or 2.\033[0m")


# ======================================= MODIFY EXISTING DATA =======================================
def edit_data():
    print("\n\033[1;34m=== Edit Existing Item ===\033[0m")
    find_sku = input_existing_sku("\nEnter SKU to edit (e.g. RMA01001): ")

    # Mencari apakah item ada di data berdasarkan SKU
    item_found = find_item_by_sku(find_sku)  
    if not item_found:
        print("\033[91mData does not exist. Returning to Update Data Menu.\033[0m")
        return
        
    print("\n\033[1;36m📦 ITEM FOUND 📦\033[0m")
    print(tabulate([item_found], headers="keys", tablefmt="fancy_grid"))


    # Update Option 1
    if not get_confirmation("\nContinue to update? (y/n): "):
        print("\n\033[93mUpdate cancelled. Returning to Update Data Menu.\033[0m")
        return
    
    # Editable fields
    editable_fields = ["sku", "nama_barang", "stok", "satuan"]
    print("\n\033[1;34mEditable fields: " + ", ".join(editable_fields) + "\033[0m")


    # Input New Values/Data to the Editable Fields
    key_to_edit = input("Enter the field name you want to update: ").strip().lower()
    if key_to_edit not in editable_fields:
        print("\033[91mInvalid field. Returning to Update Data Menu.\033[0m")
        return

    try:
        if key_to_edit == "sku":
            valid_categories = {
                'RM': 'Raw Material',
                'SC': 'Supply & Consumable',
                'FG': 'Finished Good'
            }
            valid_locations = ['A01', 'A02', 'B01', 'B02', 'C01', 'C02']  # Lokasi Penyimpanan yang Tersedia

            while True:
                new_sku = input("Enter new SKU (e.g. RMA01001): ").strip().upper()

                if len(new_sku) != 8 or not new_sku.isalnum():
                    print("\033[91mInvalid SKU format. Must be 8 alphanumeric characters.\033[0m")
                    continue

                category_code = new_sku[:2]
                location_code = new_sku[2:5]
                code = new_sku[5:]

                if category_code not in valid_categories:
                    print(f"\033[91mInvalid category code. Must be one of: {', '.join(valid_categories)}\033[0m")
                    continue
                if location_code not in valid_locations:
                    print(f"\033[91mInvalid location code. Must be one of: {', '.join(valid_locations)}\033[0m")
                    continue
                if not code.isdigit():
                    print("\033[91mUnique code must be numeric.\033[0m")
                    continue
                if new_sku != item_found['sku'] and any(item["sku"] == new_sku for item in warehouse_data):
                    print("\033[91mSKU already exists. Enter a different one.\033[0m")
                    continue

                val = new_sku
                kategori = valid_categories[category_code]
                lokasi = location_code
                break

        elif key_to_edit == "nama_barang":
            while True:
                val = input("\nEnter new item name: ").strip().capitalize()
                if not val or val.isdigit():
                    print("\033[91mInvalid name. Must be non-empty and not only numbers.\033[0m")
                else:
                    break

        elif key_to_edit == "stok":
            while True:
                stok_input = input("\nEnter new stock (numeric): ").strip()
                try:
                    val = float(stok_input)
                    if val < 0:
                        print("\033[91mStock must be positive.\033[0m")
                    else:
                        break
                except ValueError:
                    print("\033[91mInvalid stock input.\033[0m")

        elif key_to_edit == "satuan":
            while True:
                val = input("\nEnter new unit (e.g. pcs): ").strip().lower()
                if not val or val.isdigit():
                    print("\033[91mInvalid unit.\033[0m")
                else:
                    break


        # Update Option 2
        if get_confirmation(f"Update {key_to_edit}? (y/n): "):
            item_found[key_to_edit] = val
            item_found["tanggal_update"] = str(date.today())
            

            # Auto-update kategori & lokasi jika SKU diedit
            if key_to_edit == "sku":
                item_found["kategori"] = kategori
                item_found["lokasi"] = lokasi

            print("\n\033[92mData successfully updated!\033[0m")
        else:
            print("\033[93mUpdate cancelled.\033[0m")
    
    except Exception as e:
        print(f"\033[91mUnexpected error: {e}\033[0m")


def menu_3():
  while True:
        print("\n\033[1;32;47m{:^90}\033[0m".format("✏️ UPDATE DATA MENU ✏️"))
        print("\n1. Edit Data")
        print("2. Return to Main Menu")
        print("\n\033[1;32m" + "="*92 + "\033[0m")

        choice_menu_3 = input("\nEnter your choice [1-2]: ").strip()

        if choice_menu_3 == '1':
            edit_data()
        elif choice_menu_3 == '2':
            print("\n\033[92mReturn to Main Menu...\033[0m\n")
            main_menu()
            break
        else:
            print("\033[91mInvalid input. Please choose 1 or 2.\033[0m")

# ======================================= DELETE EXISTING DATA =======================================
deleted_items = [] 
def delete_data():
    print("\n\033[1;34m=== Delete Existing Item ===\033[0m")
    find_sku = input_existing_sku("Enter SKU to Delete (e.g. RMA01001): ")

    item_found = find_item_by_sku(find_sku)
    if not item_found:
        print("\033[91mData does not exist. Returning to Delete Data Menu.\033[0m")
        return

    print("\n\033[1;36m📦 ITEM FOUND 📦\033[0m")
    print(tabulate([item_found], headers="keys", tablefmt="fancy_grid"))

    if get_confirmation("\nDelete this data? (y/n): "):
        warehouse_data.remove(item_found)
        deleted_items.append(item_found)
        reindex_warehouse_data()  # Perbarui No
        print("\n\033[92mData successfully deleted!\033[0m")
    else:
        print("\n\033[93mDelete cancelled. Returning to Delete Data Menu.\033[0m")



def restore_data():
    if not deleted_items:
        print("\n\033[93mNo deleted data to restore.\033[0m")
        return

    # Tampilkan deleted items dengan No sementara
    temp_deleted_display = []
    for i, item in enumerate(deleted_items, start=1):
        row = item.copy()
        row["No"] = i
        temp_deleted_display.append(row)

    print("\n\033[1;36m🗃️ LIST OF DELETED ITEMS 🗃️\033[0m")
    print(tabulate(temp_deleted_display, headers="keys", tablefmt="fancy_grid"))

    sku_to_restore = input_existing_sku("\nEnter SKU to restore: ")
    item_to_restore = next((item for item in deleted_items if item["sku"] == sku_to_restore), None)

    if not item_to_restore:
        print("\033[91mSKU not found in deleted items.\033[0m")
        return

    print("\n\033[1;36m📦 ITEM TO BE RESTORED 📦\033[0m")
    print(tabulate([item_to_restore], headers="keys", tablefmt="fancy_grid"))

    if get_confirmation("Restore this item? (y/n): "):
        restored_item = item_to_restore.copy()
        restored_item["No"] = len(warehouse_data) + 1
        warehouse_data.append(restored_item)
        deleted_items.remove(item_to_restore)
        print("\n\033[92mData successfully restored!\033[0m")
    else:
        print("\n\033[93mRestore cancelled. Returning to Delete Data Menu.\033[0m")



def menu_4():
    while True:
        print("\n\033[1;31;47m{:^90}\033[0m".format("🧹 DELETE DATA MENU 🧹"))
        print("\n1. Delete Data")
        print("2. Restore Deleted Item")
        print("3. Return to Main Menu")
        print("\n\033[1;31m" + "="*92 + "\033[0m")

        choice_menu_4 = input("\nEnter your choice [1-3]: ").strip()

        if choice_menu_4 == '1':
            delete_data()
        elif choice_menu_4 == '2':
            restore_data()
        elif choice_menu_4 == '3':
            print("\n\033[92mReturning to Main Menu...\033[0m\n")
            main_menu()
            break
        else:
            print("\033[91mInvalid input. Please choose 1, 2, or 3.\033[0m")


# ======================================= EXIT THE PROGRAM =======================================
def menu_5():
    while True:
        if get_confirmation("\nAre you sure you want to exit? (y/n): "):
            print("\n\033[92mProgram Closed. Goodbye! 👋\033[0m")
            sys.exit()
        else:
            print("\n\033[93mExit cancelled. Returning to Main Menu...\033[0m")
            return 

# ======================================= LOGIN TO PROGRAM =======================================

# Input Credential to login to program
def login():
    max_attempts = 5  # User diberikan limit sebanyak 5x untuk percobaan login
    
    while True:
        attempts = 0
        while attempts < max_attempts:
            input_pw = input("\nInput password here: ")
            if input_pw == 'warehouse123':
                print("\033[92mLogin successful. Welcome!\033[0m")
                main_menu()
                return
            else:
                attempts += 1
                remaining = max_attempts - attempts
                print(f"\033[1;91mIncorrect password. {remaining} attempt(s) remaining.\033[0m\n")

        # Jika sudah 5x gagal, program akan meminta konfirmasi dari user untuk mencoba login ulang
        if not get_confirmation("\nMaximum attempts reached. Do you want to try logging in again? (y/n): "):
            print("\n\033[92mProgram Closed. Goodbye! 👋\033[0m") # Jika user tidak ingin mencoba login ulang, maka program akan berhenti
            return
login()

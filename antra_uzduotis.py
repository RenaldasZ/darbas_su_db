import sqlite3

# connect to the database and create a cursor
with sqlite3.connect("antra_uzduotis.db") as conn:
    cursor = conn.cursor()

# define the main loop for the program
while True:
    print("""Automobiliai
    1 - paieska pagal automobilio pavadinima
    2 - Automobilio iterpimas
    3 - ieškoti įrašų pagal visus stulpelius
    4 - iseiti
    """)
    choice = input("pasirinkite: ")

    if choice == "1":
        # ask for the make of the car to search for
        car_make = input("Automobilio pavadinimas: ")

        # execute the query to find cars with the specified make
        cursor.execute('SELECT * FROM antra_uzduotis WHERE make = ?', (car_make,))
        results = cursor.fetchall()

        if results:
            # if any results were found, print them out
            for row in results:
                print(row)
        else:
            print("tokiu automobiliu mes neturime..")

    elif choice == "2":
        # ask for details of the car to insert
        car_make = input("make: ")
        car_model = input("model: ")
        car_color = input("color: ")
        car_year = input("year: ")
        car_price = input("price: ")

        # execute the INSERT statement to add the new car to the database
        cursor.execute("""
            INSERT INTO antra_uzduotis
            (make, model, color, year, price)
            VALUES (?, ?, ?, ?, ?)
        """, (car_make, car_model, car_color, car_year, car_price))
        conn.commit()  # commit the changes to the database

        print("Automobilis ivestas.")

    elif choice == "3":
        # ask for search criteria
        make = input("make (press Enter to skip): ")
        model = input("model (press Enter to skip): ")
        color = input("color (press Enter to skip): ")
        year_from = input("year from (press Enter to skip): ")
        year_to = input("year to (press Enter to skip): ")
        price_from = input("price from (press Enter to skip): ")
        price_to = input("price to (press Enter to skip): ")

        # build the SQL query based on the user's search criteria
        query = "SELECT * FROM antra_uzduotis WHERE 1=1"
        params = []

        if make:
            query += " AND make = ?"
            params.append(make)

        if model:
            query += " AND model = ?"
            params.append(model)

        if color:
            query += " AND color = ?"
            params.append(color)

        if year_from:
            query += " AND year >= ?"
            params.append(year_from)

        if year_to:
            query += " AND year <= ?"
            params.append(year_to)

        if price_from:
            query += " AND price >= ?"
            params.append(price_from)

        if price_to:
            query += " AND price <= ?"
            params.append(price_to)

        # execute the query with the user's search criteria
        cursor.execute(query, tuple(params))
        results = cursor.fetchall()

        if results:
            # if any results were found, print them out
            for row in results:
                print(row)
        else:
            print("Nerasta jokiu automobiliu, atitinkanciu jusu paieskos kriterijus.")


        
    


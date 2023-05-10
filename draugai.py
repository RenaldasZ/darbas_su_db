import sqlite3
conn = sqlite3.connect("zmones.db")
c = conn.cursor()

while True:
    print("""Draugu katalogas
    1 - paieska pagal varda
    2 - iterpimas
    visa kita - iseiti
    """)
    choice = input("pasirinkite: ")
    if choice == "1":  
        vardas = input("Draugo vardas: ")
        with conn:
            # c.execute(f'SELECT * FROM draugai WHERE first_name = "{vardas}"')
            c.execute('SELECT * FROM draugai WHERE first_name = ?', (vardas, ))
            draugai = c.fetchall()

        if draugai and len(draugai) > 0:
            print(draugai)
        else:
            print("tokiu draugu mes neturim..")
    elif choice == "2":
        first_name = input("vardas: ")
        last_name = input("pavarde: ")
        email = input("email: ")
        with conn:
            c.execute("""INSERT INTO draugai
            (first_name, last_name, email)
            VALUES (?, ?, ?)""", (first_name, last_name, email))
        print(f"{first_name} ivestas.")
    else:
        break
c.close()
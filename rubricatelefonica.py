import tkinter as tk
import mysql.connector as xx
from tkinter import messagebox, simpledialog



# INIZIO CONNESSIONE
def connect_db():
   return     xx.connect(
   host="localhost", user="root" ,password="admin",database="rubrica")
    
 

# Funzione per aggiungere un contatto
def aggiungi_contatto(nome, telefono):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO contatti (nome, telefono) VALUES (%s, %s)"
    cursor.execute(sql, (nome, telefono))
    conn.commit()
    cursor.close()
    conn.close()
    print("Contatto aggiunto con successo!")

# Funzione per visualizzare tutti i contatti
def visualizza_contatti():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatti")
    for (id, nome, telefono) in cursor.fetchall():
        print(f"ID: {id}, Nome: {nome}, Telefono: {telefono}")
    cursor.close()
    conn.close()

# Funzione per cercare un contatto per nome
def cerca_contatto(nome):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "SELECT * FROM contatti WHERE nome LIKE %s"
    cursor.execute(sql, ('%' + nome + '%',))
    risultati = cursor.fetchall()
    if risultati:
        for (id, nome, telefono) in risultati:
            print(f"ID: {id}, Nome: {nome}, Telefono: {telefono}")
    else:
        print("Nessun contatto trovato.")
    cursor.close()
    conn.close()

# FINE CONNESSIONE

contatti = {}

def cerca_persona():
    nome = simpledialog.askstring("Cerca", "Inserisci il nome della persona da cercare:")
    if nome:
        if nome in contatti:
            messagebox.showinfo("Risultato della ricerca", "Contatto Esistente. ")
        else:
            messagebox.showinfo("Risultato della ricerca", "Contatto Non Esistente.")

def visualizza_contatti():
    if contatti:
        contatti_string = "\n".join([f"{nome}: {numero}" for nome, numero in contatti.items()])
        messagebox.showinfo("Contatti salvati", contatti_string)
    else:
        messagebox.showinfo("Contatti salvati", "Nessun contatto disponibile.")

def aggiungicontatto():
    nome = simpledialog.askstring("Aggiungi", "Inserisci il nome della persona:")
    
    if nome:
        numero = simpledialog.askstring("Aggiungi", "Inserisci il numero di telefono:")
        if numero:
            aggiungi_contatto(nome, numero)
            contatti[nome] = numero
            messagebox.showinfo("Contatto aggiunto", f"Contatto {nome} aggiunto con successo.")


root = tk.Tk()
root.title("Gestione Contatti")


bottone_cerca = tk.Button(root, text="Cerca", command=cerca_persona)
bottone_cerca.pack(pady=10)

bottone_visualizza = tk.Button(root, text="Visualizza", command=visualizza_contatti)
bottone_visualizza.pack(pady=10)

bottone_aggiungi = tk.Button(root, text="Aggiungi", command=aggiungicontatto)
bottone_aggiungi.pack(pady=10)

root.mainloop()
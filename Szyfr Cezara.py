import tkinter as tk
from tkinter import messagebox

polish_alphabet = [
    'A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 
    'O', 'Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż',
]
numbers = [ "0" , "1" , "2" , "3", "4", "5", "6", "7", "8", "9"]


#Sprawdza, czy wszystkie znaki wprowadzone przez użytkownika znajdują się na podanej liście znaków.
def contains_only_letters(user_input, char_list):
    counter = 0
    for char in user_input:
        if char in char_list:
            counter += 1
    return counter == len(user_input)

#Szyfruje wprowadzone znaki, przesuwając je o określoną liczbę pozycji w alfabecie.
def encryption(user_input, char_list, jump):
    encrypted_text = ""
    for letter in user_input:
        if letter in char_list:
            index = char_list.index(letter)
            new_index = (index + jump) % len(char_list)  # Użycie % dla zawijania
            encrypted_text += char_list[new_index]  # Zmiana okrągłych nawiasów na kwadratowe
        else:
            encrypted_text += letter  # Dodaj niezmieniony znak, jeśli nie jest w alfabecie
    return encrypted_text

#Szyfruje wprowadzone znaki, przesuwając je o określoną liczbę pozycji w alfabecie.
def dencryption(user_input, char_list, jump):
    dencrypted_text = ""
    for letter in user_input:
        if letter in char_list:
            index = char_list.index(letter)
            new_index = (index - jump) % len(char_list)  # Użycie % dla zawijania
            dencrypted_text += char_list[new_index]  # Zmiana okrągłych nawiasów na kwadratowe
        else:
            dencrypted_text += letter  # Dodaj niezmieniony znak, jeśli nie jest w alfabecie
    return dencrypted_text
def isnumber(number):
    counter = 0
    for digit in numbers:
        for num in number:
            if digit==num:
                counter += 1
    if len(number) == counter:
        return True
    else:
        return False

#Funkcja przycisku do szyfrowania
def on_submit1():
    encrypted_message = text_area_encrypt.get("1.0", tk.END).strip()  # Pobieranie tekstu z pola
    if contains_only_letters(encrypted_message.upper(), polish_alphabet):
        jump_value = jump.get("1.0", tk.END).strip()
        if isnumber(jump_value):
            encrypted_text = encryption(encrypted_message.upper(), polish_alphabet, int(jump_value))
            text_area_decrypt.delete("1.0", tk.END)  # Wyczyść pole tekstowe przed wyświetleniem nowego tekstu
            text_area_decrypt.insert(tk.END, encrypted_text)  # Wstaw zaszyfrowany tekst do pola
            messagebox.showinfo("ERROR", "Wykonano")
        else:
            messagebox.showinfo("ERROR", "Zła wartość skoku")
    else:
        messagebox.showinfo("ERROR", "Niepoprawne dane")

#Funkcja przycisku do deszyfrowania
def on_submit2():
    decrypted_message = text_area_decrypt.get("1.0", tk.END).strip()  # Pobieranie tekstu z pola
    if contains_only_letters(decrypted_message.upper(), polish_alphabet):
        jump_value = jump.get("1.0", tk.END).strip()
        if isnumber(jump_value):
            decrypted_text = dencryption(decrypted_message.upper(), polish_alphabet, int(jump_value))
            text_area_encrypt.delete("1.0", tk.END)  # Wyczyść pole tekstowe przed wyświetleniem nowego tekstu
            text_area_encrypt.insert(tk.END, decrypted_text)  # Wstaw zaszyfrowany tekst do pola
            messagebox.showinfo("ERROR", "Wykonano")
        else:
            messagebox.showinfo("ERROR", "Zła wartość skoku")
    else:
        messagebox.showinfo("ERROR", "Niepoprawne dane")

# Utworzenie głównego okna
root = tk.Tk()
root.title("Aplikacja Kodu Cezara")
root.geometry("600x700+450+50")

# Utworzenie etykiety
label = tk.Label(root, text="Odszyfrowana wiadomość:")
label.pack(pady=10)

# Utworzenie pola do szyfrowania
text_area_encrypt = tk.Text(root, height=10, width=40)
text_area_encrypt.pack(pady=10)

# Utworzenie przycisku
encrypting = tk.Button(root, text="Szyfruj", command=on_submit1)
encrypting.pack(pady=10)

#Utworzenie utykiety i pola do skoku
label_jump = tk.Label(root, text="Podaj ilość skoków do szyfru:")
label_jump.pack(pady=10)
jump = tk.Text(root,height=2, width=5)
jump.pack(pady=10)

# Utworzenie etykiety
label = tk.Label(root, text="Zaszyfrowana wiadomość:")
label.pack(pady=10)

# Utworzenie pola do deszyfrowania
text_area_decrypt = tk.Text(root, height=10, width=40)
text_area_decrypt.pack(pady=10)

# Utworzenie przycisku
decription = tk.Button(root, text="Deszyfruj", command=on_submit2)
decription.pack(pady=10)

# Uruchomienie pętli głównej aplikacji
root.mainloop()

import customtkinter

app = customtkinter.CTk()
app.geometry("500x300")
app.title("Login")

def entrar():
    username = imput_user.get()
    password = imput_password.get()

    # Implementar validação e lógica de login aqui
    if username == "admin" and password == "password":  # exemplo simples
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha inválidos.")

text = customtkinter.CTkLabel(master=app, text='System Admin', font=("Roboto", 19))
text.pack(padx=10, pady=10)

imput_user = customtkinter.CTkEntry(master=app, placeholder_text="Usuario")
imput_user.pack(padx=10, pady=10)

imput_password = customtkinter.CTkEntry(master=app, placeholder_text="password", show="*")
imput_password.pack(padx=10, pady=10)

button_login = customtkinter.CTkButton(master=app, text="Login", command=entrar)
button_login.pack(padx=10, pady=10)

app.mainloop()
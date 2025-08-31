# Import customtkinter module
import customtkinter as ctk

# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("System")

# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("green")


# Create App class
class App(ctk.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("AppZomi")
        self.geometry("400x300")

        label_username = ctk.CTkLabel(master=self, text="Username")
        input_username = ctk.CTkTextbox(master=self, width=300, height=35)
        label_password = ctk.CTkLabel(master=self, text="Password")
        input_password = ctk.CTkTextbox(master=self, width=300, height=35)
        button_login = ctk.CTkButton(master=self, text="Login", command=self.submit_button_handler)

        label_username.pack(pady=(20, 0), padx=10)
        input_username.pack(pady=(0, 10), padx=10)
        label_password.pack(pady=0, padx=10)
        input_password.pack(pady=(0, 10), padx=10)
        button_login.pack(pady=10, padx=10)

    def submit_button_handler(self):
        print(self.command)


if __name__ == "__main__":
    app = App()
    app.mainloop()  # run the app

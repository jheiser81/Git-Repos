import tkinter as tk
from tkinter import messagebox
import requests
import random
import webbrowser
import threading

class GamePickerApp:
    def __init__(self):
        self.api_key = None
        self.steam_id = None
        
    # Get a list of all games owned by the user with the given Steam ID
    def get_all_games(self):
        try:
            url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={self.steam_id}&include_appinfo=true&format=json"
            response = requests.get(url)
            response.raise_for_status() # Raise an exception for invalid response
            data = response.json()['response']['games']
            return [{'name': game['name'], 'appid': game['appid'], 'playtime_forever': game['playtime_forever']} for game in data]
        except requests.exceptions.RequestException as e:
            tk.messagebox.showerror("Error", "An error occurred while fetching the game list. Please check your Steam ID and API key and try again.")
            return []

    # Get a list of unplayed games owned by the user with the given Steam ID
    def get_unplayed_games(self):
        all_games = self.get_all_games()
        return [game for game in all_games if game['playtime_forever'] == 0]

    # Suggest a random game from the list of unplayed games
    def suggest_game(self, games):
        game = random.choice(games)
        return game

    # Validate the Steam Id
    def validate_steam_id(self, steam_id):
        if steam_id.isdigit() and len(steam_id) == 17:
            return True
        else:
            return False
    
    # Validate the Steam API key
    def validate_api_key(self, api_key):
        if api_key.isalnum() and len(api_key) == 32:
            return True
        else:
            return False
        
    # Create a function to hide the widgets and display the game type selection widgets
    def show_game_type_selection(self):
        # Hide widgets
        self.welcome_message.pack_forget()
        self.steam_id_label.pack_forget()
        self.steam_id_entry.pack_forget()
        self.api_key_label.pack_forget()
        self.api_key_entry.pack_forget()
        self.submit_button_1.pack_forget()
            
        # Display game type selection widgets
        self.instructions_message.pack()
        self.all_games_radio.pack()
        self.unplayed_games_radio.pack()
        self.submit_button_2.pack()
        
    # Function to create the GUI for the game picker application           
    def create_gui(self):

        # Create the main window
        self.window = tk.Tk()
        self.window.title("Random Game Picker")
        
        # Display a welcome message and instructions
        self.welcome_message = tk.Label(self.window, text="Welcome to the Random Game Picker!\n\nEnter your Steam ID and API key to get started.\n\nTo find your Steam ID, open the Steam client, click on your profile name, and then click on Account Details.\nYour Steam ID will be displayed under your profile name. Copy and paste it into the box below.\n\nTo get your Steam API key, visit https://steamcommunity.com/dev/apikey and follow the instructions to generate a new API key.\nUnder 'Domain Name', enter 'localhost' and click 'Create'. Copy the API key and paste it into the text box below.")
        self.welcome_message.pack()
        
        # Create labels and entry fields for the Steam ID and API key
        self.steam_id_label = tk.Label(self.window, text="Steam ID:")
        self.steam_id_entry = tk.Entry(self.window)
        self.api_key_label = tk.Label(self.window, text="API Key:")
        self.api_key_entry = tk.Entry(self.window)
    
        # Pack the labels and entry fields
        self.steam_id_label.pack()
        self.steam_id_entry.pack()
        self.api_key_label.pack()
        self.api_key_entry.pack()
        
        # Create a submit button to fetch the Steam ID and API key from the entry fields
        self.submit_button_1 = tk.Button(self.window, text="Submit", command=self.show_game_type_selection, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
        self.submit_button_1.pack(pady=10)
    
        # Create the game type selection widgets, but hide them initially
        self.instructions_message = tk.Label(self.window, text="Select from ALL your games or only UNPLAYED games, then click Submit to get a random game suggestion.")
        game_type_var = tk.StringVar(value='unplayed')
        self.all_games_radio = tk.Radiobutton(self.window, text='ALL games', variable=game_type_var, value='all')
        self.unplayed_games_radio = tk.Radiobutton(self.window, text='UNPLAYED games', variable=game_type_var, value='unplayed')
        
        # Create a submit button that fetches the game type and calls the on_submit function
        self.submit_button_2 = tk.Button(self.window, text="Submit", command=lambda: self.on_submit(game_type_var.get()), bg='blue', fg='white', font=('helvetica', 12, 'bold'))
        
        self.window.mainloop()
    
    def on_submit(self, game_type):
        # Trim leading/trailing whitespace
        self.steam_id = self.steam_id_entry.get().strip()
        self.api_key = self.api_key_entry.get().strip()
        
        # Validate the Steam ID and API key
        if not self.validate_steam_id(self.steam_id):
            tk.messagebox.showerror("Error", "Invalid Steam ID. Please enter a valid Steam ID.")
            return
        if not self.validate_api_key(self.api_key):
            tk.messagebox.showerror("Error", "Invalid API Key. Please enter a valid API Key.")
            return
        
        # Display a loading message while fetching the game list
        loading_message = tk.Label(self.window, text="Fetching game list...")
        loading_message.pack()
        
        # Run the game fetching process in a separate thread to prevent freezing the GUI
        threading.Thread(target=self.fetch_games, args=(game_type,)).start()
        
    def fetch_games(self, game_type):
        # Get a list of games based on the selected game type, key, and steam_id
        if game_type == 'all':
            games = self.get_all_games()
        else:
            games = self.get_unplayed_games()
        
        while True:
            try:
                # Suggest a random game from the list of games
                game = self.suggest_game(games)
                
                # Display a message box with the name of the suggested game
                messagebox.showinfo("Game Suggestion:", f"Try playing: {game['name']}")
                
                # Ask the user if they want to launch the suggested game
                launch = messagebox.askyesno("Launch Game", f"Would you like to launch {game['name']}?")
                
                if launch:
                    game_url = f"steam://run/{game['appid']}"
                    webbrowser.open(game_url)
                    break
                else:
                    # Ask the user if they want another random game suggestion
                    another_game = messagebox.askyesno("Another Game", "Would you like to suggest another game?")
                    
                    if not another_game:
                        break
            except Exception as e:
                messagebox.showerror("Error", "An unexpected error occurred. Please try again.")
                break

# Create an instance of the GamePickerApp class and start the GUI
app = GamePickerApp() 
app.create_gui()
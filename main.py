import sqlite3
import hashlib
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.button import Button


# Database setup: create users table if it doesn't exist
def create_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

class ParkingSpot(Button):
    is_occupied = BooleanProperty(False)  # True if a spot is occupied

    def update_spot(self):
        if self.is_occupied:
            self.background_color = (1, 0, 0, 1)  # Red color for occupied
        else:
            self.background_color = (0, 1, 0, 1)  # Green color for available

class MainPage(Screen):
    pass
class Profile(Screen):
    pass
class InfoPage(Screen):
    pass
class RegistrationPage(Screen):
    def register_user(self, email, password):
        if not email or not password:
            popup = Popup(title="Input Error", content=Label(text="Email and Password cannot be empty."), size_hint=(0.8, 0.4))
            popup.open()
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
            conn.commit()
            conn.close()
            popup = Popup(title="Registration Success", content=Label(text="Registration successful!"), size_hint=(0.8, 0.4))
            popup.open()
        except sqlite3.IntegrityError:
            popup = Popup(title="Registration Failed", content=Label(text="Email already registered."), size_hint=(0.8, 0.4))
            popup.open()

class LoginPage(Screen):
    def login_user(self, email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, hashed_password))
        user = cursor.fetchone()
        conn.close()

        if user:
            app = App.get_running_app()
            popup = Popup(title="Login Success", content=Label(text="Login successful!"), size_hint=(0.8, 0.4))
            popup.open()
            app.is_logged_in = True
            app.root.current = "main_page"
        else:
            popup = Popup(title="Login Failed", content=Label(text="Incorrect email or password."), size_hint=(0.8, 0.4))
            popup.open()

class ParkingOptionsPage(Screen):
    pass

class ParkingDetailPage1(Screen):
    pass

class ParkingDetailPage2(Screen):
    pass

class ParkingDetailPage3(Screen):
    pass
class ParkingApp(App):
    is_logged_in = BooleanProperty(False)
    def build(self):
        create_database()
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainPage(name="main_page"))
        sm.add_widget(InfoPage(name="info_page"))
        sm.add_widget(RegistrationPage(name="registration_page"))
        sm.add_widget(LoginPage(name="login_page"))
        sm.add_widget(Profile(name="profile"))
        sm.add_widget(ParkingOptionsPage(name="parking_options_page"))
        sm.add_widget(ParkingDetailPage1(name="parking_detail_page1"))
        sm.add_widget(ParkingDetailPage2(name="parking_detail_page2"))
        sm.add_widget(ParkingDetailPage3(name="parking_detail_page3"))
        return sm
    
    def show_login_notification(self):
        # Popup to notify the user to log in
        popup = Popup(
            title="Login Required",
            content=Label(text="Please log in to access parking options."),
            size_hint=(0.8, 0.4),
            auto_dismiss=True
        )
        popup.open()
    
    def account_login(self):
        self.root.current = "login_page"
    
    def show_info(self):
        self.root.current = "info_page"

    def go_back(self):
        self.root.current = "main_page"

    def account_login(self):
        self.root.current = "login_page"
        
    def profile(self):
        self.root.current = "profile"

    def register_redirect(self):
        self.root.current = "registration_page"

    def find_parking(self):
        if not self.is_logged_in:
            self.show_login_notification()
        else:
            self.root.current = "parking_options_page"  # Navigate to Find Parking

    def show_parking_detail1(self):
        self.root.current = "parking_detail_page1"  # Navigate to the Parking Detail Page for "Parcare 1"
    
    def show_parking_detail2(self):
        
        self.root.current = "parking_detail_page2"
    
    def show_parking_detail3(self):
        
        self.root.current = "parking_detail_page3"

if __name__ == "__main__":
    ParkingApp().run()
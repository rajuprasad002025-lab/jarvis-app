from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.label = Label(text="JARVIS AI Ready\nSir, main aapki kya madad karoon?", font_size=20, halign='center')
        layout.add_widget(self.label)
        
        btn_google = Button(text="Open Google", size_hint=(1, 0.2))
        btn_google.bind(on_press=self.open_google)
        layout.add_widget(btn_google)
        
        btn_alarm = Button(text="Set Alarm (06:30)", size_hint=(1, 0.2))
        btn_alarm.bind(on_press=self.set_alarm)
        layout.add_widget(btn_alarm)
        
        return layout

    def open_google(self, instance):
        self.label.text = "Opening Google..."
        os.system("am start -a android.intent.action.VIEW -d https://www.google.com")

    def set_alarm(self, instance):
        self.label.text = "Setting Alarm..."
        os.system("am start -a android.intent.action.SET_ALARM --ei android.intent.action.EXTRA_HOUR 6 --ei android.intent.action.EXTRA_MINUTES 30 --ez android.intent.action.EXTRA_SKIP_UI true")

if __name__ == '__main__':
    JarvisApp().run()
   

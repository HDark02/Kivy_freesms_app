from kivymd.uix.banner.banner import MDFlatButton
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast.kivytoast.kivytoast import toast
from plyer import filechooser
import os, io, re
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
import webbrowser

Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
login="""
MDScreen:
	name: "login_screen"
	account_sid:account_sid
	auth_token:auth_token
	twilio_number:twilio_number
	MDFloatLayout:
		md_bg_color: "white"
		MDLabel:
			text:"Message gratuit avec Twilio"
			halign: "center"
			size_hint: .9, .2
			pos_hint: {"center_x": .5, "center_y": .9}
			theme_text_color: "Custom"
			font_size: "25sp"
			font_name: "MontserratSubrayada-Regular.ttf"
			text_color: "black"
		MDLabel:
			text:"Informations"
			halign: "center"
			size_hint: .8, .2
			pos_hint: {"center_x": .5, "top": .9}
			theme_text_color: "Custom"
			font_size:"25sp"
			text_color: "black"
		MDTextField:
			id: twilio_number
			hint_text: "Votre Numero Twilio"
			width: 300
			md_bg_color: "blue"
			mode: "rectangle"
			size_hint: .8, .08
			font_size: "25sp"
			height: self.minimum_height
			pos_hint: {"center_x": .5, "center_y": .68}
			icon_left: "phone"
		MDTextField:
			id: account_sid
			hint_text: "'account sid' de votre compte Twilio"
			width: 300
			md_bg_color: "yellow"
			mode: "rectangle"
			size_hint: .8, .08
			font_size: "25sp"
			height: self.minimum_height
			pos_hint: {"center_x": .5,  "center_y": .58}
			icon_left: "account"
			
		MDTextField:
			id: auth_token
			hint_text: "'auth token' reçu sur Twilio"
			width: 300
			md_bg_color: "green"
			mode: "rectangle"
			size_hint: .8, .08
			font_size: "25sp"
			height: self.minimum_height
			pos_hint: {"center_x": .5, "center_y": .48}
			icon_left: "key"
		MDFlatButton:
			text: "Continuer"
			theme_text_color: "Custom"
			md_bg_color: "blue"
			text_color: "white"
			font_size: "25sp"
			halign: "center"
			pos_hint: {"center_x": .5,"center_y": .25}
			size_hint: .5, .08
			on_release:
				app.save()
		# MDFloatingActionButton:
		# 	id: save_login
		# 	icon: "arrow-right-circle"
		# 	theme_text_color: "Custom"
		# 	md_bg_color: "blue"
		# 	halign: "center"
		# 	pos_hint: {"right": .95,"center_y": .25}
		# 	on_release:
		# 		app.save()
		MDFloatingActionButton:
			icon: "help-circle"
			# md_bg_color: "black"
			theme_text_color: "Custom"
			text_color: "black"
			font_size: "25sp"
			pos_hint: {"center_x": dp(.08), "center_y": dp(.08)}
			on_release:
				app.info()
		MDTextButton:
			id: about_us
			text: "A propos"
			theme_text_color: "Custom"
			text_color: "black"
			size_hint: .4, .1
			font_size: "25sp"
			font_name: "BungeeInline-Regular.ttf"
			pos_hint: {"center_x": .9, "center_y": dp(.08)}
			on_release:
				root.manager.transition.direction = "left"
				root.manager.current = "about_us"
"""
screen_sms="""
MDScreen:
	name: "sms_screen"
	nbr_env:nbr_env
	br_call:br_call
	MDFloatLayout:
		md_bg_color: "#4398c7c0"
		MDTopAppBar:
			id: br_call
			title: "Nombre de contact"
			padding: 5
			pos_hint: {"center_x": .5,"top": 1}
			left_action_items: [["arrow-left-bold-outline", lambda x: app.to_login_screen()]]
			right_action_items: [["contacts", lambda x: app.open_filemanager()]]
		MDLabel:
			text:"Message"
			halign: "center"
			size_hint: .8, .2
			pos_hint: {"center_x": .5, "top": .98}
			theme_text_color: "Custom"
			font_size:"30sp"
			opacity: 5
			text_color: "white"
		TextInput:
			id: message_1
			mode: "rectangle"
			hint_text: "Entre votre message ici"
			text_theme_color: "Custom"
			text_color: "black"
			hint_text_color: "white"
			opacity: 0.7
			size_hint: .8, .1
			background_normal: ''
			background_active: ''
			background_color: "#4398c7c0" #bg_color
			foreground_color: "black"  # black pour le texte
			multiline: True
			cusor_size: "25sp"
			font_size: "25sp"
			md_bg_color: "gray"
			pos_hint: {"center_x": .5, "top": .8}
		MDTextField:
			id: lien_t
			hint_text: "Entrer votre lien à partager ici"
			theme_hint_text_color: "blue"
			text_theme_color: "Custom"
			text_color: "black"
			font_size: "20sp"
			# line_color_normal: 0, 0, 1, 1  # Blue line color when not focused
			line_color_focus: "blue"  #blue line color when focused
			mode: "round"
			size_hint_x: .8
			pos_hint: {"center_x": .5, "center_y": .65}
		
		
		MDGridLayout:
			size_hint: 1, .1
			pos_hint: {"center_x": .5, "center_y": .5}
			padding: 10
			cols: 2
			rows: 1
			spacing: 10
			Card_button:
				text_name : "Message sms"
				icon_name : "message"
				text_color: "black"
				icon_color: "black"
				on_release: app.send_message()
			Card_button:
				text_name : "Whatsapp"
				icon_name: "whatsapp"
				text_color: "green"
				icon_color: "green"
				on_release: app.send_whatsap()
			
		MDLabel:
			id: nbr_env
			text:""
			halign: "center"
			size_hint: .8, .5
			pos_hint: {"center_x": .30, "center_y": .4}
			theme_text_color: "Custom"
			halign: "center"
			font_size:"30sp"
			opacity: 5
			text_color: "white"
				
		MDFloatingActionButton:
			icon: "help-circle"
			# md_bg_color: "black"
			theme_text_color: "Custom"
			text_color: "black"
			font_size: "25sp"
			pos_hint: {"center_x": dp(.08), "center_y": dp(.08)}
			on_release:
				app.info()
		MDTextButton:
			id: about_us
			text: "A propos"
			theme_text_color: "Custom"
			text_color: "black"
			size_hint: .4, .1
			font_size: "25sp"
			font_name: "BungeeInline-Regular.ttf"
			pos_hint: {"center_x": .9, "center_y": dp(.08)}
			on_release:
				root.manager.transition.direction = "left"
				root.manager.current = "about_us"

<Card_button@MDCard>:
	size_hint: .5, .08
	pos_hint: {"center_x": .5, "center_y": .5}
	orientation: "horizontal"
	md_bg_color: "white"
	text_name: ""
	icon_name:  ""
	on_release:  ""
	text_color: "black"
	icon_color: "black"
	MDIconButton:
		icon: root.icon_name
		pos_hint: {"center_x": .5, "center_y": .5}
		on_release: on_release
		theme_text_color: "Custom"
		text_color: root.icon_color
	MDTextButton:
		text: root.text_name
		on_release: on_release
		theme_text_color: "Custom"
		font_size: "25sp"
		font_name: "GaMaamli-Regular.ttf"
		text_color: root.text_color
		size_hint_x :.8
		pos_hint: {"center_x": .5, "center_y": .5}
	
  
	


"""
from twilio.rest import Client

class Sms_app(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	def info(self):
		global dialog
		dialog = None
		with io.open("info.txt", "r", encoding="UTF-8") as file:
			info_utilisation = file.read()
			close_bt=MDRaisedButton(text="fermé", on_release=self.close_box)
			if not dialog:
				dialog=MDDialog(title= "Info",
									buttons=[close_bt],
									text=info_utilisation,
									pos_hint={"center_x": .5, "center_y": .5},
									size_hint= (.85, .7),
									padding=10
									)
			dialog.open()
	def close_box(self, obj):
		dialog.dismiss()
		pass
	
	def selected(self, selection):
		if selection:
			vcf = selection[0]
			self.load_vcf_file(vcf)
			
	def load_vcf_file(self, file_name):
		def continu(numero):
			list_contacts=[]
			numero1=(numero)
			for numero in numero1:
				list_contacts.append(numero.replace(" ",""))
			screen_manager.get_screen("sms_screen").br_call.title = "Nombre de contact: " + str(len(list_contacts))
			self.list_contacts=list_contacts
			
		with open(file_name, "r") as file:
			texte = file.read()
			toast(f"{file_name} load succesfully ...")
			num = "TEL;CELL:([0-9+*#]{8,})"; name = "N:;([ a-zA-Z]+);;;"
			numero = re.findall(num, texte)
			nom= re.findall(name, texte)
			if len(numero) !=0:
				continu(numero)
				
			else:
				pass
# self.close_filemanager()
	def open_filemanager(self):
		filechooser.open_file(on_selection= self.selected)
	def go_back(self):
		screen_manager.transition.direction = "up"
		screen_manager.current = "sms_screen"
	def to_login_screen(self):
		screen_manager.transition.direction = "right"
		screen_manager.current = "login_screen"
	def send_message(self):
		list_contacts= self.list_contacts
		with io.open("info_user.txt", "r") as file:
			info =file.read()
			account_sid,auth_token,twilio_number =info.split(",")
		try:
			if len(list_contacts) != 0:
				
				send_n=0
				contacts=list_contacts #all contact to add_to that list

				for number in contacts:
					client_phone_number = number  #client number
					client = Client(account_sid, auth_token)
					message = client.message.create(
						body = f"{screen_manager.get_screen('sms_screen').message_1.text}\n{screen_manager.get_screen('sms_screen').lien_t.text}",
						from_ = twilio_number,
						to = client_phone_number
					)
					env = screen_manager.get_screen('sms_screen').send_n.text
					send_n = +1
					screen_manager.get_screen('sms_screen').nbr_env.text = send_n
					env = f"envoyé à {client_phone_number} avec success"
					screen_manager.get_screen('sms_screen').nbr_env.text = f"Envoyé: {send_n}"
					toast(f"msg {env}")
		except:
			print("error")
	def send_whatsap(self):
		list_contacts= self.list_contacts
		with io.open("info_user.txt", "r") as file:
			info =file.read()
			account_sid,auth_token,twilio_number =info.split(",")
		if len(list_contacts) != 0:
			send_n=0
			contacts=list_contacts #all contact to add_to that list

			for number in contacts:
				client_phone_number = number  #client number
				client = Client(account_sid, auth_token)
				message = client.message.create(
					body = f"{screen_manager.get_screen('sms_screen').message_1.text}\n{screen_manager.get_screen('sms_screen').lien_t.text}",
					from_ = f"whatsapp:{twilio_number}",
					to = f"whatsapp:{client_phone_number}"
				)

				send_n = +1
				screen_manager.get_screen('sms_screen').nbr_env.text = send_n

				env = f"envoyé à {client_phone_number} avec success"
				screen_manager.get_screen('sms_screen').nbr_env.text = f"Envoyé: {send_n}"	
				toast(f"msg {env}")

		# def verif_msg(self):
	def save(self):
		account_sid = screen_manager.get_screen("login_screen").account_sid.text
		auth_token = screen_manager.get_screen("login_screen").auth_token.text
		twilio_number = screen_manager.get_screen("login_screen").twilio_number.text  # your number which is giving by twilio
		if account_sid!= "" or auth_token!="" or twilio_number =="":
			with io.open("info_user.txt", "w") as file:
				file.write(f"{account_sid}, {auth_token}, {twilio_number}")
			screen_manager.transition.direction = "left"
			screen_manager.current = "sms_screen"
		else:
			toast("Imformation non valide!")
	def go_back(self):
		screen_manager.transition.direction = "up"
		screen_manager.current = "sms_screen"
	def on_start(self):
		try:
			with io.open("info_user.txt", "r") as file:
				info =file.read()
				account_sid,auth_token,twilio_number =info.split(",")
			if (account_sid=="") or (auth_token=="") or (twilio_number== ""):
				screen_manager.transition.direction = "up"
				screen_manager.current = "login_screen"
		except:
			screen_manager.current = "sms_screen"
	def build(self):
		list_contacts=[]
		global screen_manager
		screen_manager = ScreenManager()
		screen_manager.add_widget(Builder.load_string(login))
		screen_manager.add_widget(Builder.load_string(screen_sms))
		screen_manager.add_widget(Builder.load_file("about_us.kv"))
		
		return screen_manager
	def info_all_notification(self, index):
		if (index== 1) or (index == 2):
			toast("Contacte en cour ....")
			webbrowser.open("https://t.me/Thekingdynamo")
Sms_app().run()









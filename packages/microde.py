from xmpd import run
import os
apps = ["Calculator", "System Info", "Install new Apps", "Network Manager", "More..."]
while True:
	for app in apps:
		print(app)
		chosen = input("Leave blank to skip, type 'e' to execute >> ")
		if chosen == "e":
			chosen_app = app
			for _ in range(50): print("\n")
		else:
			continue
		if chosen_app == "Calculator":
			run("run microlator.py")
		elif chosen_app == "System Info":
			run("aboutsys")
		elif chosen_app == "Install new Apps":
			_ = input("App name: ")
			run(f"pkginstall {_}")
		elif chosen_app == "Network Manager":
			_1 = input("Turn WiFi on/off? ")
			_2 = input("Enter SSID: ")
			_3 = input("Type in password: ")
			run(f"netman {_1} {_2} {_3}")
		elif chosen_app == "More...":
			for app in os.listdir():
				if app.endswith(".py"):
					print("Detected", app, "on computer.")
					_ = input("Execute? y/n > ")
					if _ == "y":
						run(f"run {app}")
						continue
					elif _ == "n":
						continue
				
	

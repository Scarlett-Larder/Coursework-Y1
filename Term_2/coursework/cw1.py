from tkinter import Tk, Frame, Button, Label, simpledialog
import csv

#Task 1: 6-58, Task 2: 63-135, Task 3: 139-268

#Task 1
class SmartPlug:

    def __init__(self, consumption_rate):
        while consumption_rate > 150 or consumption_rate < 0:
            raise ValueError("Consumption rate must be between 0 and 150")
        self._consumption_rate = consumption_rate
        self.switched_on = False

    def toggle_switch(self):
         self.switched_on = not self.switched_on

    @property
    def consumption_rate(self):
        return self._consumption_rate

    @consumption_rate.setter
    def consumption_rate(self, value):
        if value > 150 or value < 0:
            print("ERROR: Invalid consumption rate. No changes where made. \n")
        else: 
            self._consumption_rate = value
            
    
    def __str__(self):
        if self.switched_on:
            return f"SmartPlug is on with a consumption rate of {self.consumption_rate}"
        else:
            return f"SmartPlug is off with a consumption rate of {self.consumption_rate}"


def test_smart_plug():
    plug1 = SmartPlug(45)
    print(plug1)
    plug1.toggle_switch()
    print(plug1)
    plug1.consumption_rate = 75
    print(plug1)
    plug1.toggle_switch()
    print(plug1)

    plug1.consumption_rate = -10
    print(plug1)

    try:
        plug2 = SmartPlug(-5)
    except ValueError:
        print("Invalid initalisation was blocked \n")
    
    try:
        plug3 = SmartPlug(200)
    except ValueError:
        print("Invalid initalisation was blocked \n")



#Task 2 - ID = 2276970
class SmartDevice:

    def __init__(self):
        self.switched_on = False

    def toggle_switch(self):
         self.switched_on = not self.switched_on


class SmartLight(SmartDevice):

    def __init__(self):
        super().__init__()
        self._brightness = 50
    
    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if value > 100 or value < 0:
            print("ERROR: Invalid brightness. No changes where made. \n")
        else: 
            self._brightness = value
    
    def __str__(self):
        status = "on" if self.switched_on else "off"
        return f"SmartLight is {status} with a brightness of {self.brightness}"


class SmartWashingMachine(SmartDevice):

    valid_wash_mode = {"Daily wash", "Quick wash", "Eco"}

    def __init__(self):
        super().__init__()
        self.wash_mode = "Daily wash"
    
    @property
    def wash_mode(self):
        return self._wash_mode

    @wash_mode.setter
    def wash_mode(self, value):
        if value not in self.valid_wash_mode:
            print("ERROR: Invalid consumption rate. No changes where made. \n")
        else: 
            self._wash_mode = value
    
    def __str__(self):
        status = "on" if self.switched_on else "off"
        return f"SmartWashingMachine is {status} with a wash mode of {self.wash_mode}"


def test_custom_device():
    #Test initalisation and default valuess
    light1 = SmartLight()
    wash1 = SmartWashingMachine()
    print(light1)
    print(wash1)

    #Test ON/OFF
    light1.toggle_switch()
    wash1.toggle_switch()
    print(light1)
    print(wash1)

    #Hard: Invalid constraints
    light1.brightness = 500
    wash1.wash_mode = "Umm idk"
    print(light1)
    print(wash1)



#Task 3
class SmartHome():

    max_items = 5

    def __init__(self):
        self.devices = []

    def add_device(self, device):
        if len(self.devices) < self.max_items:
            self.devices.append(device)
        else:
            print(f"No more devices can added (max {self.max_items})\n")

    def get_device(self, index):
        if 0 <= index < len(self.devices):
            print(self.devices[index])
            return self.devices[index]
        else:
            raise IndexError("Invalid device index \n")

    def toggle_device(self, index):
        if 0 <= index < len(self.devices):
            self.devices[index].toggle_switch()
        else:
            raise IndexError("Invalid device index \n")

    def switch_all_on(self):
        for device in self.devices:
            device.switched_on = True

    def switch_all_off(self):
        for device in self.devices:
            device.switched_on = False

    def remove_device(self, index):
        if 0 <= index < len(self.devices):
            self.devices.pop(index)
        else:
            raise IndexError("Invalid device index \n")
    
    def update_option(self, index, value):
        device = self.devices[index]
        if 0 <= index < len(self.devices):
            if isinstance(device, SmartPlug):
                if value > 150 or value < 0:
                    print("ERROR: Invalid consumption rate. No changes where made. \n")
                else: 
                    self.devices[index].consumption_rate = value
            if isinstance(device, SmartWashingMachine):
                if value not in self.devices[index].valid_wash_mode:
                    print("ERROR: Invalid Wash mode. No changes where made. \n")
                else: 
                    self.devices[index].wash_mode = value
            if isinstance(device, SmartLight):
                if value > 100 or value < 0:
                    print("ERROR: Invalid brightness. No changes where made. \n")
                else: 
                    self.devices[index].brightness = value
        else:
            raise IndexError("Invalid device index \n")

    def __str__(self):
        para = f"Smart Home with {len(self.devices)} device(s):"
        for index, device in enumerate(self.devices, start=1):
            para += f"\n {index}. {device}"
        para += "\n"
        return para



def test_smart_home():
    # Initalisation
    item1 = SmartPlug(100)
    item2 = SmartLight()
    item3 = SmartWashingMachine()
    home1 = SmartHome()

    # Adding devices
    home1.add_device(item1)
    home1.add_device(item2)
    home1.add_device(item3)
    print(home1)

    # Getting each device
    home1.get_device(0)
    home1.get_device(1)
    home1.get_device(2)

    # Toggling each devices on
    home1.toggle_device(0)
    home1.toggle_device(1)
    home1.toggle_device(2)
    print(home1)

    # Toggle all devices on and off
    home1.switch_all_on()
    home1.switch_all_off()
    print(home1)

    print("Now testing harder requirements... \n")
    
    # max_items test
    item4 = SmartLight()
    item5 = SmartLight()
    item6 = SmartLight()
    home1.add_device(item4)
    home1.add_device(item5)
    home1.add_device(item6)

    # Modify devices
    home1.update_option(0, 70)
    print(home1)
    home1.update_option(0, 5000)
    print(home1)

    # Remove test
    home1.remove_device(3)
    print(home1)
    try:
        home1.remove_device(100000000)
    except IndexError:
        print("Invalid device index  \n")

    # update devices
    home1.update_option(0, 5000)
    home1.update_option(1, 110)
    home1.update_option(2, "IDK lol")

    print(home1)



#  - 5
class SmartHomeApp():
    def __init__(self, home=None):
        self.home = home if home else SmartHome()
        item1 = SmartPlug(45)
        item2 = SmartLight()
        item3 = SmartWashingMachine()

        self.home.add_device(item1)
        self.home.add_device(item2)
        self.home.add_device(item3)

        self.win = Tk()
        self.win.title("Smart Home App")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )
    
    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):

        # Turn on/off buttons
        turn_on_button = Button(
            self.main_frame,
            text="Turn on all",
            command=self.turn_on_all,
            padx=30
        )
        turn_on_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        turn_off_button = Button(
            self.main_frame,
            text="Turn off all",
            command=self.turn_off_all,
            padx=30
        )
        turn_off_button.grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
            sticky="w"
        )

        # Device
        i = 0
        for i, device in enumerate(self.home.devices):
            
            device = self.home.devices[i]

            if isinstance(device, SmartPlug):
                device_name = "Plug"
                device_variable = "Consumption"
                device_value = device.consumption_rate
            elif isinstance(device, SmartWashingMachine):
                device_name = "Wash Machine"
                device_variable = "Temperature"
                device_value = device.wash_mode
            elif isinstance(device, SmartLight):
                device_name = "Light"
                device_variable = "Mode"
                device_value = device.brightness
            else:
                device_name = ""
                device_variable = ""
                device_value = ""
                print("ERROR: Invalid object. \n")

            status = "on" if device.switched_on else "off"
            device_label = Label(
                self.main_frame,
                text = f"{device_name}: {status}, {device_variable}: {device_value}"
            )
            device_label.grid(row=i+1, column=1, padx=5, pady=5, sticky="w")

            #buttons
            toggle_button = Button(
                self.main_frame,
                text="Toggle",
                command=lambda index=i: self.toggle_device(index),
                padx= 40
            )
            toggle_button.grid(
                row=i+1,
                column=2,
                padx=0,
                pady=0,
                sticky="w"
            )

            edit_button = Button(
                self.main_frame,
                text="Edit",
                command=lambda index=i: self.edit_device(index),
                padx=20
            )
            edit_button.grid(
                row=i+1,
                column=3,
                padx=0,
                pady=0,
                sticky="w"
            )

            delete_button = Button(
                self.main_frame,
                text="Delete",
                command=lambda index=i: self.delete_device(index),
                padx=10
            )
            delete_button.grid(
                row=i+1,
                column=4,
                padx=10,
                pady=0,
                sticky="w"
            )

        add_button = Button(
            self.main_frame,
            text="Add",
            command=self.add_device,
            padx=25
        )
        add_button.grid(
            row=i+2,
            column=1,
            padx=0,
            pady=10,
            sticky="w"
        )


    def turn_on_all(self):
        self.home.switch_all_on()
        self.create_widgets()
    
    def turn_off_all(self):
        self.home.switch_all_off()
        self.create_widgets()
    
    def toggle_device(self, index):
        self.home.toggle_device(index)
        self.create_widgets()
    
    def delete_device(self, index):
        self.home.remove_device(index)
        self.refresh()

    def edit_device(self, index):
        device = self.home.devices[index]
        if isinstance(device, SmartPlug):
            value = simpledialog.askinteger("-", "Consumption (0-150)")
            self.home.update_option(index, value)
            self.refresh()
        elif isinstance(device, SmartWashingMachine):
            value = simpledialog.askstring("-", "Mode (Daily, Quick, Eco)")
            self.home.update_option(index, value)
            self.refresh()
        elif isinstance(device, SmartLight):
            value = simpledialog.askinteger("", "Brightness (0-100)")
            self.home.update_option(index, value)
            self.refresh()
        else:
            print("ERROR: Invalid object \n")
    
    def add_device(self):
        device_choice = simpledialog.askstring("-", "What device? (Plug, Washing Machine, Light)")
        if device_choice == "Plug":
            value = simpledialog.askinteger("-", "Consumption (0-150)")
            self.home.add_device(SmartPlug(value))
            self.refresh()
        elif device_choice == "Washing Machine":
            self.home.add_device(SmartWashingMachine())
            self.refresh()
        elif device_choice == "Light":
            self.home.add_device(SmartLight())
            self.refresh()
        else:
            print("ERROR: Invalid selection. No changes where made.")

    def refresh(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.create_widgets()



def test_start_home_system():
    smart = SmartHomeApp()
    smart.run()



#Challenge Task
class SmartHomesApp():

    homes = []

    def __init__(self):
        self.win = Tk()
        self.win.title("Smart Homes App")

        self.win.protocol("WM_DELETE_WINDOW", self.before_close)

        #open file
        try:
            with open("smart_homes_save.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    home = SmartHome()
                    for col in row:
                        parts = col.split(",")
                        device_type = int(parts[0])
                        variable = parts[1]
                        state = parts[2].strip().lower() == "true"

                        if device_type == 0:
                            plug = SmartPlug(int(variable))
                            plug.switched_on = state
                            home.add_device(plug)

                        if device_type == 1:
                            light = SmartLight()
                            light.brightness = int(variable)
                            light.switched_on = state
                            home.add_device(light)
                        
                        if device_type == 2:
                            wash = SmartWashingMachine()
                            wash.brightness = variable
                            wash.switched_on = state
                            home.add_device(wash)


                    self.homes.append(home)
        except FileNotFoundError:
            print("No file found. Cool!")

        self.main_frame = Frame(self.win)v
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

    def run(self):
        self.create_widgets()
        self.win.mainloop()
        
    def create_widgets(self):
            
        #Add smart home
        turn_on_button = Button(
            self.main_frame,
            text="Add a new Home",
            command=self.add_home,
            padx=75
        )
        turn_on_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        refresh_button = Button(
            self.main_frame,
            text="Refresh",
            command=self.refresh,
            padx=20
        )
        refresh_button.grid(
            row=0,
            column=2,
            padx=0,
            pady=0,
            sticky="w"
        )

        for i, home in enumerate(self.homes):
            home = self.homes[i]
            home_devices = len(home.devices)
            home_devices_on = 0
            for device in home.devices:
                if device.switched_on:
                     home_devices_on += 1
            device_label = Label(
                self.main_frame,
                text = f"{i+1}. Smart Home, Devices: {home_devices}, Currently On: {home_devices_on}"
            )
            device_label.grid(row=i+1, column=1, padx=5, pady=5, sticky="w")
        
            edit_button = Button(
                self.main_frame,
                text="Edit",
                command=lambda index=i: self.edit_home(index),
                padx=30
            )
            edit_button.grid(
                row=i+1,
                column=2,
                padx=0,
                pady=0,
                sticky="w"
            )
            remove_button = Button(
                self.main_frame,
                text="Remove",
                command=lambda index=i: self.remove_home(index),
                padx=10
            )
            remove_button.grid(
                row=i+1,
                column=3,
                padx=0,
                pady=0,
                sticky="w"
            )

    def add_home(self):
        new_home = SmartHome()
        self.homes.append(new_home)
        self.refresh()

    def edit_home(self, index):
        selected_home = self.homes[index]
        smart_home_app = SmartHomeApp(selected_home)
        smart_home_app.run()
        self.refresh()
    
    def remove_home(self, index):
        self.homes.pop(index)
        self.refresh()

    def refresh(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.create_widgets()

    def before_close(self):
        print("Saving changes...")
        file_name = "smart_homes_save.csv"
        with open(file_name, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            for home in self.homes:
                home_data = []
                for device in home.devices:
                    if isinstance(device, SmartPlug):
                        home_data.append(f"{0},{device.consumption_rate},{device.switched_on}")
                    elif isinstance(device, SmartWashingMachine):
                        home_data.append(f"{2},{device.wash_mode},{device.switched_on}")
                    elif isinstance(device, SmartLight):
                        home_data.append(f"{1},{device.brightness},{device.switched_on}")
                csvwriter.writerow(home_data)

        self.win.destroy()

def test_smart_homes_app():
    start = SmartHomesApp()
    start.run()

test_smart_homes_app()
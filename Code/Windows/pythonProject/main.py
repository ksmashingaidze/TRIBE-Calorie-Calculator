import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp

# Define key variables used in the Mifflin St. Jeor calculation
result = ""            # Initialize a variable that will be used to store the output of the Mifflin St. Jeor calculation
ac_lvl = float(0)      # Initialize a variable that will be used to store the selected activity level
weight_goal = ""       # Initialize a variable that will be used to store the selected weight goal
sex = ""               # Initialize a variable that will be used to store the sex of the user
age_yrs = float(0)     # Initialize a variable that will be used to store the age of the user
height_ft = float(0)   # Initialize a variable that will be used to store the "ft" component of the height of the user
height_in = float(0)   # Initialize a variable that will be used to store the "in" component of the height of the user
weight_lbs = float(0)  # Initialize a variable that will be used to store the weight of the user
bmr = float(0)         # Initialize a variable to store the basal metabolic rate
calories = float(0)    # Initialize a variable to store the product of the BMR and the activity level in kcal/day

class CalculatorInterface(GridLayout):
    def __init__(self, **kwargs):
        super(CalculatorInterface, self).__init__(**kwargs)
        self.cols = 5

        # Row 1
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 2
        # Logo
        for i in range(0, 2):
            self.add_widget(Label(text=" "))
        self.add_widget(Label(text="[b][u]TRIBE Calorie Calculator[/u][/b]", markup=True))
        for i in range(0, 2):
            self.add_widget(Label(text=" "))

        # Row 3
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 4
        # Sex labels "M" and "F" above radio buttons
        self.add_widget(Label(text=" "))
        self.add_widget(Label(text="M"))
        self.add_widget(Label(text="F"))
        for i in range(0, 2):
            self.add_widget(Label(text=" "))

        # Row 5
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 6
        # Radio-box for Sex
        self.add_widget(Label(text="Sex: "))
        male_check = CheckBox(group="Sex", allow_no_selection=False)
        female_check = CheckBox(group="Sex", allow_no_selection=False)
        self.add_widget(male_check)
        self.add_widget(female_check)
        for i in range(0, 2):
            self.add_widget(Label(text=" "))

        # Row 7
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 8
        # Age
        self.add_widget(Label(text="Age: "))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)
        self.add_widget(Label(text="Yrs."))
        for i in range(0, 2):
            self.add_widget(Label(text=" "))

        # Row 9
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 10
        # Height
        self.add_widget(Label(text="Height: "))
        self.feet = TextInput(multiline=False)
        self.add_widget(self.feet)
        self.add_widget(Label(text="Ft."))
        self.inches = TextInput(multiline=False)
        self.add_widget(self.inches)
        self.add_widget(Label(text="In."))

        # Row 11
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 12
        # Current Weight
        self.add_widget(Label(text="Current Weight: "))
        self.curr_weight = TextInput(multiline=False)
        self.add_widget(self.curr_weight)
        self.add_widget(Label(text="Lbs."))
        for i in range(0, 2):
            self.add_widget(Label(text=" "))

        # Row 13
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 14
        # Drop-down list for Activity Level
        self.add_widget(Label(text="Activity Level: "))
        ac_lvl_dropdown = DropDown()
        # Create the entries/options of the dropdown list, which have the properties of a button
        ac_lvl_0 = Button(text="Sedentary", size_hint_y=None, width=200, height=44)
        ac_lvl_1 = Button(text="Lightly Active", size_hint_y=None, width=200, height=44)
        ac_lvl_2 = Button(text="Moderately Active", size_hint_y=None, width=200, height=44)
        ac_lvl_3 = Button(text="Very Active", size_hint_y=None, width=200, height=44)
        ac_lvl_4 = Button(text="Extra Active", size_hint_y=None, width=200, height=44)
        # Pass the text of the selected entry/option of the dropdown list to the dropdown list itself
        ac_lvl_0.bind(on_release=lambda btn: ac_lvl_dropdown.select(ac_lvl_0.text))
        ac_lvl_1.bind(on_release=lambda btn: ac_lvl_dropdown.select(ac_lvl_1.text))
        ac_lvl_2.bind(on_release=lambda btn: ac_lvl_dropdown.select(ac_lvl_2.text))
        ac_lvl_3.bind(on_release=lambda btn: ac_lvl_dropdown.select(ac_lvl_3.text))
        ac_lvl_4.bind(on_release=lambda btn: ac_lvl_dropdown.select(ac_lvl_4.text))
        # Manifest the entries/options of the dropdown list as widgets on the dropdown list itself
        ac_lvl_dropdown.add_widget(ac_lvl_0)
        ac_lvl_dropdown.add_widget(ac_lvl_1)
        ac_lvl_dropdown.add_widget(ac_lvl_2)
        ac_lvl_dropdown.add_widget(ac_lvl_3)
        ac_lvl_dropdown.add_widget(ac_lvl_4)
        # Create the main button of the dropdown list which is clicked to expand the options
        ac_lvl_main = Button(text="Select Activity Level", size_hint=(None, None), width=200, height=44)
        # Show the dropdown list when the main button is pressed
        ac_lvl_main.bind(on_release=ac_lvl_dropdown.open)
        # Update the dropdown list's main button text to the text of the selected entry/option
        ac_lvl_dropdown.bind(on_select=lambda instance, x: setattr(ac_lvl_main, 'text', x))
        # Manifest the main button of the dropdown list
        self.add_widget(ac_lvl_main)
        # Blank columns
        for i in range(0, 3):
            self.add_widget(Label(text=" "))

        # Row 15
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 16
        # Drop-down list for Weight Goal
        self.add_widget(Label(text="Weight Goal: "))
        weight_goal_dropdown = DropDown()
        # Create the entries/options of the dropdown list, which have the properties of a button
        weight_goal_0 = Button(text="Lose Weight", size_hint_y=None, width=200, height=44)
        weight_goal_1 = Button(text="Maintain Weight", size_hint_y=None, width=200, height=44)
        weight_goal_2 = Button(text="Gain Weight", size_hint_y=None, width=200, height=44)
        # Pass the text of the selected entry/option of the dropdown list to the dropdown list itself
        weight_goal_0.bind(on_release=lambda btn: weight_goal_dropdown.select(weight_goal_0.text))
        weight_goal_1.bind(on_release=lambda btn: weight_goal_dropdown.select(weight_goal_1.text))
        weight_goal_2.bind(on_release=lambda btn: weight_goal_dropdown.select(weight_goal_2.text))
        # Manifest the entries/options of the dropdown list as widgets on the dropdown list itself
        weight_goal_dropdown.add_widget(weight_goal_0)
        weight_goal_dropdown.add_widget(weight_goal_1)
        weight_goal_dropdown.add_widget(weight_goal_2)
        # Create the main button of the dropdown list which is clicked to expand the options
        weight_goal_main = Button(text="Select Goal", size_hint=(None, None), width=200, height=44)
        # Show the dropdown list when the main button is pressed
        weight_goal_main.bind(on_release=weight_goal_dropdown.open)
        # Update the dropdown list's main button text to the text of the selected entry/option
        weight_goal_dropdown.bind(on_select=lambda instance, x: setattr(weight_goal_main, 'text', x))
        # Manifest the main button of the dropdown list
        self.add_widget(weight_goal_main)
        # Blank columns
        for i in range(0, 3):
            self.add_widget(Label(text=" "))

        # Row 17
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 18
        # Calculate button
        for i in range(0, 2):
            self.add_widget(Label(text=" "))
        calc_btn = Button(text="Calculate")

        # Define a function that checks whether the user input fields are valid
        def check_input_fields():
            # Try and convert the user inputs to float format. If successful, return "True"
            try:
                float(self.age.text)
                float(self.feet.text)
                float(self.inches.text)
                float(self.curr_weight.text)
                return True
            # If the conversion to float is unsuccessful, implying the user inputs are invalid, return "False"
            except:
                return False

        # Define "Calculate" button behaviour
        def callback(instance):
            # Update the all variables which will be used in the Mifflin St. Jeor calculation
            if male_check.active is True:
                sex = "Male"
            elif female_check.active is True:
                sex = "Female"
            else:
                sex = ""

            if ac_lvl_main.text == "Sedentary":
                ac_lvl = 1.2
            elif ac_lvl_main.text == "Lightly Active":
                ac_lvl = 1.375
            elif ac_lvl_main.text == "Moderately Active":
                ac_lvl = 1.550
            elif ac_lvl_main.text == "Very Active":
                ac_lvl = 1.725
            elif ac_lvl_main.text == "Extra Active":
                ac_lvl = 1.9
            else:
                ac_lvl = 0
            weight_goal = weight_goal_main.text
            # Implement Mifflin St. Jeor calculation
            if check_input_fields():
                age_yrs = float(self.age.text)
                height_ft = float(self.feet.text)
                height_in = float(self.inches.text)
                weight_lbs = float(self.curr_weight.text)
                if ac_lvl == 1.2 or ac_lvl == 1.375 or ac_lvl == 1.550 or ac_lvl == 1.725 or ac_lvl == 1.9:
                    if sex == "Male":
                        bmr = (10*weight_lbs/2.2)+(6.25*((height_ft*30.48)+(height_in*0.0833*30.48)))-(5*age_yrs)+5
                        if weight_goal == "Lose Weight":
                            calories = round(0.8*(bmr*ac_lvl), 2)
                            result = str(calories) + " Calories"
                        elif weight_goal == "Maintain Weight":
                            calories = round(bmr*ac_lvl, 2)
                            result = str(calories) + " Calories"
                        elif weight_goal == "Gain Weight":
                            calories = round((bmr*ac_lvl)+500, 2)
                            result = str(calories) + " Calories"
                        else:
                            result = "Please select your weight goal."
                    elif sex == "Female":
                        bmr = (10*weight_lbs/2.2)+(6.25*((height_ft*30.48)+(height_in*0.0833*30.48)))-(5*age_yrs)-161
                        if weight_goal == "Lose Weight":
                            calories = round(0.8*(bmr*ac_lvl), 2)
                            result = str(calories) + " Calories"
                        elif weight_goal == "Maintain Weight":
                            calories = round(bmr*ac_lvl, 2)
                            result = str(calories) + " Calories"
                        elif weight_goal == "Gain Weight":
                            calories = round((bmr*ac_lvl)+500, 2)
                            result = str(calories) + " Calories"
                        else:
                            result = "Please select your weight goal."
                    else:
                        result = "Please select your sex."
                else:
                    result = "Please select your activity level."
            else:
                result = "Please enter numeric values in all of the input boxes."
            # Update the output text
            result_label.text = result
        calc_btn.bind(on_press=callback)
        self.add_widget(calc_btn)
        for i in range(0, 2):
            self.add_widget(Label(text=" "))

        # Row 19
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))

        # Row 20
        # Result
        for i in range(0, 2):
            self.add_widget(Label(text=" "))
        result_label = Label(text=result)
        self.add_widget(result_label)
        for i in range(0, 2):
            self.add_widget(Label(text=" "))

        # Row 21
        # Padding
        for i in range(0, 5):
            self.add_widget(Label(text=" "))


class MyApp(App):
    def build(self):
        self.title = "TRIBE Calorie Calculator"
        return CalculatorInterface()


if __name__ == '__main__':
    MyApp().run()
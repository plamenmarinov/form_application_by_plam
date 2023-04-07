# form_application_by_plam
Simple Form Application

![python_kivy_logo](https://user-images.githubusercontent.com/117172634/230569063-d36795e4-3780-4afb-9191-7574b91f5219.jpg)

![form_pictude](https://user-images.githubusercontent.com/117172634/230569661-658acfbc-f7e0-4991-bee9-c62a3db7498e.JPG)

The Python code defines a Kivy application that displays a form with several input fields for a user to fill out (personal name, family name, email address, phone number, birthdate, password, and password confirmation). When the user clicks the "Send" button, the application validates the input and displays an error message if any field is empty or if the email or phone number are not in the correct format.

The code uses regular expressions to check if the email and phone number are valid. If any of the validation checks fail, a custom exception class FormValidationException is raised with an appropriate error message.

The Kivy code defines the UI layout for the form, with labels and text inputs for each field, as well as a submit button and a label for displaying error messages.

When the form is submitted and all validation checks pass, the application prints the values entered by the user to the console and exits.

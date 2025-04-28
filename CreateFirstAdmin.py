from flet import (
    TextField,
    icons,
    Text,
    OutlinedButton,
    Column,
    Row,
    AlertDialog,
    TextAlign,
)

from Database import UserDatabase
from Notification import Notification
from datetime import date
import bcrypt


class CreateFirstAdmin(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.modal = True
        self.title = Row(
            expand=True,
            alignment="center",
            controls=[
                Text(
                    value="Administrator registration",
                    text_align=TextAlign.CENTER,
                    width=350,
                )
            ],
        )

        self.tf_name = TextField(
            autofocus=True,
            label="Name",
            prefix_icon=icons.PERSON_2_ROUNDED,
            on_change=self.validate_fields,
        )
        self.tf_user = TextField(
            label="User",
            prefix_icon=icons.ASSIGNMENT_IND_ROUNDED,
            on_change=self.validate_fields,
        )
        self.tf_pass1 = TextField(
            label="Insert password",
            password=True,
            prefix_icon=icons.PASSWORD,
            on_change=self.validate_fields,
        )
        self.tf_pass2 = TextField(
            label="Repeat password",
            password=True,
            prefix_icon=icons.PASSWORD,
            on_change=self.validate_fields,
        )
        self.btn_register_user = OutlinedButton(
            text="Register",
            disabled=True,
            icon=icons.ADD_OUTLINED,
            width=140,
            on_click=self.register_admin,
        )

        self.actions = [
            Column(
                expand=True,
                horizontal_alignment="center",
                controls=[
                    self.tf_name,
                    self.tf_user,
                    self.tf_pass1,
                    self.tf_pass2,
                    self.btn_register_user,
                ],
            )
        ]

    def build(self):
        return self

    def validate_fields(self, e):
        required_fields = [
            self.tf_name,
            self.tf_user,
            self.tf_pass1,
            self.tf_pass2,
        ]
        all_filled = all(control.value != "" for control in required_fields)
        all_empty = all(control.value == "" for control in required_fields)

        if all_empty:
            for control in required_fields:
                control.error_text = ""
            self.btn_register_user.disabled = True
            self.update()
            return

        if all_filled:
            if self.tf_pass1.value != self.tf_pass2.value:
                self.tf_pass1.error_text = "Passwords do not match!"
                self.tf_pass2.error_text = "Passwords do not match!"
                self.btn_register_user.disabled = True
                self.update()
                return
            for control in required_fields:
                control.error_text = ""
            self.btn_register_user.disabled = False
            self.update()
            return

        for control in required_fields:
            if control.value == "":
                control.error_text = "Passwords do not match!"
                control.update()
            self.btn_register_user.disabled = True
            self.update()

    def create_hash(self, password):
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_pass.decode("utf-8")

    def prepare_data(self):
        today = date.today()
        form_date = today.strftime("%Y-%m-%d")
        hashed_pass = self.create_hash(self.tf_pass1.value)
        fulldataset = [
            self.tf_name.value,
            self.tf_user.value,
            hashed_pass,
            form_date,
            "Admin",
        ]
        return fulldataset

    def register_admin(self, e):
        fulldataset = self.prepare_data()
        mydb = UserDatabase(self.route)
        mydb.connect()
        result = mydb.register_user(fulldataset)
        mydb.close()

        if result == "success":
            Notification(
                self.route.page, "Administrator registered successfully!", "green"
            ).show_message()
            self.open = False
        else:
            Notification(
                self.route.page, f"Error registering the administrator: {result}", "red"
            ).show_message()

        self.route.page.update()

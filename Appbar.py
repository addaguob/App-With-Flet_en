from flet import (
    UserControl,
    Row,
    Column,
    Container,
    Text,
    IconButton,
    icons,
    colors,
    padding,
    FontWeight,
    alignment,
    MainAxisAlignment,
    CrossAxisAlignment,
    AppBar,
    Icon,
    PopupMenuButton,
    PopupMenuItem,
    Theme,
    ThemeMode,
)
import datetime
import locale
from apscheduler.schedulers.blocking import BlockingScheduler


class Appbar(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

        # Creates the scheduler to update day/hour
        # Start of the scheduler in the Login.initialize() method
        self.scheduler = BlockingScheduler()
        self.scheduler.add_job(self.update_day, "interval", seconds=1)

        self.hour_text = Text("", size=15, weight=FontWeight.W_600)
        self.week_text = Text("", size=12, weight=FontWeight.W_200)
        self.text_title = Text(value="Login", size=26, weight=FontWeight.W_500)
        self.btn_change_theme = IconButton(
            icon=icons.DARK_MODE_OUTLINED,
            tooltip="Light/Dark Theme",
            on_click=self.change_theme,
        )
        self.text_user = Text(
            "Login to access the system!", size=15, weight=FontWeight.W_600
        )
        self.btn_logout = IconButton(
            icon=icons.LOGOUT_OUTLINED,
            disabled=True,
            tooltip="Logout",
            on_click=self.logout,
        )

        locale.setlocale(locale.LC_ALL, "en_US.utf8")

    def build(self):
        self.app_barr = AppBar(
            elevation=10,
            leading_width=180,
            bgcolor=colors.PRIMARY_CONTAINER,
            leading=Container(
                # bgcolor='grey',
                padding=padding.only(left=15),
                alignment=alignment.center,
                content=Row(
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Icon(icons.COTTAGE_OUTLINED, size=36),
                        Column(
                            expand=True,
                            alignment=MainAxisAlignment.CENTER,
                            spacing=0,
                            controls=[self.hour_text, self.week_text],
                        ),
                    ],
                ),
            ),
            title=self.text_title,
            actions=[
                self.btn_change_theme,
                PopupMenuButton(
                    icon=icons.COLOR_LENS_OUTLINED,
                    tooltip="Change theme color",
                    items=[
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED,
                                        color=colors.PURPLE_300,
                                    ),
                                    Text("Purple"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED,
                                        color=colors.ORANGE_300,
                                    ),
                                    Text("Orange"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED,
                                        color=colors.GREEN_300,
                                    ),
                                    Text("Green"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED, color=colors.RED_300
                                    ),
                                    Text("Red"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED, color=colors.BLUE_300
                                    ),
                                    Text("Blue (Default)"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED,
                                        color=colors.YELLOW_300,
                                    ),
                                    Text("Yellow"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED,
                                        color=colors.INDIGO_300,
                                    ),
                                    Text("Indigo"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED, color=colors.TEAL_300
                                    ),
                                    Text("Teal"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED, color=colors.LIME_300
                                    ),
                                    Text("Lime"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                        PopupMenuItem(
                            content=Row(
                                controls=[
                                    Icon(
                                        icons.COLOR_LENS_OUTLINED,
                                        color=colors.BROWN_400,
                                    ),
                                    Text("Brown"),
                                ]
                            ),
                            on_click=self.change_color_seed,
                        ),
                    ],
                ),
                Container(
                    padding=10,
                    content=Column(
                        spacing=0,
                        controls=[
                            Text("Welcome!", size=12),
                            self.text_user,
                        ],
                    ),
                ),
                self.btn_logout,
            ],
        )
        return self.app_barr

    def change_theme(self, e):
        if self.route.page.theme_mode == ThemeMode.LIGHT:
            self.route.page.theme_mode = ThemeMode.DARK
            self.btn_change_theme.icon = icons.WB_SUNNY_OUTLINED
            self.route.page.update()
            return
        if self.route.page.theme_mode == ThemeMode.DARK:
            self.route.page.theme_mode = ThemeMode.LIGHT
            self.btn_change_theme.icon = icons.DARK_MODE_OUTLINED
            self.route.page.update()
            return

    def change_color_seed(self, e):
        self.route.page.theme = Theme(
            color_scheme_seed=e.control.content.controls[0].color
        )
        self.route.page.update()

    def set_title(self, text):
        self.text_title.value = text
        self.text_title.update()

    def enable_btn_logout(self):
        self.btn_logout.disabled = False

    def logout(self, e):
        self.route.page.go("/")
        self.btn_logout.disabled = True
        self.set_username("Log in to access the system!")
        self.set_title("Login")
        # self.update()
        self.route.menu.cont.visible = False
        self.route.menu.update()
        self.route.page.update()

    def set_username(self, text):
        self.text_user.value = text
        self.route.page.update()

    def update_day(self):
        # Gets the current date
        today = datetime.date.today()

        # Gets the current time
        agora = datetime.datetime.now()

        # Formats the time in a string with the format h:m:s
        formatted_time = agora.strftime("%H:%M:%S")

        # Defines the date format for only day and month
        date_format = "%d/%m"

        # Defines the text for the date label
        date_text = today.strftime(date_format)

        # Defines the text for the day of the week label
        day_of_week_text = today.strftime("%A")

        # Defines the text of the labels
        self.hour_text.value = f"{date_text} - {formatted_time}"
        self.week_text.value = day_of_week_text.upper()
        self.hour_text.update()
        self.week_text.update()

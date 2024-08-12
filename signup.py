import flet as ft
import splashscreen
import signin


def main(page: ft.Page):
    page.clean()
    def back_button(e):
        splashscreen.main(page)
    def signin_page(e):
        signin.main(page)

    body = ft.Stack([

        ft.Column([
                ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_ROUNDED, icon_color="black", bgcolor=ft.colors.BLACK26,
                              on_click=back_button),

        ], top=50, left=30),
        ft.Column([
            ft.Text("Register", weight=ft.FontWeight.BOLD, size=30, color=ft.colors.GREEN_900, width=400),

            ft.Text("Create your new Account", color=ft.colors.BLACK54),
        ],top=90,left=100),
        ft.Column([

            ft.TextField(hint_text="Full Name",
                         prefix_icon=ft.icons.SENTIMENT_VERY_SATISFIED,
                         width=300,
                         height=45,
                         border_radius=10,
                         bgcolor=ft.colors.GREEN_100,
                         border_color=ft.colors.GREEN_100,
                         # icon="park_rounded",
                         ),
            ft.TextField(hint_text="user@mail.com",
                         prefix_icon=ft.icons.ALTERNATE_EMAIL_ROUNDED,
                         width=300,
                         height=45,
                         border_radius=10,
                         bgcolor=ft.colors.GREEN_100,
                         border_color=ft.colors.GREEN_100,
                         # icon="park_rounded",
                         ),
            ft.TextField(hint_text="Password",
                         prefix_icon=ft.icons.LOCK_PERSON,
                         width=300,
                         height=45,
                         border_radius=10,
                         bgcolor=ft.colors.GREEN_100,
                         border_color=ft.colors.GREEN_100,
                         password=True,
                         can_reveal_password=True),
            ft.TextField(hint_text="Confirm Password",
                         prefix_icon=ft.icons.LOCK_PERSON,
                         width=300,
                         height=45,
                         border_radius=10,
                         bgcolor=ft.colors.GREEN_100,
                         border_color=ft.colors.GREEN_100,
                         password=True,
                         can_reveal_password=True),
            ft.Row([
                ft.Checkbox(label="Terms and condition", value=False, fill_color=ft.colors.GREEN_100),

            ]),
        ],left=30,top=200),

        ft.Column([
            ft.ElevatedButton(
                text="Register",
                width=260,

                on_click="",
                style=ft.ButtonStyle(bgcolor="green", color="white"),
            ),
            ft.Row([
                ft.Text("Already having account?"),
                ft.TextButton("Signin", on_click=signin_page),

            ])

        ], left=50, top=650),
    ])
    page.add(body)


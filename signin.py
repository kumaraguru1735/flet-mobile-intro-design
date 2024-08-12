import flet as ft

import signup
import splashscreen


def main(page: ft.Page):
    def signin_submit():
        print('form submited')
    page.clean()
    page.bgcolor = "white"
    page.window_width = 370
    page.window_height = 800
    body = ft.Stack([

        ft.Column([

            ft.Image(
                src=f"assests/top.png",
                width=370,
                height=900,
                fit=ft.image.ImageFit.FILL,
            ),
        ],top=0,left=0),
        ft.Column([
            ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_ROUNDED, icon_color="white", bgcolor=ft.colors.WHITE38, on_click=lambda e: splashscreen.main(page)),

        ],top=50,left=45),
        ft.Column([
            ft.Text("Welcome Back", weight=ft.FontWeight.BOLD, size=30, color=ft.colors.GREEN_900,width=400),

            ft.Text("Login to your Account", color=ft.colors.BLACK54),

            ft.TextField(hint_text="Full Name",

                         prefix_icon=ft.icons.SENTIMENT_VERY_SATISFIED,
                         width=300,
                         height=45,
                         border_radius=10,
                         bgcolor=ft.colors.GREEN_100,
                         border_color=ft.colors.GREEN_100,

                         ),
            ft.TextField(hint_text="Password",

                         prefix_icon=ft.icons.LOCK,
                         width=300,
                         height=45,
                         border_radius=10,
                         bgcolor=ft.colors.GREEN_100,
                         border_color=ft.colors.GREEN_100,
                         password=True,
                         can_reveal_password=True),
            ft.Row([
                ft.Checkbox(label="Remember Me",value=False,fill_color=ft.colors.GREEN_100),
                ft.TextButton(text="Forget Password?"),
            ]),


        ],left=30,top=300),

        ft.Column([
            ft.ElevatedButton(
                text="Login",
                width=260,

                on_click=lambda e: signin_submit(),
                style=ft.ButtonStyle(bgcolor="green", color="white"),
            ),
            ft.Row([
                ft.Text("Don't have account?"),
                ft.TextButton("Signup", on_click=lambda e: signup.main(page)),

            ])

        ],left=50,top=650),

    ])


    page.add(body)


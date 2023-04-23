import math
# import CoolProp as CP
from pyXSteam.XSteam import XSteam
from flet import *
import flet as ft


# the content of the icon tab
class TabContentCoolProp(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.icon_color = "red900"
        self.icon_name = "cake_rounded"

        self.icon_obj = ft.Ref[ft.Icon]()

        # text field for color property of the Icon object
        self.field_color = ft.TextField(
            label="color",
            value="red900",
            on_submit=self.update_icon,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for the name property of the Icon object
        self.field_name = ft.TextField(
            label="name",
            hint_text="ft.icons.COPY or COPY or copy",
            value="cake_rounded",
            on_submit=self.update_icon,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=2
        )
        
        # text field for pressure
        self.field_pressure = ft.TextField(
            label="pressure",
            value="",
            helper_text="Optional[str]",
            on_change=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )
        
        # text field for temperature    
        self.field_temperature = ft.TextField(
            label="temperature",
            value="",
            helper_text="Optional[str]",
            on_change=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_name, self.field_color],
                ),
                ft.Row(
                    [self.field_pressure, self.field_temperature],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=11
        )
        # self.result = CP.CoolProp.PropsSI("T", "P", 101325, "Q", 0, "Water")
        self.result = "coolprop result"
        self.steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS) # m/kg/sec/°C/bar/W

        return ft.Column(
            [
                ft.Text("BRFLUID web:", weight=ft.FontWeight.BOLD, size=21),
                all_fields,
                ft.Row(
                    [
                        ft.Icon(
                            ref=self.icon_obj,
                            name="cake_rounded",
                            color="red900"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.Text(self.result)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.Text(self.steamTable.hL_p(210.0))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.FilledButton(
                            "Copy Value to Clipboard",
                            icon=ft.icons.COPY,
                            on_click=self.copy_to_clipboard
                        ),
                        ft.FilledTonalButton(
                            "Go to Docs",
                            icon=ft.icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/icon")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=25
        )

    def update_icon(self, e: ft.ControlEvent):
        """
        It updates the Icon object.
        :param e: The event object
        """
        self.icon_color = self.field_color.value.strip() if self.field_color.value.strip() else None
    
    
        # name
        try:
            if self.icon_name is not None:
                self.icon_name = eval(self.icon_name) if '.' in self.icon_name else self.icon_name.lower()

                # Getting all the icons from flet's icons module
                list_started = False
                all_flet_icons = list()
                for value in vars(ft.icons).values():
                    if value == "ten_k":
                        list_started = True
                    if list_started:
                        all_flet_icons.append(value)

                # checking if all the entered icons exist in flet
                if self.icon_name not in all_flet_icons:
                    raise ValueError("Wrong Value!")
        except Exception as x:
            print(f"Name Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: There seems to be an error with your icon's name. See the Icon tabs for "
                        f"help with choosing an icon name!"),
                    open=True))
            return
        
        # color
        try:
            if self.icon_color is not None:
                self.icon_color = eval(self.icon_color) if '.' in self.icon_color else self.icon_color.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.icon_color not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Color Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return


        self.icon_obj.current.color = self.icon_color
        self.icon_obj.current.name = self.icon_name

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Icon!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """It copies the tooltip object/instance to the clipboard."""
        c = f", color='{self.icon_color}'"

        others = f"{c if self.icon_color is not None else ''}"
        val = f"Icon(name='{self.icon_name}',{others if others else ''})"
        e.page.set_clipboard(val)
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {val}"), open=True))
        print(val)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentCoolProp())


    ft.app(main)

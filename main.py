import flet as ft
from utils.icon_utils import TabContentIcon
from utils.coolprop_utils import TabContentCoolProp
from utils.padding_utils import TabContentPadding
from utils.alignment_utils import TabContentAlignment
from utils.border_utils import TabContentBorder
from utils.border_radius_utils import TabContentBorderRadius
from utils.colors_utils import TabContentColors1, TabContentColors2
from utils.icons_browser_utils import TabContentIconsBrowser
from utils.gradient_utils import TabContentLinearGradient, TabContentSweepGradient, TabContentRadialGradient
from utils.shadermask_utils import TabContentShaderMask
from utils.shape_utils import TabContentShape
from utils.tooltip_utils import TabContentTooltip
from utils.progress_ring_utils import TabContentProgressRing
from utils.progress_bar_utils import TabContentProgressBar
from utils.divider_utils import TabContentDivider
from utils.vertical_divider_utils import TabContentVerticalDivider
from utils.circle_avatar_utils import TabContentCircleAvatar
from utils.shadow_utils import TabContentShadow
from utils.blur_utils import TabContentBlur


def main(page: ft.Page):
    # the title of the app
    page.title = "BRFLUID App"

    # a light/bright theme
    page.theme_mode = "light"

    # use material 2 design theme | this is just to better mimic the Flutter example
    page.theme = ft.Theme(use_material3=False)

    # page.window_always_on_top = True
    page.vertical_alignment = "start"


    # the page's alignment
    # page.horizontal_alignment = "center"
    # page.vertical_alignment = "center"
    
    # set the width and height of the window.
    page.window_width = 800
    page.window_height = 900


    def change_theme(e):
        """
        Changes the app's theme_mode, from dark to light or light to dark.

        :param e: The event that triggered the function
        :type e: ControlEvent
        """
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"  # changes the page's theme_mode
        theme_icon_button.selected = not theme_icon_button.selected  # changes the icon
        page.update()

    theme_icon_button = ft.IconButton(
        ft.icons.DARK_MODE,
        selected=False,
        selected_icon=ft.icons.LIGHT_MODE,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
        style=ft.ButtonStyle(color={"": ft.colors.BLACK, "selected": ft.colors.WHITE}, ),
    )

    # the app's appbar
    page.appbar = ft.AppBar(
        title=ft.Text(
            "BRFLUID Apps Page", 
            color=ft.colors.WHITE),  # a title of white color
        bgcolor=ft.colors.DEEP_PURPLE,  # a blue background color
        center_title=True,  # center the title || without this, the title will be on the left
        actions=[theme_icon_button],
        leading=ft.IconButton(
            icon=ft.icons.CODE,
            icon_color=ft.colors.GREEN_500,
            on_click=lambda e: page.launch_url(
                "https://github.com/tobony/flet-test02/"),
            tooltip="View Code"
        ),
    )



    # def increment_counter(e):
    #     """Increment the value of the counter_text object by 1, and update the UI to reflect these changes."""
    #     counter_text.value = str(int(counter_text.value) + 1)
    #     page.update()


    # # text that contains the counter number to be incremented
    # counter_text = ft.Text("0", style=ft.TextThemeStyle.DISPLAY_MEDIUM)

    # # the app's FAB
    # page.floating_action_button = ft.FloatingActionButton(
    #     content=ft.Icon(ft.icons.ADD, color=ft.colors.WHITE),
    #     shape=ft.CircleBorder(),  # gives the button a round/circle shape
    #     on_click=increment_counter,  # the callback to be executed when this button is clicked
    #     tooltip="Increment",  # the text to be shown when this button is hovered
    #     bgcolor=ft.colors.BLUE  # a blue background color
    # )

    # adding our widgets/controls to the page/UI
    # page.add(
    #     ft.Text("You have pushed the button this many times:"),
    #     counter_text
    # )




    ###### another example ######
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=80)
    
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Text("You have pushed the button this many times:"),
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            )
        )
    
    
    
    ###########################################
    ## another example
    icon_coolprop = TabContentCoolProp()
    icon_content = TabContentIcon()
    tooltip_content = TabContentTooltip()
    progress_ring_content = TabContentProgressRing()
    # progress_bar_content = TabContentProgressBar()
    # divider_content = TabContentDivider()
    # vertical_divider_content = TabContentVerticalDivider()
    # circle_avatar_content = TabContentCircleAvatar()
    border_radius_content = TabContentBorderRadius()
    # padding_content = TabContentPadding()
    icons_browser_content = TabContentIconsBrowser()
    # colors1_content = TabContentColors1()
    colors2_content = TabContentColors2(page)
    # alignment_content = TabContentAlignment()
    # shape_content = TabContentShape()
    # shadow_content = TabContentShadow()
    # blur_content = TabContentBlur()
    # border_content = TabContentBorder()
    # linear_gradient_content = TabContentLinearGradient()
    # radial_gradient_content = TabContentRadialGradient()
    # sweep_gradient_content = TabContentSweepGradient()
    # shader_mask_content = TabContentShaderMask()

    page.add(
        ft.Tabs(
            expand=True,
            selected_index=0,
            tabs=[
                ft.Tab(
                    text="CoolProp",
                    content=icon_coolprop
                ),
                ft.Tab(
                    text="Icon",
                    content=icon_content
                ),
                ft.Tab(
                    text="Tooltip",
                    content=tooltip_content
                ),
                ft.Tab(
                    text="ProgressRing",
                    content=progress_ring_content
                ),
                # ft.Tab(
                #     text="ProgressBar",
                #     content=progress_bar_content
                # ),
                # ft.Tab(
                #     text="Divider",
                #     content=divider_content
                # ),
                # ft.Tab(
                #     text="VerticalDivider",
                #     content=vertical_divider_content
                # ),
                # ft.Tab(
                #     text="CircleAvatar",
                #     content=circle_avatar_content
                # ),
                # ft.Tab(
                #     text="Shadow",
                #     content=shadow_content
                # ),
                # ft.Tab(
                #     text="Blur",
                #     content=blur_content
                # ),
                ft.Tab(
                    text="BorderRadius",
                    content=border_radius_content
                ),
                # ft.Tab(
                #     text="Padding",
                #     content=padding_content
                # ),
                ft.Tab(
                    text="Icons Browser",
                    content=icons_browser_content
                ),
                # ft.Tab(
                #     text="Colors V1",
                #     content=colors1_content
                # ),
                ft.Tab(
                    text="Colors V2",
                    content=colors2_content
                ),
                # ft.Tab(
                #     text="Alignment",
                #     content=alignment_content
                # ),
                # ft.Tab(
                #     text="Shape",
                #     content=shape_content
                # ),
                # ft.Tab(
                #     text="Border",
                #     content=border_content
                # ),
                # ft.Tab(
                #     text="Linear Gradient",
                #     content=linear_gradient_content
                # ),
                # ft.Tab(
                #     text="Radial Gradient",
                #     content=radial_gradient_content
                # ),
                # ft.Tab(
                #     text="Sweep Gradient",
                #     content=sweep_gradient_content
                # ),
                # ft.Tab(
                #     text="Shader Mask",
                #     content=shader_mask_content
                # ),
            ]
        ),
        ft.Text(
            "BRFLUID, original example from @ndonkoHenri",
            # style=ft.TextThemeStyle.LABEL_SMALL,
            style=ft.TextThemeStyle.BODY_SMALL,
            weight=ft.FontWeight.BOLD,
            italic=True,
            color=ft.colors.BLUE_900,
        )
    )

# open a browser tab containing the app | remove the view parameter to open in a native OS window
ft.app(
    target=main, 
    route_url_strategy="path",
    assets_dir="assets",
    view=ft.WEB_BROWSER,
    )
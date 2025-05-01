from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: 1, 1, 1, 1

    # Green curved shape top-right
    FloatLayout:
        canvas:
            Color:
                rgba: 0.0, 0.6, 0.0, 1
            Ellipse:
                pos: self.width - dp(200), self.height - dp(200)
                size: dp(400), dp(400)

    # Back Button
    MDRoundFlatIconButton:
        icon: "arrow-left"
        text: ""
        size_hint: None, None
        size: dp(40), dp(40)
        pos_hint: {"x": 0.03, "top": 0.96}
        md_bg_color: 0.0, 0.6, 0.0, 1
        text_color: 1, 1, 1, 1
        icon_color: 1, 1, 1, 1

    # Top image (Student icon)
    Image:
        source: "https://img.icons8.com/ios-filled/500/student-male.png"
        size_hint: None, None
        size: dp(160), dp(160)
        pos_hint: {"center_x": 0.5, "top": 0.78}

    # Title: LET’S GET STARTED
    MDLabel:
        text: "LET’S GET STARTED"
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0.05, 0.05, 0.3, 1
        pos_hint: {"center_x": 0.5}
        size_hint_y: None
        height: self.texture_size[1]

    # Subtitle: LOGIN
    MDLabel:
        text: "LOGIN"
        font_style: "Subtitle1"
        halign: "center"
        theme_text_color: "Secondary"
        pos_hint: {"center_x": 0.5}
        size_hint_y: None
        height: self.texture_size[1]

    # Form fields
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(12)
        padding: dp(30), 0
        size_hint: 1, None
        height: self.minimum_height
        pos_hint: {"center_x": 0.5, "center_y": 0.45}

        MDTextField:
            hint_text: "+88-01XXXXXXXXX"
            mode: "rectangle"
            fill_color_normal: 0.9, 1, 0.9, 1
            radius: [20, 20, 20, 20]
            line_color_focus: 0.0, 0.6, 0.0, 1
            icon_right: "account"
            icon_right_color: 0.2, 0.2, 0.2, 1

        MDTextField:
            hint_text: "Email Address"
            mode: "rectangle"
            fill_color_normal: 0.9, 1, 0.9, 1
            radius: [20, 20, 20, 20]
            line_color_focus: 0.0, 0.6, 0.0, 1
            icon_right: "email"
            icon_right_color: 0.2, 0.2, 0.2, 1

        MDTextField:
            hint_text: "Enter Password"
            mode: "rectangle"
            password: True
            fill_color_normal: 0.9, 1, 0.9, 1
            radius: [20, 20, 20, 20]
            line_color_focus: 0.0, 0.6, 0.0, 1
            icon_right: "eye"
            icon_right_color: 0.2, 0.2, 0.2, 1

    # Login Button
    MDRaisedButton:
        text: "LOGIN"
        md_bg_color: 0.0, 0.6, 0.0, 1
        text_color: 1, 1, 1, 1
        size_hint: 0.9, None
        height: dp(48)
        radius: [25, 25, 25, 25]
        pos_hint: {"center_x": 0.5, "y": 0.16}

    # Graduation cap image
    Image:
        source: "https://img.icons8.com/ios/500/graduation-cap.png"
        size_hint: None, None
        size: dp(90), dp(90)
        pos_hint: {"center_x": 0.5, "y": 0.08}

    # Bottom blue ellipse
    FloatLayout:
        size_hint: 1, None
        height: dp(160)
        pos_hint: {"y": 0}
        canvas:
            Color:
                rgba: 0.05, 0.05, 0.3, 1
            Ellipse:
                pos: self.x, self.y - dp(80)
                size: self.width, dp(300)
'''

class PixelPerfectLoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

if __name__ == '__main__':
    PixelPerfectLoginApp().run()

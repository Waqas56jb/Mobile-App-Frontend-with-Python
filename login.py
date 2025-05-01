from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: 1, 1, 1, 1  # White background

    # Green curved top-right corner
    MDBoxLayout:
        size_hint: None, None
        size: dp(200), dp(200)
        pos_hint: {"right": 1, "top": 1}
        canvas:
            Color:
                rgba: 0.0, 0.6, 0.0, 1  # Green
            Ellipse:
                pos: self.pos
                size: self.size

    # Back button
    MDRoundFlatIconButton:
        icon: "arrow-left"
        text: ""
        pos_hint: {"x": 0.03, "top": 0.96}
        md_bg_color: 0.0, 0.6, 0.0, 1
        text_color: 1, 1, 1, 1
        icon_color: 1, 1, 1, 1
        size_hint: None, None
        size: dp(40), dp(40)
        padding: 0

    # Top illustration
    Image:
        source: "https://img.icons8.com/ios-filled/500/student-male.png"
        size_hint: None, None
        size: dp(160), dp(160)
        pos_hint: {"center_x": 0.5, "top": 0.78}

    # Title: LET'S GET STARTED
    MDLabel:
        text: "LET’S GET STARTED"
        font_style: "H5"
        halign: "center"
        bold: True
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

    # Login form
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(10)
        padding: dp(30), dp(10)
        size_hint: 1, None
        height: self.minimum_height
        pos_hint: {"center_x": 0.5, "center_y": 0.45}

        MDTextField:
            hint_text: "+88-01XXXXXXXXX"
            mode: "rectangle"
            fill_color_normal: 0.8, 1, 0.8, 1
            line_color_focus: 0.0, 0.6, 0.0, 1
            radius: [25, 25, 25, 25]
            icon_right: "account"
            icon_right_color: 0.2, 0.2, 0.2, 1

        MDTextField:
            hint_text: "Email Address"
            mode: "rectangle"
            fill_color_normal: 0.8, 1, 0.8, 1
            line_color_focus: 0.0, 0.6, 0.0, 1
            radius: [25, 25, 25, 25]
            icon_right: "eye"
            icon_right_color: 0.2, 0.2, 0.2, 1

        MDTextField:
            hint_text: "Enter Password"
            mode: "rectangle"
            password: True
            fill_color_normal: 0.8, 1, 0.8, 1
            line_color_focus: 0.0, 0.6, 0.0, 1
            radius: [25, 25, 25, 25]
            icon_right: "eye"
            icon_right_color: 0.2, 0.2, 0.2, 1

    # Bottom image (replaced with icon)
    Image:
        source: "https://img.icons8.com/ios/500/graduation-cap.png"
        size_hint: None, None
        size: dp(100), dp(100)
        pos_hint: {"center_x": 0.5, "y": 0.15}

    # Bottom dark curve
    MDBoxLayout:
        size_hint: 1, None
        height: dp(120)
        pos_hint: {"y": 0}
        canvas:
            Color:
                rgba: 0.05, 0.05, 0.3, 1
            Ellipse:
                pos: self.x, self.y - dp(60)
                size: self.width, dp(240)

    # Green login button centered
    MDRaisedButton:
        text: "LOGIN"
        md_bg_color: 0.0, 0.6, 0.0, 1
        text_color: 1, 1, 1, 1
        size_hint: 0.9, None
        height: dp(50)
        pos_hint: {"center_x": 0.5, "y": 0.05}
        radius: [25, 25, 25, 25]
'''

class PixelPerfectLoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

if __name__ == '__main__':
    PixelPerfectLoginApp().run()

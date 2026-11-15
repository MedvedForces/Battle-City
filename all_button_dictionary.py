from map import GameMap
from button import ImageButton

WIDTH = 512
HEIGHT = 512

class ButtonManager:
    def __init__(self, buttons_type):
        self.buttons = None
        self.buttons_type = buttons_type

    def __getitem__(self, key):
        if self.buttons is None:
            self._initialize_buttons()
        return self.buttons[key]

    def _initialize_buttons(self):
        if self.buttons_type == "buttons_custom_level":
            self.buttons = {
                "button_player": ImageButton(GameMap.WIDTH, 32 * 2,
                                             32, 32, "",
                                             "sprites/tank10.png",
                                             "",
                                             "Музыка/click_button.wav"),
                "button_play": ImageButton(GameMap.WIDTH + 32 * 0, 32 * 14,
                                            32 * 2, 32 * 2, "",
                                            "sprites/загруженное.jpg",
                                            "",
                                            "Музыка/click_button.wav"),
                "button_bot_default": ImageButton(GameMap.WIDTH, 32 * 3,
                                           32, 32, "",
                                           "sprites/tank9.png",
                                           "",
                                           "Музыка/click_button.wav"),
                "button_bot_chasing": ImageButton(GameMap.WIDTH, 32 * 4,
                                                  32, 32, "",
                                                  "sprites/tank8.png",
                                                  "",
                                                  "Музыка/click_button.wav"),
                "button_brick": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 2,
                                           32, 16, "",
                                           "sprites/half_brick.png",
                                           "",
                                           "Музыка/click_button.wav"),
                "button_water": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 6,
                                            32, 32, "",
                                            "sprites/whole_water.png",
                                            "",
                                            "Музыка/click_button.wav"),
                "button_steel": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 3,
                                            32, 32, "",
                                            "sprites/steel.png",
                                            "",
                                            "Музыка/click_button.wav"),
                "button_ice": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 4,
                                            32, 32, "",
                                            "sprites/block_ice.png",
                                            "",
                                            "Музыка/click_button.wav"),
                "button_bird": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 5,
                                          32, 32, "",
                                          "sprites/bird.png",
                                          "",
                                          "Музыка/click_button.wav"),
                "button_bonus_hp": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 9,
                                           32, 32, "",
                                           "sprites/bonus_tank.png",
                                           "",
                                           "Музыка/click_button.wav"),
                "button_bonus_armor": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 10,
                                               32, 32, "",
                                               "sprites/bonus_helmet.png",
                                               "",
                                               "Музыка/click_button.wav"),
                "button_delete_all": ImageButton(GameMap.WIDTH + 32 * 1, 0,
                                                 32, 32, "",
                                                 "sprites/button_delete_all.png",
                                                 "",
                                                 "Музыка/click_button.wav")
            }

        elif self.buttons_type == "buttons_setting_menu":
            self.buttons = {
                "button_audio": ImageButton(WIDTH / 2 - (252 / 2), 100,
                                   252, 74, "Audio",
                                   "sprites/green_button2.jpg",
                                   "sprites/green_button2_hover.jpg",
                                   "Музыка/click_button.wav"),
                "button_video": ImageButton(WIDTH / 2 - (252 / 2), 200,
                                   252, 74, "Video",
                                   "sprites/green_button2.jpg",
                                   "sprites/green_button2_hover.jpg",
                                   "Музыка/click_button.wav"),
                "button_back": ImageButton(WIDTH / 2 - (252 / 2), 300,
                                  252, 74, "Back",
                                  "sprites/green_button2.jpg",
                                  "sprites/green_button2_hover.jpg",
                                  "Музыка/click_button.wav")
            }
        elif self.buttons_type == "buttons_main_menu":
            self.buttons = {
                "button_level1" : ImageButton(WIDTH / 2 - (252 / 2), 100,
                                            252, 74, "Level1",
                                            "sprites/green_button2.jpg",
                                            "sprites/green_button2_hover.jpg",
                                            "Музыка/click_button.wav"),
                "button_level2" : ImageButton(WIDTH / 2 - (252 / 2), 200,
                                        252, 74, "Level2",
                                        "sprites/green_button2.jpg",
                                        "sprites/green_button2_hover.jpg",
                                        "Музыка/click_button.wav"),
                "button_create_level" : ImageButton(WIDTH / 2 - (252 / 2), 300,
                                              252, 74, "Create Level",
                                              "sprites/green_button2.jpg",
                                              "sprites/green_button2_hover.jpg",
                                              "Музыка/click_button.wav"),
                "button_settings" : ImageButton(WIDTH / 2 - (252 / 2), 400,
                                          252, 74, "Settings",
                                          "sprites/green_button2.jpg",
                                          "sprites/green_button2_hover.jpg",
                                          "Музыка/click_button.wav")
            }


buttons_custom_level = ButtonManager("buttons_custom_level")
buttons_setting_menu = ButtonManager("buttons_setting_menu")
buttons_main_menu = ButtonManager("buttons_main_menu")
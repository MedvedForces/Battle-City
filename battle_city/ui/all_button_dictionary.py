from ..core.map import GameMap
from .button import ImageButton
from ..core.paths import audio_path, sprite_path

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
                                             sprite_path("tank10.png"),
                                             "",
                                             audio_path("click_button.wav")),
                "button_play": ImageButton(GameMap.WIDTH + 32 * 0, 32 * 14,
                                            32 * 2, 32 * 2, "",
                                            sprite_path("загруженное.jpg"),
                                            "",
                                            audio_path("click_button.wav")),
                "button_bot_default": ImageButton(GameMap.WIDTH, 32 * 3,
                                           32, 32, "",
                                           sprite_path("tank9.png"),
                                           "",
                                           audio_path("click_button.wav")),
                "button_bot_chasing": ImageButton(GameMap.WIDTH, 32 * 4,
                                                  32, 32, "",
                                                  sprite_path("tank8.png"),
                                                  "",
                                                  audio_path("click_button.wav")),
                "button_brick": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 2,
                                           32, 16, "",
                                           sprite_path("half_brick.png"),
                                           "",
                                           audio_path("click_button.wav")),
                "button_water": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 6,
                                            32, 32, "",
                                            sprite_path("whole_water.png"),
                                            "",
                                            audio_path("click_button.wav")),
                "button_steel": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 3,
                                            32, 32, "",
                                            sprite_path("steel.png"),
                                            "",
                                            audio_path("click_button.wav")),
                "button_ice": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 4,
                                            32, 32, "",
                                            sprite_path("block_ice.png"),
                                            "",
                                            audio_path("click_button.wav")),
                "button_bird": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 5,
                                          32, 32, "",
                                          sprite_path("bird.png"),
                                          "",
                                          audio_path("click_button.wav")),
                "button_bonus_hp": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 9,
                                           32, 32, "",
                                           sprite_path("bonus_tank.png"),
                                           "",
                                           audio_path("click_button.wav")),
                "button_bonus_armor": ImageButton(GameMap.WIDTH + 32 * 1, 32 * 10,
                                               32, 32, "",
                                               sprite_path("bonus_helmet.png"),
                                               "",
                                               audio_path("click_button.wav")),
                "button_delete_all": ImageButton(GameMap.WIDTH + 32 * 1, 0,
                                                 32, 32, "",
                                                 sprite_path("button_delete_all.png"),
                                                 "",
                                                 audio_path("click_button.wav"))
            }

        elif self.buttons_type == "buttons_setting_menu":
            self.buttons = {
                "button_audio": ImageButton(WIDTH / 2 - (252 / 2), 100,
                                   252, 74, "Audio",
                                   sprite_path("green_button2.jpg"),
                                   sprite_path("green_button2_hover.jpg"),
                                   audio_path("click_button.wav")),
                "button_video": ImageButton(WIDTH / 2 - (252 / 2), 200,
                                   252, 74, "Video",
                                   sprite_path("green_button2.jpg"),
                                   sprite_path("green_button2_hover.jpg"),
                                   audio_path("click_button.wav")),
                "button_back": ImageButton(WIDTH / 2 - (252 / 2), 300,
                                  252, 74, "Back",
                                  sprite_path("green_button2.jpg"),
                                  sprite_path("green_button2_hover.jpg"),
                                  audio_path("click_button.wav"))
            }
        elif self.buttons_type == "buttons_main_menu":
            self.buttons = {
                "button_level1" : ImageButton(WIDTH / 2 - (252 / 2), 100,
                                            252, 74, "Level1",
                                            sprite_path("green_button2.jpg"),
                                            sprite_path("green_button2_hover.jpg"),
                                            audio_path("click_button.wav")),
                "button_level2" : ImageButton(WIDTH / 2 - (252 / 2), 200,
                                        252, 74, "Level2",
                                        sprite_path("green_button2.jpg"),
                                        sprite_path("green_button2_hover.jpg"),
                                        audio_path("click_button.wav")),
                "button_create_level" : ImageButton(WIDTH / 2 - (252 / 2), 300,
                                              252, 74, "Create Level",
                                              sprite_path("green_button2.jpg"),
                                              sprite_path("green_button2_hover.jpg"),
                                              audio_path("click_button.wav")),
                "button_settings" : ImageButton(WIDTH / 2 - (252 / 2), 400,
                                          252, 74, "Settings",
                                          sprite_path("green_button2.jpg"),
                                          sprite_path("green_button2_hover.jpg"),
                                          audio_path("click_button.wav"))
            }


buttons_custom_level = ButtonManager("buttons_custom_level")
buttons_setting_menu = ButtonManager("buttons_setting_menu")
buttons_main_menu = ButtonManager("buttons_main_menu")
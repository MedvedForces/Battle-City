import pygame


class GameMap:
    FPS = 60
    WIDTH, HEIGHT = 512 - 32 * 2, 512 - 32 * 2
    SIZE = 32
    SIZE_BRICK_WIDTH = 32
    SIZE_BRICK_HEIGHT = 16

    tanks = []
    blocks = []
    shells = []
    ui_list = []
    bonuses = []

    count_bird = 0 #идет пересчет в Levels

    DIRECTIONS = {
        "Left": (-1, 0),
        "Right": (1, 0),
        "Up": (0, -1),
        "Down": (0, 1)
    }

    ROTATIONS = {
        "Left": 90,
        "Right": 270,
        "Up": 0,
        "Down": 180
    }

    #@classmethod
    #def init(cls):
        #if not pygame.get_init():
        #    pygame.init()

        #cls.window = pygame.display.set_mode((cls.WIDTH, cls.HEIGHT))
        #cls.clock = pygame.time.Clock()
        #cls.fontUI = pygame.font.Font(None, 30)

    @classmethod
    def load_resources(cls):
        cls.load_textures()
        cls.load_sounds()

    @classmethod
    def load_textures(cls):
        cls.img_brick = pygame.image.load("sprites/half_brick.png")
        cls.img_ice = pygame.image.load("sprites/block_ice.png")
        cls.img_water = pygame.image.load("sprites/whole_water.png")

        cls.img_bonus_hp = pygame.image.load("sprites/bonus_tank.png")
        cls.img_bonus_armor = pygame.image.load("sprites/bonus_helmet.png")

        cls.img_brick = pygame.transform.scale(cls.img_brick, (
        cls.SIZE_BRICK_WIDTH, cls.SIZE_BRICK_HEIGHT))

        cls.img_bird = pygame.image.load("sprites/bird.png")
        cls.img_steel = pygame.image.load("sprites/steel1.png")
        cls.img_tanks = [pygame.image.load(f"sprites/tank{i}.png") for i in
                         range(1, 11)]
        cls.img_bangs = [pygame.image.load(f"sprites/bang{i}.png") for i in
                         range(1, 4)]

    @classmethod
    def load_sounds(cls):
        cls.shot_sound = pygame.mixer.Sound("Музыка/shot.wav")

    @classmethod
    def clean_map(cls):
        cls.tanks = []
        cls.shells = []
        cls.blocks = []
        cls.ui_list = []
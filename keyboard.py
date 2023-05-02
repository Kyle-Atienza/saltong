import pygame
from assets import theme as theme

fonts = theme.fonts('assets/fonts/')

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "C", "V", "B", "N", "M"]
]



class Key(pygame.sprite.Sprite):
    def __init__(self, col, row, character):
        super().__init__()

        self.character = character
        self.content = None
        self.content_rect = None
        self.status = "default"

        self.col = col
        self.row = row

        self.gap = 15
        self.width = 50
        self.height = 70

        self.dimensions = (self.width, self.height)
        self.image = pygame.Surface(self.dimensions)
        self.image.fill(theme.colors["white"])

        self.rect = self.image.get_rect()
        self.rect.x = self.col * (self.width + self.gap)
        self.rect.y = self.row * (self.height + self.gap)

        self.render_content()

    def set_status(self, status):
        self.status = status
        self.render_content()

    def get_character(self):
        return self.character

    def render_content(self):
        if self.status == "default":
            self.image.fill(theme.colors["white"])
        elif self.status == "true":
            self.image.fill(theme.colors["success"])
        elif self.status == "false":
            self.image.fill(theme.colors["gray"])
        elif self.status == "maybe":
            self.image.fill(theme.colors["primary"])

        self.content = fonts["characters"].render(self.character, True, "#000000")
        self.content_rect = self.content.get_rect(center=(self.width / 2, self.height / 2))

        self.image.blit(self.content, self.content_rect)


width = 0
height = 0
rows = [{} for i in range(len(keys))]

group = pygame.sprite.Group()

for row_index, row in enumerate(keys):
    row_height = 0
    row_width = 0
    row_group = pygame.sprite.Group()

    for key_index, key in enumerate(row):
        key = Key(key_index, 0, key)
        row_group.add(key)

        row_width += key.width + key.gap
        if key_index == 0:
            # only run one time in the row
            row_height += key.height + key.gap
    if row_width > width:
        width = row_width
    height += row_height

    row_surface = pygame.Surface((row_width, row_height))
    row_surface.fill(theme.colors["base"])
    rows[row_index]["y"] = int((row_height * row_index) + (row_height / 2))
    rows[row_index]["surface"] = row_surface
    rows[row_index]["group"] = row_group

    row_group.draw(row_surface)


surface = pygame.Surface((width, height))
surface.fill(theme.colors["base"])
surface_rect = surface.get_rect(center=(theme.screen_horizontal / 2, 550))


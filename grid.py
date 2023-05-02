import pygame
from assets import theme as theme

fonts = theme.fonts('assets/fonts/')

box_width = 50
box_height = 50

class GridBox(pygame.sprite.Sprite):
    def __init__(self, width, height, col, row):
        super().__init__()

        self.character = ""
        self.content = None
        self.content_rect = None
        self.status = 'default'

        self.col = col
        self.row = row

        self.gap = 15
        self.width = width
        self.height = height

        self.dimensions = (self.width, self.height)
        self.image = pygame.Surface(self.dimensions)
        self.rect = self.image.get_rect()
        self.rect.x = self.col * (self.width + self.gap)
        self.rect.y = self.row * (self.height + self.gap)

        self.set_status(self.status)
        self.render_content()

    def set_status(self, status):
        self.status = status
        self.render_content()

    def update(self, character):
        self.character = character
        self.set_status(self.status)
        self.render_content()

    def reset(self):
        self.character = ""
        self.set_status("default")
        self.render_content()

    def get_character(self):
        return self.character

    def render_content(self):
        if self.status == "active":
            self.image.fill(theme.colors["blue"])
        elif self.status == "default":
            self.image.fill(theme.colors["white"])
        elif self.status == "true":
            self.image.fill(theme.colors["success"])
        elif self.status == "false":
            self.image.fill(theme.colors["gray"])
        elif self.status == "maybe":
            self.image.fill(theme.colors["primary"])

        self.content = fonts["characters"].render(self.character, True, theme.colors["white"])
        self.content_rect = self.content.get_rect(center=(self.width / 2, self.height / 2))

        self.image.blit(self.content, self.content_rect)


group = pygame.sprite.Group()
group_rect = None
group_width = 0
group_height = 0
cols_count = 5
rows_count = 5
current_col = 0
current_row = 0


def reset():
    for box in group.sprites():
        box.reset()


def active_row():
    start = current_row * rows_count
    end = (current_row * rows_count) + rows_count
    return group.sprites()[start:end]


def set_active_row():
    for box in active_row():
        box.set_status("active")


def get_row_word():
    row_word = ''
    for box in active_row():
       row_word += box.get_character()

    return row_word


def get_words():
    words = []
    for row_index in range(current_row):
        word = ""
        start = row_index * rows_count
        end = (row_index * rows_count) + rows_count
        for box in group.sprites()[start:end]:
            word += box.get_character()
        words.append(word)

        word = ""

    return words



for row in range(rows_count):
    for col in range(cols_count):
        box = GridBox(box_width, box_height, col, row)
        group.add(box)

        # get dimensions of grid
        if col == 0:
            group_width += box.width + box.gap
            group_height += box.height + box.gap

group_surface = pygame.Surface((group_width, group_height))
group_surface_rect = group_surface.get_rect(center=(theme.screen_horizontal / 2, 210))
group_surface.fill(theme.colors["base"])
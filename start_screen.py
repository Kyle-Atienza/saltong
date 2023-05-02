import pygame
from assets import theme as theme

fonts = theme.fonts('assets/fonts/')

title = fonts["start_screen_title"].render("Saltong", True, theme.colors["secondary"])
title_rect = title.get_rect(center=(theme.screen_horizontal/2, 290))

button_start = fonts["start_screen_button"].render("Tara", True, theme.colors["secondary"])
button_start_rect = button_start.get_rect(center=(480, 400))
button_start_rect.size = (200, button_start.get_height() + 15)


def render(screen):
    screen.blit(title, title_rect)
    pygame.draw.rect(screen, theme.colors["primary"], button_start_rect)
    screen.blit(button_start, (button_start_rect.centerx - button_start.get_width() // 2,
                                        button_start_rect.centery - button_start.get_height() // 2))



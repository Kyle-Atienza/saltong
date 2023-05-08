import pygame

from assets import theme as theme

fonts = theme.fonts('assets/fonts/')

width = 450
height = 500

close = pygame.image.load('assets/images/bulb.png')
close_rect = close.get_rect(topright=(width-25,30))

squiggle = pygame.image.load('assets/images/wavy.png')
squiggle_rect = squiggle.get_rect(topright=(width/2,320))

answer_label = fonts["modal_paragraph"].render("And Salita ay", True, theme.colors["secondary"])
answer_label_rect = answer_label.get_rect(center=(width/2, 120))

button_reset = fonts["button_label"].render("Maglaro Muli!", True, theme.colors["secondary"])
button_reset_rect = button_reset.get_rect(center=(180, 230))
button_reset_rect.size = (200, button_reset.get_height() + 15)

duration_label = fonts["modal_paragraph"].render("Tumagal ka ng", True, theme.colors["secondary"])
duration_label_rect = duration_label.get_rect(center=(110, 340))

moves_label = fonts["modal_paragraph"].render("Bilang ng Subok", True, theme.colors["secondary"])
moves_label_rect = moves_label.get_rect(center=(width-120, 340))

content_surface = pygame.Surface((width, height))
content_surface.fill(theme.colors["base"])
content_rect = content_surface.get_rect(center=theme.screen_center)

surface = pygame.Surface(theme.screen_size, pygame.SRCALPHA)
surface.fill(theme.colors["modal_base"])
rect = surface.get_rect(center=theme.screen_center)


def render(screen, answer_content, duration_content, moves_content, state):
    label_content = ""
    if state:
        label_content = "Nasagot mo"
    else:
        label_content = "Nabigo ka"
    label = fonts["modal_label"].render(label_content, False, theme.colors["secondary"])
    label_rect = label.get_rect(topleft=(25, 25))

    answer = fonts["answer"].render(answer_content, False, theme.colors["secondary"])
    answer_rect = answer.get_rect(center=(width / 2, 170))

    duration = fonts["body_title"].render(duration_content, False, theme.colors["secondary"])
    duration_rect = duration.get_rect(center=(110, 390))

    moves = fonts["body_title"].render(moves_content, False, theme.colors["secondary"])
    moves_rect = moves.get_rect(center=(width - 120, 390))

    content_surface.blit(label, label_rect)
    content_surface.blit(answer, answer_rect)
    content_surface.blit(duration, duration_rect)
    content_surface.blit(moves, moves_rect)

    content_surface.blit(close, close_rect)
    content_surface.blit(answer_label, answer_label_rect)
    content_surface.blit(duration_label, duration_label_rect)
    content_surface.blit(moves_label, moves_label_rect)
    content_surface.blit(squiggle, squiggle_rect)

    pygame.draw.rect(content_surface, theme.colors["primary"], button_reset_rect)
    content_surface.blit(button_reset, (button_reset_rect.centerx - button_reset.get_width() // 2,
                                        button_reset_rect.centery - button_reset.get_height() // 2))

    surface.blit(content_surface, content_rect)

    screen.blit(surface, rect)


def clear(screen):
    content_surface.fill(theme.colors["base"])
    surface.blit(content_surface, content_rect)
    screen.blit(surface, rect)
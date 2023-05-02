import pygame

from assets import theme as theme

fonts = theme.fonts('assets/fonts/')

width = 550
height = 180

close = pygame.image.load('assets/images/close.png')
close_rect = close.get_rect(topright=(width - 25, 30))

content_surface = pygame.Surface((width, height))
content_surface.fill(theme.colors["base"])
content_rect = content_surface.get_rect(center=theme.screen_center)

surface = pygame.Surface(theme.screen_size, pygame.SRCALPHA)
surface.fill(theme.colors["modal_base"])

rect = surface.get_rect(center=theme.screen_center)


def render(screen, modal_label, modal_content):
    label = fonts["modal_label"].render(modal_label, False, theme.colors["secondary"])
    label_rect = label.get_rect(topleft=(25, 25))

    message = fonts["modal_paragraph"].render(modal_content, False, theme.colors["secondary"])
    message_rect = message.get_rect(center=(width / 2, height / 2 + 25))

    content_surface.blit(label, label_rect)
    content_surface.blit(close, close_rect)
    content_surface.blit(message, message_rect)

    surface.blit(content_surface, content_rect)

    screen.blit(surface, rect)


def clear(screen):
    content_surface.fill(theme.colors["base"])
    surface.blit(content_surface, content_rect)
    screen.blit(surface, rect)
import pygame

from assets import theme as theme

fonts = theme.fonts('assets/fonts/')

width = 450
height = 500

box_1 = pygame.Surface((50, 50))
box_1.fill(theme.colors["white"])
box_1_rect = box_1.get_rect(center=(50, 50))

box_2 = pygame.Surface((50, 50))
box_2.fill(theme.colors["primary"])
box_2_rect = box_2.get_rect(center=(115, 50))

box_3 = pygame.Surface((50, 50))
box_3.fill(theme.colors["white"])
box_3_rect = box_3.get_rect(center=(180, 50))

box_4 = pygame.Surface((50, 50))
box_4.fill(theme.colors["white"])
box_4_rect = box_4.get_rect(center=(245, 50))

box_5 = pygame.Surface((50, 50))
box_5.fill(theme.colors["white"])
box_5_rect = box_5.get_rect(center=(310, 50))

content_surface = pygame.Surface((width, height))
content_surface.fill(theme.colors["base"])
content_rect = content_surface.get_rect(center=theme.screen_center)

content_surface.blit(box_1, box_1_rect)
content_surface.blit(box_2, box_2_rect)
content_surface.blit(box_3, box_3_rect)
content_surface.blit(box_4, box_4_rect)
content_surface.blit(box_5, box_5_rect)

surface = pygame.Surface(theme.screen_size, pygame.SRCALPHA)
surface.fill(theme.colors["modal_base"])
rect = surface.get_rect(center=theme.screen_center)

surface.blit(content_surface, content_rect)

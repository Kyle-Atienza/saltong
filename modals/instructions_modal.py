import pygame

from assets import theme as theme

fonts = theme.fonts('assets/fonts/')

width = 466
height = 640

close = pygame.image.load('assets/images/close.png')
close_rect = close.get_rect(topright=(width-25,30))

label = fonts["modal_label"].render("Paano Laruin", False, theme.colors["secondary"])
label_rect = label.get_rect(topleft=(25, 25))

content_1 = fonts["modal_paragraph"].render("Hulaan ang SALTONG sa loob ng 6 na tira.", False, theme.colors["secondary"])
content_1_rect = content_1.get_rect(topleft=(25, 75))

content_2 = fonts["modal_paragraph"].render("Ang bawat hulang salita ay dapat 5 letra ang haba.", False, theme.colors["secondary"])
content_2_rect = content_2.get_rect(topleft=(25, 110))

content_3 = fonts["modal_paragraph"].render("Pindutin ang Enter button para i-submit.", False, theme.colors["secondary"])
content_3_rect = content_3.get_rect(topleft=(25, 130))

content_4 = fonts["modal_paragraph"].render("Pagkatapos ng bawat tira, mag-iiba ang kulay ng ", False, theme.colors["secondary"])
content_4_rect = content_4.get_rect(topleft=(25, 165))

content_5 = fonts["modal_paragraph"].render("mga tiles na nagpapakita kung gaano kalapit ang hula", False, theme.colors["secondary"])
content_5_rect = content_5.get_rect(topleft=(25, 185))

content_6 = fonts["modal_paragraph"].render("mo sa tamang sagot.", False, theme.colors["secondary"])
content_6_rect = content_6.get_rect(topleft=(25, 205))

squiggle = pygame.transform.rotate(pygame.image.load('assets/images/wavy.png'), 90)
squiggle_rect = squiggle.get_rect(topright=(290,260))

example_title = fonts["modal_section_title"].render("Mga Halimbawa", False, theme.colors["secondary"])
example_title_rect = example_title.get_rect(topleft=(25, 290))

content_surface = pygame.Surface((width, height))
content_surface.fill(theme.colors["base"])
content_rect = content_surface.get_rect(center=theme.screen_center)

content_surface.blit(close, close_rect)
content_surface.blit(label, label_rect)
content_surface.blit(content_1, content_1_rect)
content_surface.blit(content_2, content_2_rect)
content_surface.blit(content_3, content_3_rect)
content_surface.blit(content_4, content_4_rect)
content_surface.blit(content_5, content_5_rect)
content_surface.blit(content_6, content_6_rect)
content_surface.blit(squiggle, squiggle_rect)
content_surface.blit(example_title, example_title_rect)

surface = pygame.Surface(theme.screen_size, pygame.SRCALPHA)
surface.fill(theme.colors["modal_base"])
rect = surface.get_rect(center=theme.screen_center)

surface.blit(content_surface, content_rect)

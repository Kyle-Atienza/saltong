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

example_1_box_1 = pygame.Surface((50, 50))
example_1_box_1.fill(theme.colors["gray"])
example_1_box_1_rect = example_1_box_1.get_rect(center=(50, 355))

example_1_box_2 = pygame.Surface((50, 50))
example_1_box_2.fill(theme.colors["gray"])
example_1_box_2_rect = example_1_box_2.get_rect(center=(115, 355))

example_1_box_3 = pygame.Surface((50, 50))
example_1_box_3.fill(theme.colors["gray"])
example_1_box_3_rect = example_1_box_3.get_rect(center=(180, 355))

example_1_box_4 = pygame.Surface((50, 50))
example_1_box_4.fill(theme.colors["success"])
example_1_box_4_rect = example_1_box_4.get_rect(center=(245, 355))

example_1_box_5 = pygame.Surface((50, 50))
example_1_box_5.fill(theme.colors["gray"])
example_1_box_5_rect = example_1_box_5.get_rect(center=(310, 355))

example_description1 = fonts["modal_paragraph"].render("Ang letra ay nasa salita at nasa tamang pwesto.", False, theme.colors["secondary"])
example_description1_rect = example_description1.get_rect(topleft=(25, 385))

example_2_box_1 = pygame.Surface((50, 50))
example_2_box_1.fill(theme.colors["gray"])
example_2_box_1_rect = example_2_box_1.get_rect(center=(50, 455))

example_2_box_2 = pygame.Surface((50, 50))
example_2_box_2.fill(theme.colors["primary"])
example_2_box_2_rect = example_2_box_2.get_rect(center=(115, 455))

example_2_box_3 = pygame.Surface((50, 50))
example_2_box_3.fill(theme.colors["gray"])
example_2_box_3_rect = example_2_box_3.get_rect(center=(180, 455))

example_2_box_4 = pygame.Surface((50, 50))
example_2_box_4.fill(theme.colors["gray"])
example_2_box_4_rect = example_2_box_4.get_rect(center=(245, 455))

example_2_box_5 = pygame.Surface((50, 50))
example_2_box_5.fill(theme.colors["gray"])
example_2_box_5_rect = example_2_box_5.get_rect(center=(310, 455))

example_description2 = fonts["modal_paragraph"].render("Ang letra ay nasa salita ngunit mali ang pwesto.", False, theme.colors["secondary"])
example_description2_rect = example_description2.get_rect(topleft=(25, 485))

example_3_box_1 = pygame.Surface((50, 50))
example_3_box_1.fill(theme.colors["gray"])
example_3_box_1_rect = example_3_box_1.get_rect(center=(50, 555))

example_3_box_2 = pygame.Surface((50, 50))
example_3_box_2.fill(theme.colors["gray"])
example_3_box_2_rect = example_3_box_2.get_rect(center=(115, 555))

example_3_box_3 = pygame.Surface((50, 50))
example_3_box_3.fill(theme.colors["gray"])
example_3_box_3_rect = example_3_box_3.get_rect(center=(180, 555))

example_3_box_4 = pygame.Surface((50, 50))
example_3_box_4.fill(theme.colors["gray"])
example_3_box_4_rect = example_3_box_4.get_rect(center=(245, 555))

example_3_box_5 = pygame.Surface((50, 50))
example_3_box_5.fill(theme.colors["gray"])
example_3_box_5_rect = example_3_box_5.get_rect(center=(310, 555))

example_description3 = fonts["modal_paragraph"].render("Wala ang letra sa salita. ", False, theme.colors["secondary"])
example_description3_rect = example_description3.get_rect(topleft=(25, 585))

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

content_surface.blit(example_1_box_1, example_1_box_1_rect)
content_surface.blit(example_1_box_2, example_1_box_2_rect)
content_surface.blit(example_1_box_3, example_1_box_3_rect)
content_surface.blit(example_1_box_4, example_1_box_4_rect)
content_surface.blit(example_1_box_5, example_1_box_5_rect)
content_surface.blit(example_description1, example_description1_rect)

content_surface.blit(example_2_box_1, example_2_box_1_rect)
content_surface.blit(example_2_box_2, example_2_box_2_rect)
content_surface.blit(example_2_box_3, example_2_box_3_rect)
content_surface.blit(example_2_box_4, example_2_box_4_rect)
content_surface.blit(example_2_box_5, example_2_box_5_rect)
content_surface.blit(example_description2, example_description2_rect)

content_surface.blit(example_3_box_1, example_3_box_1_rect)
content_surface.blit(example_3_box_2, example_3_box_2_rect)
content_surface.blit(example_3_box_3, example_3_box_3_rect)
content_surface.blit(example_3_box_4, example_3_box_4_rect)
content_surface.blit(example_3_box_5, example_3_box_5_rect)
content_surface.blit(example_description3, example_description3_rect)

surface = pygame.Surface(theme.screen_size, pygame.SRCALPHA)
surface.fill(theme.colors["modal_base"])
rect = surface.get_rect(center=theme.screen_center)

surface.blit(content_surface, content_rect)

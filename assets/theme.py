import pygame.font

screen_horizontal = 1024
screen_vertical = 728
screen_size = (screen_horizontal, screen_vertical)

screen_center = (screen_horizontal / 2, screen_vertical / 2)

colors = {
    "primary": "#FAC859",
    "secondary": "#271008",
    "base": "#E9DECA",
    "success": "#70E500",

    "blue": "#62B3ED",
    "white": "#FFFFFF",
    "gray": "#A0AEC0",
    
    "modal_base": (39, 16, 8, 102)
}


def fonts(directory):
    return {
        "game_title": pygame.font.Font(directory + 'Cubao_Free_Wide.otf', 100),
        "characters": pygame.font.Font(directory + 'Cubao_Free_Narrow.otf', 36),
        "modal_label": pygame.font.Font(directory + 'Cubao_Free_Regular.otf', 33),
        "modal_paragraph": pygame.font.Font(directory + 'DMSans-Bold.ttf', 16),
        "answer": pygame.font.Font(directory + 'Cubao_Free_Regular.otf', 78),
        "button_label": pygame.font.Font(directory + 'DMSans-Regular.ttf', 16),
        "start_screen_title": pygame.font.Font(directory + 'Cubao_Free_Wide.otf', 125),
        "start_screen_button": pygame.font.Font(directory + 'Cubao_Free_Narrow.otf', 74),

        "body_title": pygame.font.Font(directory + 'Cubao_Free_Regular.otf', 50),
    }
import pygame
import json
import webbrowser

from random import choice
from sys import exit

from assets import theme as theme

pygame.init()
import grid
import keyboard
import modal
from modals import finished_modal, message_modal

# Open the JSON file with list of 5-letter words
with open('data/words.json', 'r') as f:
    # Load the JSON data from the file
    words = json.load(f)

screen = pygame.display.set_mode(theme.screen_size)
pygame.display.set_caption("Saltong")

fonts = theme.fonts('assets/fonts/')

clock = pygame.time.Clock()
word = choice(words["data"])
time = {
    "start": pygame.time.get_ticks(),
    "minutes": 0,
    "seconds": 0,
    "mm:ss": ""
}
message = {
    "show": False,
    "label": "",
    "content": ""
}
finish = {
    "show": False,
    "success": False
}

grid.set_active_row()

while True:
    # Get the position of the mouse cursor
    mouse_pos = pygame.mouse.get_pos()
    # Create a rect representing the mouse cursor
    mouse_rect = pygame.Rect(mouse_pos, (1, 1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if message["show"]:
                    close_message_rect = message_modal.content_rect.move(message_modal.close_rect.topleft)
                    if close_message_rect.collidepoint(event.pos):
                        message["show"] = False
                        message_modal.clear(screen)

                if finish["show"]:
                    try_again_rect = finished_modal.content_rect.move(finished_modal.button_reset_rect.topleft)
                    if try_again_rect.collidepoint(event.pos):
                        finish["show"] = False
                        finished_modal.clear(screen)
                        # reset
                        grid.reset()
                        grid.current_row = 0
                        grid.current_col = 0
                        grid.set_active_row()

                    meaning_rect = finished_modal.content_rect.move(finished_modal.close_rect.topleft)
                    if meaning_rect.collidepoint(event.pos):
                        url = "https://tagalog.pinoydictionary.com/word/" + word + "/"
                        webbrowser.open_new_tab(url)

        if event.type == pygame.KEYDOWN and not message["show"]:
            # temp change row

            if event.key == pygame.K_RETURN:
                if grid.get_row_word() == word:
                    finish["show"] = True
                    finish["success"] = True

                if not grid.get_row_word() in words["data"]:
                    message["label"] = "May Mali"
                    message["content"] = "Hindi nakalagay ang salitang ito sa aming database"
                    message["show"] = True

                if len(grid.get_row_word()) != grid.rows_count:
                    message["label"] = "May Mali"
                    message["content"] = "Kulang ng letra ang iyong salitang nailagay"
                    message["show"] = True

                # if word is already placed within the grid
                if grid.get_row_word() in grid.get_words():
                    message["label"] = "May Mali"
                    message["content"] = "Nagamit mo na ang salitang ito, sumubok ng ibang salita"
                    message["show"] = True

                if grid.current_row + 1 == grid.rows_count and not message["show"]:
                    finish["show"] = True
                    finish["success"] = False

                if len(grid.get_row_word()) == grid.rows_count and grid.get_row_word() in words["data"] and not grid.get_row_word() in grid.get_words():
                    for letter_index, letter in enumerate(word):
                        current_box = grid.group.sprites()[letter_index + (grid.current_row * grid.rows_count)]

                        if current_box.get_character().lower() == letter:
                            current_box.set_status("true")
                        elif current_box.get_character().lower() in word:
                            current_box.set_status("maybe")
                        else:
                            current_box.set_status("false")

                    grid.current_row += 1
                    grid.current_col = 0
                    grid.set_active_row()

            # backspace
            if event.key == pygame.K_BACKSPACE and grid.current_col > 0:
                grid.group.sprites()[(grid.current_row * grid.rows_count) + grid.current_col - 1].update("")
                grid.current_col -= 1

            # on type letters
            if grid.current_col < grid.cols_count and event.unicode.isalpha():
                grid.group.sprites()[(grid.current_row * grid.rows_count) + grid.current_col].update(str(event.unicode))
                grid.current_col += 1

    # grid
    grid.group.draw(grid.group_surface)
    screen.blit(grid.group_surface, grid.group_surface_rect)

    # keyboard
    for index, keyboard_row in enumerate(keyboard.rows):
        keyboard_row_rect = keyboard_row["surface"].get_rect(center=(keyboard.width / 2, keyboard_row["y"]))
        keyboard.group.draw(keyboard_row["surface"])
        keyboard.surface.blit(keyboard_row["surface"], keyboard_row_rect)
    screen.blit(keyboard.surface, keyboard.surface_rect)

    if message["show"]:
        message_modal.render(screen, message["label"], message["content"])

    if finish["show"]:
        finished_modal.render(screen, word, time["mm:ss"], str(grid.current_row), finish["success"])
    else:
        elapsed_time = (pygame.time.get_ticks() - time["start"]) // 1000  # in seconds
        time["minutes"] = elapsed_time // 60
        time["seconds"] = elapsed_time % 60
        time["mm:ss"] = f"{time['minutes']:02}:{time['seconds']:02}"

    pygame.display.update()

    clock.tick(60)

    screen.fill(theme.colors["base"])


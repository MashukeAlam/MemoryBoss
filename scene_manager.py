import constants

class Scene:

    def draw_game_screen(self, pg, win, constants):
        pg.draw.rect(win, constants.RED, constants.RECT_POS_1ST + constants.RECT_DIM)
        pg.draw.rect(win, constants.GREEN, constants.RECT_POS_2ND + constants.RECT_DIM)
        pg.draw.rect(win, constants.BLUE, constants.RECT_POS_3RD + constants.RECT_DIM)
        pg.draw.rect(win, constants.YELLOW, constants.RECT_POS_4TH + constants.RECT_DIM)

    def draw_question_screen(self, pg, win, color_list):

        win.fill(constants.BLACK)
        curr_height = 10
        font = pg.font.Font(pg.font.get_default_font(), constants.FONT_SIZE)
        text = font.render("REMEMBER THIS SEQUENCE...", True, (255, 255, 255), (0, 0, 0))
        win.blit(text, dest=(20, curr_height))
        curr_height += 70

        for i in range(0, len(color_list)):

            text = font.render(str(i + 1) + ": " + color_list[i], True, constants.WHITE, constants.BLACK)
            win.blit(text, dest=(0, curr_height))
            curr_height += 50

        font = pg.font.Font(pg.font.get_default_font(), constants.SMALL_FONT_SIZE)

        text = font.render(constants.INST_1, True, constants.WHITE, constants.BLACK)
        win.blit(text, dest=(30, curr_height))
        text = font.render(constants.INST, True, constants.WHITE, constants.BLACK)
        win.blit(text, dest=(30, curr_height+50))

    def draw_game_over(self, pg, win, res):
        verdict = ""
        if res == "WIN":
            verdict = "You Win!"
            color = constants.GREEN
        elif res == "LOST":
            verdict = "Better luck next time!"
            color = constants.RED


        win.fill(color)
        font = pg.font.Font(pg.font.get_default_font(), constants.FONT_SIZE)
        text = font.render(verdict, True, constants.WHITE, constants.BLACK)
        win.blit(text, dest=(constants.RECT_WIDTH - constants.RECT_WIDTH // 2, 100))
        font = pg.font.Font(pg.font.get_default_font(), constants.SMALL_FONT_SIZE)

        text = font.render(constants.INST, True, constants.WHITE, constants.BLACK)
        win.blit(text, dest=(20, 500))



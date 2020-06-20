from pygame_env_inittialize import GameEngineInit
from scene_manager import Scene
import constants
import math
import random

RUN = True
LEVEL = 3
g = GameEngineInit(constants.SIZE, constants.TITLE)
scene = Scene()

pg, win = g.return_obj()

# print(pg,win)


curr_mode = "ques"

def make_a_sequence():
    global LEVEL
    color_list = []
    for i in range(0, LEVEL):
        color_list.append(constants.COLORS[random.randint(0, 3)])

    if LEVEL < 8:
        LEVEL += 1
    return color_list

c_l = make_a_sequence()
inputted = []
while RUN:

    pg.time.delay(constants.TIME_DELAY)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            print(constants.END_MSG)
            RUN = False

        keys = pg.key.get_pressed()

        if curr_mode == "ques" and keys[pg.K_SPACE]:
            curr_mode = "game"

        if curr_mode == "game_over" and keys[pg.K_SPACE]:
            c_l = make_a_sequence()
            curr_mode = "ques"


        if curr_mode == "game" and event.type == pg.MOUSEBUTTONUP :
            pos = pg.mouse.get_pos()
            x = math.floor(pos[0]/constants.RECT_WIDTH)
            y = math.floor(pos[1]/constants.RECT_HEIGHT)

            clicked_col = constants.COLOR_MAP[(x, y)]
            print(clicked_col)
            if c_l[0][0] == clicked_col:
                print("DONE!")
                c_l.pop(0)

                if len(c_l) == 0:
                    curr_mode = "game_over"
                    latest_res = "WIN"
            else:
                print("OHHO!")
                curr_mode = "game_over"
                latest_res = "LOST"



        if curr_mode == "ques":
            scene.draw_question_screen(pg, win, c_l)
        elif curr_mode == "game":
            scene.draw_game_screen(pg, win, constants)
        elif curr_mode == "game_over":
            scene.draw_game_over(pg, win, latest_res)
        pg.display.update()

pg.quit()
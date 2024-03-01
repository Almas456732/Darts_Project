from ursina import *

global speed
global hold


class Dart(Entity):
    global hold

    def __init__(self):
        super().__init__(
            model='dart.obj',
            color=color.red,
            scale=(1.5, 1.5, 1.5),
            texture="photo_5375316730072651008_y.jpg",
            collider="mesh"
        )
        Entity(model='sphere', scale=1000, texture='SKY.jpg', double_sided=True)  # sky
        self.delta_y = 0
        self.y = 0
        self.x = 0

        self.rotation_y = -90
        self.rotation_z = -5
        self.start_drag_position = (0, 0)

        self.position = (0, -5, 0)

    def update(self):

        if hold:
            if held_keys['left mouse']:
                if not self.start_drag_position:
                    self.start_drag_position = (mouse.x, mouse.y)

                delta_x = mouse.x - self.start_drag_position[0]
                delta_y = mouse.y - self.start_drag_position[1]
                print(f'delta_y: {delta_y}')
                self.x += delta_x * 6
                self.y += delta_y * 6
                self.delta_y = delta_y
                self.start_drag_position = (mouse.x, mouse.y)

            elif not held_keys['left mouse'] and self.delta_y >= 0.008:
                self.throw_object()



            else:
                self.start_drag_position = None



    def throw_object(self):
        global speed,k,overall_your

        y = (self.y * 1.0500 + 0.0005) * speed
        z = ((y ** 2) * 70) * speed

        forward_vector = Vec3(0, y, z).normalized()
        self.position += forward_vector * speed



class Dartboard(Entity):
    global score, text, k

    def __init__(self):
        super().__init__(
        )

        self.zone1 = Entity(model="circle", scale=2, position=(0, 5, 47.99), color=color.rgb(143, 22, 48),
                            collider="box")
        self.zone2 = Entity(model="circle", scale=4, position=(0, 5, 48), color=color.green, collider="box")
        self.zone3 = Entity(model="circle", scale=6, position=(0, 5, 48.1), color=color.blue, collider="box")
        self.zone4 = Entity(model="circle", scale=8, position=(0, 5, 48.2), color=color.red, collider="box")
        self.zone5 = Entity(model="circle", scale=10, position=(0, 5, 48.3), color=color.green, collider="box")
        self.zone6 = Entity(model="circle", scale=12, position=(0, 5, 48.4), color=color.blue, collider="box")
        self.zone7 = Entity(model="circle", scale=14, position=(0, 5, 48.5), color=color.red, collider="box")
        self.zone8 = Entity(model="circle", scale=30, position=(0, 5, 48.6), visible=False, collider="box")


        self.hit = True

        self.text_your = Text(
            text=f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}",
            position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
            background=True, enabled=False)
        self.text_teacher = Text(
            text=f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}",
            position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=False)

    def update(self):
        global speed
        global hold
        global score, text_your, text_teacher, score1_your, score2_your, score3_your, k, overall_your, \
            score1_teacher, score2_teacher, score3_teacher, overall_teacher, score_teacher, go_to_menu

        hit_info1 = Dart.intersects(self.zone1)
        if hit_info1.hit and self.hit:
            sound.play()
            k += 1
            speed = 0
            hold = False
            score += 10
            text_your.y = 1
            text_teacher.y = 1
            score_teacher = (random.randint(4, 10))
            if k == 1:
                score1_your = score1_your + score
                score1_teacher = score1_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 2:
                score2_your = score2_your + score
                score2_teacher = score2_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 3:
                score3_your = score3_your + score
                score3_teacher = score3_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            self.text_your.enabled = False
            self.text_teacher.enabled = False
            self.text_your = Text(
                text=f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}",
                position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
                background=True, enabled=True)
            self.text_teacher = Text(
                text=f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}",
                position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=True)
            if k == 3 and score3_your != 0 and overall_your>overall_teacher:
                win()
            if k == 3 and score3_your != 0 and overall_your<overall_teacher:
                lose()
            if k == 3 and score3_your != 0 and overall_your==overall_teacher:
                draw()
            self.hit = False
        hit_info2 = Dart.intersects(self.zone2)
        if hit_info2.hit and self.hit:
            sound.play()
            k += 1
            speed = 0
            hold = False
            score += 9
            text_your.y = 1
            text_teacher.y = 1
            score_teacher = (random.randint(4, 10))
            if k == 1:
                score1_your = score1_your + score
                score1_teacher = score1_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 2:
                score2_your = score2_your + score
                score2_teacher = score2_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 3:
                score3_your = score3_your + score
                score3_teacher = score3_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            self.text_your.enabled = False
            self.text_teacher.enabled = False
            self.text_your = Text(
                text=f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}",
                position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
                background=True, enabled=True)
            self.text_teacher = Text(
                text=f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}",
                position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=True)
            if k == 3 and score3_your != 0 and overall_your>overall_teacher:
                win()
            if k == 3 and score3_your != 0 and overall_your<overall_teacher:
                lose()
            if k == 3 and score3_your != 0 and overall_your==overall_teacher:
                draw()
            self.hit = False
        hit_info3 = Dart.intersects(self.zone3)
        if hit_info3.hit and self.hit:
            sound.play()
            k += 1
            speed = 0
            hold = False
            score += 8
            text_your.y = 1
            text_teacher.y = 1
            score_teacher = (random.randint(4, 10))
            if k == 1:
                score1_your = score1_your + score
                score1_teacher = score1_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 2:
                score2_your = score2_your + score
                score2_teacher = score2_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 3:
                score3_your = score3_your + score
                score3_teacher = score3_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            self.text_your.enabled = False
            self.text_teacher.enabled = False
            self.text_your = Text(
                text=f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}",
                position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
                background=True, enabled=True)
            self.text_teacher = Text(
                text=f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}",
                position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=True)
            if k == 3 and score3_your != 0 and overall_your>overall_teacher:
                win()
            if k == 3 and score3_your != 0 and overall_your<overall_teacher:
                lose()
            if k == 3 and score3_your != 0 and overall_your==overall_teacher:
                draw()
            self.hit = False
        hit_info4 = Dart.intersects(self.zone4)
        if hit_info4.hit and self.hit:
            sound.play()
            k += 1
            speed = 0
            hold = False
            score += 7
            text_your.y = 1
            text_teacher.y = 1
            score_teacher = (random.randint(4, 10))
            if k == 1:
                score1_your = score1_your + score
                score1_teacher = score1_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 2:
                score2_your = score2_your + score
                score2_teacher = score2_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 3:
                score3_your = score3_your + score
                score3_teacher = score3_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            self.text_your.enabled = False
            self.text_teacher.enabled = False
            self.text_your = Text(
                text=f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}",
                position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
                background=True, enabled=True)
            self.text_teacher = Text(
                text=f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}",
                position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=True)
            if k == 3 and score3_your != 0 and overall_your>overall_teacher:
                win()
            if k == 3 and score3_your != 0 and overall_your<overall_teacher:
                lose()
            if k == 3 and score3_your != 0 and overall_your==overall_teacher:
                draw()
            self.hit = False
        hit_info5 = Dart.intersects(self.zone5)
        if hit_info5.hit and self.hit:
            sound.play()
            k += 1
            speed = 0
            hold = False
            score += 6
            text_your.y = 1
            text_teacher.y = 1
            score_teacher = (random.randint(4, 10))
            if k == 1:
                score1_your = score1_your + score
                score1_teacher = score1_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 2:
                score2_your = score2_your + score
                score2_teacher = score2_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 3:
                score3_your = score3_your + score
                score3_teacher = score3_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            self.text_your.enabled = False
            self.text_teacher.enabled = False
            self.text_your = Text(
                text=f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}",
                position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
                background=True, enabled=True)
            self.text_teacher = Text(
                text=f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}",
                position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=True)
            if k == 3 and score3_your != 0 and overall_your>overall_teacher:
                win()
            if k == 3 and score3_your != 0 and overall_your<overall_teacher:
                lose()
            if k == 3 and score3_your != 0 and overall_your==overall_teacher:
                draw()
            self.hit = False
        hit_info6 = Dart.intersects(self.zone6)
        if hit_info6.hit and self.hit:
            sound.play()
            k += 1
            speed = 0
            hold = False
            score += 5
            text_your.y = 1
            text_teacher.y = 1
            score_teacher = (random.randint(4, 10))
            if k == 1:
                score1_your = score1_your + score
                score1_teacher = score1_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 2:
                score2_your = score2_your + score
                score2_teacher = score2_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 3:
                score3_your = score3_your + score
                score3_teacher = score3_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            self.text_your.enabled = False
            self.text_teacher.enabled = False
            self.text_your = Text(
                text=f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}",
                position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
                background=True, enabled=True)
            self.text_teacher = Text(
                text=f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}",
                position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=True)
            if k == 3 and score3_your != 0 and overall_your>overall_teacher:
                win()
            if k == 3 and score3_your != 0 and overall_your<overall_teacher:
                lose()
            if k == 3 and score3_your != 0 and overall_your==overall_teacher:
                draw()
            self.hit = False
        hit_info7 = Dart.intersects(self.zone7)
        if hit_info7.hit and self.hit:
            sound.play()
            k += 1
            speed = 0
            hold = False
            score += 4
            text_your.y = 1
            text_teacher.y = 1
            score_teacher = (random.randint(4, 10))
            if k == 1:
                score1_your = score1_your + score
                score1_teacher = score1_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 2:
                score2_your = score2_your + score
                score2_teacher = score2_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 3:
                score3_your = score3_your + score
                score3_teacher = score3_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            self.text_your.enabled = False
            self.text_teacher.enabled = False
            self.text_your = Text(
                text=f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}",
                position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
                background=True, enabled=True)
            self.text_teacher = Text(
                text=f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}",
                position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=True)
            if k == 3 and score3_your != 0 and overall_your > overall_teacher:
                win()
            if k == 3 and score3_your != 0 and overall_your < overall_teacher:
                lose()
            if k == 3 and score3_your != 0 and overall_your == overall_teacher:
                draw()
            self.hit = False
        hit_info8 = Dart.intersects(self.zone8)
        if hit_info8.hit and self.hit:
            k += 1
            score += 0
            text_your.y = 1
            text_teacher.y = 1
            score_teacher = (random.randint(4, 10))
            if k == 1:
                score1_your = score1_your + score
                score1_teacher = score1_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 2:
                score2_your = score2_your + score
                score2_teacher = score2_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            elif k == 3:
                score3_your = score3_your + score
                score3_teacher = score3_teacher + score_teacher
                overall_your += score
                overall_teacher += score_teacher
            self.text_your.enabled = False
            self.text_teacher.enabled = False
            self.text_your = Text(
                text=f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}",
                position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
                background=True, enabled=True)
            self.text_teacher = Text(
                text=f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}",
                position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=True)
            if k == 3 and score3_your != 1 and overall_your > overall_teacher:
                win()
            if k == 3 and score3_your != 1 and overall_your < overall_teacher:
                lose()
            if k == 3 and score3_your != 1 and overall_your == overall_teacher:
                draw()
            self.hit = False


def restart():
    global score1_your, score2_your, score3_your, hold, speed, k, score, overall_your, score1_teacher, score2_teacher, score3_teacher, overall_teacher, score_teacher
    score = 0
    score_teacher = 0
    dart.position = (0, -5, 0)
    dart.start_drag_position = None
    if k == 1:
        text_your.text = f"Overall your Points: {overall_your}\n First try: {score1_your}\n Second try: {score2_your}\n Third try:{score3_your}"
        text_teacher.text = f"Overall teacher points: {overall_teacher}\n First try: {score1_teacher}\n Second try: {score2_teacher}\n Third try: {score3_teacher}"
    elif k == 2:

        text_your.text = f"Overall your Points: {overall_your}\n First try: {score2_your}\n Second try: {score2_your}\n Third try: {score2_your}"
        text_teacher.text = f"Overall teacher points: {overall_teacher}\n First try: {score1_teacher}\n Second try: {score2_teacher}\n Third try: {score3_teacher}"
    elif k == 3:

        text_your.text = f"Overall your Points:{overall_your}\n First try:{score1_your}\n Second try:{score2_your}\n Third try:{score3_your}"
        text_teacher.text = f"Overall teacher points:{overall_teacher}\n First try:{score1_teacher}\n Second try:{score2_teacher}\n Third try:{score3_teacher}"
    hold = True
    speed = 3
    dartboard.hit = True


def p1():
    global dart, dartboard, score1_your, score2_your, score3_your, hold, speed, k, score, \
        overall_your, score1_teacher, score2_teacher, score3_teacher, overall_teacher, score_teacher

    dartboard.text_your = Text(
        text=f"Overall your Points: {overall_your}\n First try: {score1_your}\n Second try: {score2_your}\n Third try: {score3_your}",
        position=(-.5, -.35), origin=(0, 0), scale=(2), color=color.pink,
        background=True, enabled=True)
    dartboard.text_teacher = Text(
        text=f"Overall teacher points: {overall_teacher}\n First try: {score1_teacher}\n Second try:{score2_teacher}\n Third try: {score3_teacher}",
        position=(.25, -.25), scale=(2), color=color.pink, background=True, enabled=True)

    camera.position = (0, 0, -20)
    button1.enabled = False
    button.enabled = True

    go_to_menu.enabled = True
    go_to_menu.position = (-0.75, 0.45)
    dart.position = (0, -5, 0)

    exit.enabled=False
    setting.enabled=False

def back_to_menu():
    go_to_menu.enabled = False
    global dart, dartboard, score1_your, score2_your, score3_your, hold, speed, k, score, overall_your, score1_teacher, score2_teacher, score3_teacher, overall_teacher, score_teacher
    k = 0
    dart.position = (0, -5, 0)
    score1_your = 0
    score2_your = 0
    score3_your = 0
    score = 0
    overall_your = 0

    overall_teacher = 0
    score1_teacher = 0
    score2_teacher = 0
    score3_teacher = 0
    score_teacher = 0

    dartboard.text_your.enabled = False
    dartboard.text_teacher.enabled = False

    camera.position = (2000, 0, -20)
    button1.enabled = True
    button.enabled = False

    hold = True
    speed = 3
    dartboard.hit = True

    text_win_lose.enabled = False
    exit.enabled=True

    setting.enabled = True
def win ():
    go_to_menu.enabled = True
    go_to_menu.position=(0,-.2,0)
    global text_win_lose,dart, dartboard, score1_your, score2_your, score3_your,\
        hold, speed, k, score, overall_your, score1_teacher, score2_teacher, score3_teacher, overall_teacher, score_teacher
    k = 0

    dartboard.text_your.enabled = False
    dartboard.text_teacher.enabled = False

    camera.position = (-2000, 0, -20)
    button1.enabled = False
    button.enabled = False

    hold = True
    speed = 3
    dartboard.hit = True

    text_win_lose.enabled=True
    text_win_lose.text = f"Overall your points: {overall_your}\n Overall teacher points: {overall_teacher}"
def lose():
    go_to_menu.enabled = True
    go_to_menu.position = (0, -.2, 0)
    global text_win_lose,dart, dartboard, score1_your, score2_your, score3_your, hold, speed, k, score, overall_your, score1_teacher, score2_teacher, score3_teacher, overall_teacher, score_teacher
    k = 0

    dartboard.text_your.enabled = False
    dartboard.text_teacher.enabled = False

    camera.position = (0, 2000, -20)
    button1.enabled = False
    button.enabled = False

    hold = True
    speed = 3
    dartboard.hit = True

    text_win_lose.enabled = True
    text_win_lose.text = f"Overall your points: {overall_your}\n Overall teacher points: {overall_teacher}"
def draw():
    go_to_menu.enabled = True
    go_to_menu.position = (0, -.2, 0)
    global text_win_lose,dart, dartboard, score1_your, score2_your, score3_your, hold,\
        speed, k, score, overall_your, score1_teacher, score2_teacher, score3_teacher, overall_teacher, score_teacher
    k = 0

    dartboard.text_your.enabled = False
    dartboard.text_teacher.enabled = False

    camera.position = (0, -2000, -20)
    button1.enabled = False
    button.enabled = False

    hold = True
    speed = 3
    dartboard.hit = True

    text_win_lose.enabled = True
    text_win_lose.text = f"Overall your points:{overall_your}\n Overall teacher points:{overall_teacher}"
def Setting():
    button1.enabled=False
    exit.enabled=False
    setting.enabled=False
    start_music.enabled=True
    stop_music.enabled=True
    back.enabled=True
def Back():
    button1.enabled = True
    exit.enabled = True
    setting.enabled = True
    start_music.enabled = False
    stop_music.enabled = False
    back.enabled = False
def start_m():
    global music_
    music_.play()
def stop_m():
    global music_
    music_.stop()
app = Ursina()

# background
Entity(model='cube', scale=(15, 8), texture="Menu_background.jpg", double_sided=True, position=(2000, 0, 0),
       color="black")

button1 = Button(text="Start", scale=(.3, .1), position=(0, .2))
button1.on_click = p1
Single_game = False
camera.position = (2000, 0, -20)

go_to_menu = Button(text="Menu", position=(-0.75, 0.45), scale=(.3, .1))
go_to_menu.on_click = back_to_menu
go_to_menu.enabled = False
#win
Entity(model='cube', scale=(15, 8), texture="images.png", double_sided=True, position=(-2000, 0, 0), color="black")
#lose
Entity(model='cube', scale=(15, 8), texture="Game_over.jpg", double_sided=True, position=(0, 2000, 0), color="black")
#draw
Entity(model='cube', scale=(15, 8), texture="draw.png", double_sided=True, position=(0, -2000, 0), color="black")


k = 0

dart = Dart()
EditorCamera()
score1_your = 0
score2_your = 0
score3_your = 0
score = 0
overall_your = 0


overall_teacher = 0
score1_teacher = 0
score2_teacher = 0
score3_teacher = 0
score_teacher = 0

dartboard = Dartboard()

button = Button(text="Return dart", position=(0.75, 0.45), scale=(.3, .1))
button.on_click = restart
button.enabled = False

text_your = Text(
    text=f"Overall your points: {overall_your}\n First try: {score1_your}\n Second try: {score2_your}\n Third try: {score3_your}",
    position=(-.5, -.35), scale=(2), color=color.pink, background=True, enabled=False, origin=(0, 0))
text_teacher = Text(
    text=f"Overall teacher points: {overall_teacher}\n First try: {score1_teacher}\n Second try: {score2_teacher}\n Third try: {score3_teacher}",
    position=(.5, -.35), scale=(2), color=color.pink, background=True, enabled=False, )
#text for win lose draw
text_win_lose = Text(
    text=f"Overall your points: {overall_your}\n Overall teacher points: {overall_teacher}",
    position=(-0.1, 0.35), scale=(2), color=color.white, background=True, enabled=False, )
print(camera.position)
speed = 3
hold = True
window.fps_counter.enabled=False
window.fullscreen=True
window.entity_counter.enabled=False
window.collider_counter.enabled=False
window.exit_button.enabled=False
window.cog_button.enabled=False
window.title="Darts"

#exit button
exit = Button(text="Exit",scale=(.3, .1), position=(0, -.2))
exit.on_click=Func(sys.exit)

#music


setting = Button(text="Settings",scale=(.3, .1), position=(0,0),enabled=True)
start_music = Button(text="Music: turn on", scale=(.3, .1),position=(0,.2),enabled=False)

stop_music=Button(text="Music: turn off",scale=(.3, .1),position=(0,0),enabled=False)

back=Button(text="Back",scale=(.3, .1),position=(0,-.2),enabled=False)
setting.on_click=Setting
back.on_click=Back
music_=Audio("perfect-beauty-191271.mp3",loop=True,autoplay=True)
stop_music.on_click=stop_m
start_music.on_click=start_m

#sound
sound=Audio("Dart_Sound.mp3",loop=False,autoplay=False)
app.run()


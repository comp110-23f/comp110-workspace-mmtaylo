"""EX05 - Turtle Project; the Grand Budapest Hotel from my favorite movie, Wes Anderson's The Grand Budapest Hotel."""

__author__ = "730578652"

from turtle import Turtle, done


def draw_one_room_window(a: Turtle, x: float, y: float) -> None:
    """Function to create a hotel room window."""
    a.pencolor("linen")
    a.penup()
    a.goto(x - 2, y - 2)
    a.setheading(0.0)
    a.pendown()
    a.begin_fill()
    a.fillcolor("linen")
    window_idx: int = 0
    while window_idx < 2:
        a.forward(12)
        a.left(90)
        a.forward(28)
        a.left(90)
        window_idx += 1
    window_idx = 0
    a.end_fill()

    a.pencolor("mistyrose3")
    a.pensize(2)
    a.penup()
    a.goto(x - 2, y + 27)
    a.setheading(0.0)
    a.pendown()
    a.forward(12)

    a.pencolor("linen")
    a.penup()
    a.goto(x, y)
    a.setheading(0.0)
    a.pendown()
    a.begin_fill()
    a.fillcolor("rosybrown3")
    while window_idx < 3:
        a.forward(9)
        a.left(90)
        a.forward(18)
        a.left(90)
        window_idx += 1
    window_idx = 0
    a.right(90)
    a.circle(4.5, 180)
    a.end_fill()
    a.hideturtle()


def draw_one_bottom_floor_window(aa: Turtle, x: float, y: float) -> None:
    """Function meant to draw a window on the bottom floor."""
    aa.pencolor("linen")
    aa.penup()
    aa.goto(x - 1, y - 4)
    aa.setheading(0.0)
    aa.pendown()
    aa.begin_fill()
    aa.fillcolor("linen")
    window_idx: int = 0
    while window_idx < 2:
        aa.forward(12)
        aa.left(90)
        aa.forward(23)
        aa.left(90)
        window_idx += 1
    window_idx = 0
    aa.end_fill()

    aa.pencolor("rosybrown")
    aa.penup()
    aa.goto(x, y)
    aa.setheading(0.0)
    aa.pendown()
    aa.begin_fill()
    aa.fillcolor("rosybrown")
    while window_idx < 2:
        aa.forward(10)
        aa.left(90)
        aa.forward(17)
        aa.left(90)
        window_idx += 1
    window_idx = 0
    aa.end_fill()

    aa.pencolor("linen")
    aa.penup()
    aa.goto(x + 5, y)
    aa.setheading(0.0)
    aa.pendown()
    aa.left(90)
    aa.forward(20)

    aa.hideturtle()


def draw_one_white_verti_panel(b: Turtle, length: float, x: float, y: float) -> None:
    """Function meant to draw vertical white panels along edges of hotel."""
    b.pencolor("linen")
    b.pensize(5)
    b.penup()
    b.goto(x, y)
    b.setheading(0.0)
    b.pendown()
    b.right(90)
    b.forward(length)
    b.hideturtle()


def draw_crown_moulding(c: Turtle, length: float, x: float, y: float) -> None:
    """Function meant to draw crown moulding along top edges of hotel."""
    c.pencolor("linen")
    c.pensize(7)
    c.penup()
    c.goto(x, y)
    c.setheading(0.0)
    c.pendown()
    c.forward(length)
    c.hideturtle()


def draw_roof(d: Turtle, length: float, x: float, y: float) -> None:
    """Function meant to draw the hotel roof."""
    d.pencolor("lightskyblue4")
    d.penup()
    d.goto(x, y)
    d.setheading(0.0)
    d.pendown()
    d.begin_fill()
    d.fillcolor("lightskyblue4")
    roof_idx: int = 0
    while roof_idx < 3:
        d.forward(20)
        d.left(120)
        roof_idx += 1
    roof_idx = 0
    d.end_fill()

    d.penup()
    d.goto(x + 10, y + 19)
    d.setheading(0.0)
    d.pendown()
    d.begin_fill()
    d.fillcolor("lightskyblue4")
    while roof_idx < 2:
        d.forward(length)
        d.right(90)
        d.forward(19)
        d.right(90)
        roof_idx += 1
    roof_idx = 0
    d.end_fill()

    d.penup()
    d.goto(x + (20 + length), y)
    d.setheading(0.0)
    d.pendown()
    d.begin_fill()
    d.fillcolor("lightskyblue4")
    while roof_idx < 3:
        d.left(120)
        d.forward(20)
        roof_idx += 1
    roof_idx = 0
    d.end_fill()
    d.hideturtle()


def draw_semicircle_roof(e: Turtle, x: float, y: float) -> None:
    """Function meant to draw a semi-circle roof on the hotel."""
    e.pencolor("lightskyblue4")
    e.penup()
    e.goto(x, y)
    e.setheading(0.0)
    e.pendown()
    e.begin_fill()
    e.fillcolor("lightskyblue4")
    e.left(90)
    e.circle(14, 180)
    e.end_fill()

    e.pencolor("skyblue4")
    e.penup()
    e.goto(x - 14, y + 12)
    e.setheading(0.0)
    e.pendown()
    e.left(90)
    e.forward(22)
    e.hideturtle()


def draw_stairs(f: Turtle, x: float, y: float) -> None:
    """Function meant to draw stairs leading up to the hotel."""
    f.pencolor("cornsilk3")
    f.penup()
    f.goto(x, y)
    f.setheading(0.0)
    if x < 0:
        f.left(180)
    f.pendown()
    f.begin_fill()
    f.fillcolor("cornsilk3")
    stairs_idx: int = 0
    while stairs_idx < 2:
        f.forward(5)
        if x < 0:
            f.left(90)
        else:
            f.right(90)
        stairs_idx += 1
    stairs_idx = 0
    f.end_fill()
    f.hideturtle()


def draw_tree(g: Turtle, x: float, y: float) -> None:
    """Function meant to draw a tree."""
    tree_idx: int = 0

    g.pencolor("gainsboro")
    g.penup()
    g.goto(x - 2, y - 20)
    g.setheading(0.0)
    g.pendown()
    g.begin_fill()
    g.fillcolor("ghostwhite")
    while tree_idx < 3:
        g.forward(45)
        g.left(120)
        tree_idx += 1
    tree_idx = 0
    g.end_fill()

    g.penup()
    g.goto(x, y)
    g.setheading(0.0)
    g.pendown()
    g.begin_fill()
    g.fillcolor("ghostwhite")
    while tree_idx < 3:
        g.forward(40)
        g.left(120)
        tree_idx += 1
    tree_idx = 0
    g.end_fill()

    g.pencolor("wheat4")
    g.penup()
    g.goto(x + 15, y - 35)
    g.setheading(0.0)
    g.pendown()
    g.begin_fill()
    g.fillcolor("wheat4")
    while tree_idx < 2:
        g.forward(10)
        g.left(90)
        g.forward(14)
        g.left(90)
        tree_idx += 1
    tree_idx = 0
    g.end_fill()


def main() -> None:
    """The entrypoint of my scene."""


i: int = 0
iy: int = 0
ix: int = 0

background: Turtle = Turtle()
background.pencolor("slategray2")
background.penup()
background.goto(-650, 375)
background.pendown()
background.begin_fill()
background.fillcolor("slategray2")
while i < 2:
    background.forward(1300)
    background.right(90)
    background.forward(115)
    background.right(90)
    i += 1
i = 0
background.end_fill()
background.hideturtle()


background.pencolor("slategray3")
background.penup()
background.goto(-650, 260)
background.pendown()
background.begin_fill()
background.fillcolor("slategray3")
while i < 4:
    background.forward(1300)
    background.right(90)
    i += 1
i = 0
background.end_fill()
background.hideturtle()

t: Turtle = Turtle()
while i < 23:
    draw_tree(t, -660 + ix, 275 + iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy -= 60
while i < 21:
    draw_tree(t, -630 + ix, 275 + iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy -= 60
while i < 23:
    draw_tree(t, -660 + ix, 275 + iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy -= 60
while i < 21:
    draw_tree(t, -630 + ix, 275 + iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy -= 60
while i < 23:
    draw_tree(t, -660 + ix, 275 + iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy -= 60
while i < 21:
    draw_tree(t, -630 + ix, 275 + iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy = 0


bottom_rec: Turtle = Turtle()
bottom_rec.pencolor("light pink")
bottom_rec.penup()
bottom_rec.goto(-250, -50)
bottom_rec.pendown()
bottom_rec.begin_fill()
bottom_rec.fillcolor("light pink")
while i < 2:
    bottom_rec.forward(515)
    bottom_rec.left(90)
    bottom_rec.forward(75)
    bottom_rec.left(90)
    i += 1
i = 0
bottom_rec.end_fill()
bottom_rec.hideturtle()

top_rec: Turtle = Turtle()
top_rec.pencolor("misty rose")
top_rec.penup()
top_rec.goto(-250, 25)
top_rec.pendown()
top_rec.begin_fill()
top_rec.fillcolor("misty rose")
while i < 2:
    top_rec.forward(515)
    top_rec.left(90)
    top_rec.forward(150)
    top_rec.left(90)
    i += 1
i = 0
top_rec.end_fill()
top_rec.hideturtle()

roof: Turtle = Turtle()
draw_roof(roof, 155, -252, 175)
draw_roof(roof, 155, 93, 175)
draw_roof(roof, 182, -97, 217)

upper_rec: Turtle = Turtle()
upper_rec.pencolor("misty rose")
upper_rec.penup()
upper_rec.goto(-95, 175)
upper_rec.pendown()
upper_rec.begin_fill()
upper_rec.fillcolor("misty rose")
while i < 2:
    upper_rec.forward(198)
    upper_rec.left(90)
    upper_rec.forward(42)
    upper_rec.left(90)
    i += 1
i = 0
upper_rec.end_fill()
upper_rec.hideturtle()

side_recs: Turtle = Turtle()
side_recs.pencolor("mistyrose2")
side_recs.penup()
side_recs.goto(-194, 230)
side_recs.pendown()
side_recs.begin_fill()
side_recs.fillcolor("misty rose")
while i < 2:
    side_recs.right(90)
    side_recs.forward(280)
    side_recs.right(90)
    side_recs.forward(26)
    i += 1
i = 0
side_recs.penup()
side_recs.goto(231, 230)
side_recs.pendown()
while i < 2:
    side_recs.right(90)
    side_recs.forward(280)
    side_recs.right(90)
    side_recs.forward(26)
    i += 1
i = 0
side_recs.end_fill()
side_recs.hideturtle()

bottom_side_recs: Turtle = Turtle()
bottom_side_recs.pencolor("light pink")
bottom_side_recs.penup()
bottom_side_recs.goto(-195, 24)
bottom_side_recs.pendown()
bottom_side_recs.begin_fill()
bottom_side_recs.fillcolor("light pink")
while i < 2:
    bottom_side_recs.right(90)
    bottom_side_recs.forward(73)
    bottom_side_recs.right(90)
    bottom_side_recs.forward(24)
    i += 1
i = 0
bottom_side_recs.penup()
bottom_side_recs.goto(230, 24)
bottom_side_recs.pendown()
while i < 2:
    bottom_side_recs.right(90)
    bottom_side_recs.forward(73)
    bottom_side_recs.right(90)
    bottom_side_recs.forward(24)
    i += 1
i = 0
bottom_side_recs.end_fill()
bottom_side_recs.hideturtle()

door: Turtle = Turtle()
door.pencolor("mistyrose4")
door.penup()
door.goto(-10, -50)
door.setheading(0.0)
door.pendown()
door.begin_fill()
door.fillcolor("rosybrown3")
while i < 2:
    door.forward(26)
    door.left(90)
    door.forward(35)
    door.left(90)
    i += 1
i = 0
door.end_fill()
door.forward(13)
door.left(90)
door.forward(35)
door.hideturtle()

stairs: Turtle = Turtle()  
while i < 10:
    draw_stairs(stairs, -343 - ix, -50 - iy)
    ix += 5
    iy += 5
    i += 1
stairs.pencolor("cornsilk3")
stairs.penup()
stairs.goto(-343 - ix, -50 - iy)
stairs.pendown()
stairs.begin_fill()
stairs.fillcolor("cornsilk3")
stairs.forward(50)
stairs.left(90)
stairs.forward(50)
stairs.end_fill()
stairs.hideturtle()
i = 0
ix = 0
iy = 0

while i < 10: 
    draw_stairs(stairs, 377 + ix, -50 - iy)
    ix += 5
    iy += 5
    i += 1
stairs.pencolor("cornsilk3")
stairs.penup()
stairs.goto(377 + ix, -50 - iy)
stairs.pendown()
stairs.begin_fill()
stairs.fillcolor("cornsilk3")
stairs.right(360)
stairs.forward(50)
stairs.right(90)
stairs.forward(50)
stairs.end_fill()
stairs.hideturtle()
i = 0
ix = 0
iy = 0

walkway: Turtle = Turtle()
walkway.pencolor("linen")
walkway.pensize(4)
walkway.penup()
walkway.goto(-340, -100)
walkway.pendown()
walkway.begin_fill()
walkway.fillcolor("mistyrose")
while i < 2:
    walkway.forward(715)
    walkway.left(90)
    walkway.forward(50)
    walkway.left(90)
    i += 1
i = 0
walkway.end_fill()
walkway.hideturtle()

while i < 23:     # front trees
    draw_tree(t, -660 + ix, -120 - iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy += 60
while i < 21:
    draw_tree(t, -630 + ix, -120 - iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy += 60
while i < 23:
    draw_tree(t, -660 + ix, -120 - iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy += 60
while i < 21:
    draw_tree(t, -630 + ix, -120 - iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy += 60
while i < 23:
    draw_tree(t, -660 + ix, -120 - iy)
    i += 1
    ix += 60
i = 0
ix = 0
iy = 0

semicircle_roof: Turtle = Turtle()
while i < 2:
    draw_semicircle_roof(semicircle_roof, -193 + ix, 230)
    i += 1
    ix += 425
i = 0
ix = 0
semicircle_roof.hideturtle()

brown_hori_panel2: Turtle = Turtle()
brown_hori_panel2.pencolor("mistyrose3")
brown_hori_panel2.pensize(1)
while i < 3:
    brown_hori_panel2.penup()
    brown_hori_panel2.goto(-250, 59 + iy)
    brown_hori_panel2.pendown()
    brown_hori_panel2.forward(515)
    i += 1
    iy += 50
if i == 3:
    brown_hori_panel2.penup()
    brown_hori_panel2.goto(-95, 59)
    brown_hori_panel2.pendown()
    brown_hori_panel2.forward(198)
i += 1
iy = 0
if i == 4:
    brown_hori_panel2.penup()
    brown_hori_panel2.goto(-250, 15)
    brown_hori_panel2.pendown()
    brown_hori_panel2.forward(515)
i = 0
iy = 0
brown_hori_panel2.hideturtle()

white_verti_panel: Turtle = Turtle()
while i < 2:
    draw_one_white_verti_panel(white_verti_panel, 222, -249 + ix, 173)
    i += 1
    ix += 513
i = 0
ix = 0
while i < 2:
    draw_one_white_verti_panel(white_verti_panel, 257, -93 + ix, 209)
    i += 1
    ix += 194
i = 0 
ix = 0
while i < 2:
    draw_one_white_verti_panel(white_verti_panel, 75, -40 + ix, 25)
    i += 1
    ix += 85
i = 0
ix = 0
while i < 2:
    draw_one_white_verti_panel(white_verti_panel, 75, -18 + ix, 25)
    i += 1
    ix += 41
i = 0
ix = 0


main_sign: Turtle = Turtle()
main_sign.pencolor("mistyrose3")
main_sign.penup()
main_sign.goto(40, 25)
main_sign.setheading(0.0)
main_sign.pendown()
main_sign.begin_fill()
main_sign.fillcolor("linen")
main_sign.left(90)
main_sign.circle(38, 180)
main_sign.end_fill()
main_sign.hideturtle()

upper_sign: Turtle = Turtle()
upper_sign.pencolor("mistyrose3")
upper_sign.penup()
upper_sign.goto(30, 217)
upper_sign.setheading(0.0)
upper_sign.pendown()
upper_sign.begin_fill()
upper_sign.fillcolor("linen")
upper_sign.left(90)
upper_sign.circle(25, 180)
upper_sign.setheading(0.0)
upper_sign.end_fill()
upper_sign.penup()
upper_sign.goto(15, 238)
upper_sign.setheading(0.0)
upper_sign.pendown()
upper_sign.begin_fill()
upper_sign.fillcolor("linen")
upper_sign.left(90)
upper_sign.circle(10, 180)
upper_sign.end_fill()
upper_sign.pencolor("skyblue4")
upper_sign.penup()
upper_sign.goto(5, 248)
upper_sign.setheading(0.0)
upper_sign.pendown()
upper_sign.left(90)
upper_sign.forward(20)
upper_sign.hideturtle()


crown_moulding: Turtle = Turtle()
draw_crown_moulding(crown_moulding, 156, -252, 173)
draw_crown_moulding(crown_moulding, 164, 102, 173)
draw_crown_moulding(crown_moulding, 202, -98, 215)
while i < 2:
    draw_crown_moulding(crown_moulding, 20, -217 + ix, 226)
    i += 1
    ix += 425
i = 0
ix = 0

white_hori_panel: Turtle = Turtle()
white_hori_panel.pencolor("linen")
white_hori_panel.pensize(3)
while i < 3:
    white_hori_panel.penup()
    white_hori_panel.goto(-250, 25 + iy)
    white_hori_panel.pendown()
    white_hori_panel.forward(515)
    i += 1
    iy += 50
if i == 3:
    white_hori_panel.penup()
    white_hori_panel.goto(-95, 27 + iy)
    white_hori_panel.pendown()
    white_hori_panel.forward(198)
i = 0
iy = 0
white_hori_panel.hideturtle()

brown_hori_panel: Turtle = Turtle()
brown_hori_panel.pencolor("mistyrose3")
brown_hori_panel.pensize(1)
while i < 3:
    brown_hori_panel.penup()
    brown_hori_panel.goto(-250, 23 + iy)
    brown_hori_panel.pendown()
    brown_hori_panel.forward(515)
    i += 1
    iy += 50
if i == 3:
    brown_hori_panel.penup()
    brown_hori_panel.goto(-95, 25 + iy)
    brown_hori_panel.pendown()
    brown_hori_panel.forward(198)
i = 0
iy = 0
brown_hori_panel.hideturtle()


room_window: Turtle = Turtle()
# for windows inside pillars
while i < 4:
    draw_one_room_window(room_window, -212, 30 + iy)
    i += 1
    iy += 50
i = 0
ix = 0
iy = 0 
while i < 4:
    draw_one_room_window(room_window, 213, 30 + iy)
    i += 1
    iy += 50
i = 0
ix = 0
iy = 0
# for outside windows
while i < 3:
    draw_one_room_window(room_window, -237, 30 + iy)
    i += 1
    iy += 50
i = 0
ix = 0
iy = 0
while i < 3:
    draw_one_room_window(room_window, 242, 30 + iy)
    i += 1
    iy += 50
i = 0
ix = 0
iy = 0
#  for left side windows
while i < 5:
    draw_one_room_window(room_window, -189 + ix, 30)
    i += 1
    ix += 20
i = 0
ix = 0
iy += 25
while i < 5:
    draw_one_room_window(room_window, -189 + ix, 80)
    i += 1
    ix += 20
i = 0
ix = 0
iy += 25
while i < 5:
    draw_one_room_window(room_window, -189 + ix, 130)
    i += 1
    ix += 20
i = 0
ix = 0
iy = 0
# for right side window
while i < 5:
    draw_one_room_window(room_window, 110 + ix, 30)
    i += 1
    ix += 20
i = 0
ix = 0
iy += 25
while i < 5:
    draw_one_room_window(room_window, 110 + ix, 80)
    i += 1
    ix += 20
i = 0
ix = 0
iy += 25
while i < 5:
    draw_one_room_window(room_window, 110 + ix, 130)
    i += 1
    ix += 20
i = 0
ix = 0
iy = 0
# main windows
while i < 2:
    draw_one_room_window(room_window, -80 + ix, 30)
    i += 1
    ix += 20
i = 0
ix = 0
iy += 25
while i < 2:
    draw_one_room_window(room_window, 60 + ix, 30)
    i += 1
    ix += 20
i = 0
ix = 0
iy += 25
while i < 9:
    draw_one_room_window(room_window, -80 + ix, 80)
    i += 1
    ix += 20
i = 0
ix = 0
iy += 25
while i < 9:
    draw_one_room_window(room_window, -80 + ix, 130)
    i += 1
    ix += 20
i = 0
ix = 0
iy += 25
while i < 9:
    draw_one_room_window(room_window, -80 + ix, 180)
    i += 1
    ix += 20
i = 0
ix = 0
iy = 0

bottom_window: Turtle = Turtle()
# outside and pillar bottom windows
while i < 2:
    draw_one_bottom_floor_window(bottom_window, -237, -40 + iy)
    i += 1
    iy += 35
iy = 0
while i < 4:
    draw_one_bottom_floor_window(bottom_window, 242, -40 + iy)
    i += 1
    iy += 35
i = 0
iy = 0
while i < 2:
    draw_one_bottom_floor_window(bottom_window, -212, -40 + iy)
    i += 1
    iy += 35
iy = 0
while i < 4:
    draw_one_bottom_floor_window(bottom_window, 213, -40 + iy)
    i += 1
    iy += 35
i = 0
iy = 0
# for right and left side bottom windows
while i < 3:
    draw_one_bottom_floor_window(bottom_window, -180 + ix, -40 + iy)
    i += 1
    ix += 30
ix = 0
iy += 35
while i < 6:
    draw_one_bottom_floor_window(bottom_window, -180 + ix, -40 + iy)
    i += 1
    ix += 30
i = 0
ix = 0
iy = 0
while i < 3:
    draw_one_bottom_floor_window(bottom_window, 119 + ix, -40 + iy)
    i += 1
    ix += 30
ix = 0
iy += 35
while i < 6:
    draw_one_bottom_floor_window(bottom_window, 119 + ix, -40 + iy)
    i += 1
    ix += 30
i = 0
ix = 0
iy = 0
# for main bottom windows adjacent to main door
while i < 2:
    draw_one_bottom_floor_window(bottom_window, -70, -40 + iy)
    i += 1
    iy += 35
iy = 0
while i < 4:
    draw_one_bottom_floor_window(bottom_window, 69, -40 + iy)
    i += 1
    iy += 35
i = 0
iy = 0
while i < 2:
    draw_one_bottom_floor_window(bottom_window, -34, -40 + iy)
    i += 1
    iy += 35
iy = 0
while i < 4:
    draw_one_bottom_floor_window(bottom_window, 29, -40 + iy)
    i += 1
    iy += 35
i = 0
iy = 0

done()
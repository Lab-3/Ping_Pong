"""

Εμφάνιση των σετ του παίκτη

"""
"""

Διαιρούμε τους πόντους του παίκτη και παίρνουμε τον ακέριο αριθμό, στρογγυλοποιώντας προς τα πάνω.

Στην συνέχεια, υπολογίζουμε το μέγεθος του Χ, ώστε αν είναι μικρότερο του 5 να μην γεμίσει ολόκληρη την γραμμή αλλά μόνο το υπόλοιπο των πόντων.

"""
"""

Εμφανίζει τους πόντους του αντιπάλου ξεκινώντας από την κάτω δεξιά γωνία.

"""
"""

Στην μπάλα δίνεται τυχαίος αριθμός από χτυπήματα

"""
"""

Αν κάποιος παίκτης κάνει το τελευταίο χτύπημα, χάνει. Ο αντίπαλος παίρνει έναν πόντο.

"""
"""

Για να αχήσει το παιχνίδι, θα πρέπει να πατήσει κάθε παίκτης τα πλήκτρα ΑΒ ταυτόχρονα.

Κάθε παίκτης θα ονομαστεί σε Παίκτης 1 ή 2

"""

def on_button_pressed_ab():
    global Ball, Play, P_Num, Point
    if Play == 0 and P_Num == "P0":
        basic.show_icon(IconNames.SMALL_DIAMOND)
        Ball = 0
        Play = 1
        P_Num = "P1"
        radio.send_value("Player", Play)
    elif Play == 1 and P_Num == "P0":
        basic.show_icon(IconNames.DIAMOND)
        Ball = 1
        Play = 2
        P_Num = "P2"
        Point = randint(5, 20)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

"""

Εμφάνιση πόντο του παίκτη

"""

def on_button_pressed_a():
    global X, Y, Z
    basic.clear_screen()
    X = 0
    Y = 0
    for index in range(Math.ceil(Your_Points / 5)):
        for index2 in range(Your_Points - Y * 5):
            led.plot(X, Y)
            X += 1
        Y += 1
        X = 0
    X = 4
    Y = 4
    Z = 0
    for index3 in range(Math.ceil(Other_Points / 5)):
        for index4 in range(Other_Points - Z * 5):
            led.plot(X, Y)
            X += -1
        Y += -1
        X = 4
        Z += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

"""

Κάθε φορά που έχουμε την μπάλα, στο κούνια, στέλνουμε την μπάλα στον άλλο και αγερούμε ένα πόντο από την μπάλα

"""

def on_gesture_six_g():
    global Point, Ball, Other_Points, Other_Sets
    if Ball == 1:
        Point += -1
        music.play(music.create_sound_expression(WaveShape.SINE,
                500,
                500,
                255,
                0,
                50,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(50)
        if 0 < Point:
            Ball = 0
            basic.show_icon(IconNames.SMALL_DIAMOND)
            radio.send_value(P_Num, Point)
        elif 0 >= Point:
            basic.show_icon(IconNames.NO)
            Ball = 0
            music._play_default_background(music.built_in_playable_melody(Melodies.POWER_DOWN),
                music.PlaybackMode.UNTIL_DONE)
            radio.send_string("Win")
            Other_Points += 1
            if Other_Points == 11:
                Other_Sets += 1
                Other_Points = 0
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

def on_received_string(receivedString):
    global Your_Points, Ball, Point, Your_Sets
    basic.pause(100)
    if receivedString == "Win":
        basic.show_icon(IconNames.YES)
        music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
            music.PlaybackMode.UNTIL_DONE)
        Your_Points += 1
        basic.pause(200)
        basic.show_icon(IconNames.DIAMOND)
        Ball = 1
        Point = randint(5, 20)
        if Your_Points == 11:
            Your_Sets += 1
            Your_Points = 0
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global X, Y, Z
    basic.clear_screen()
    X = 0
    Y = 0
    for index5 in range(Math.ceil(Your_Sets / 5)):
        for index6 in range(Your_Sets - Y * 5):
            led.plot(X, Y)
            X += 1
        Y += 1
        X = 0
    X = 4
    Y = 4
    Z = 0
    for index7 in range(Math.ceil(Other_Sets / 5)):
        for index8 in range(Other_Sets - Z * 5):
            led.plot(X, Y)
            X += -1
        Y += -1
        X = 4
        Z += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global Play, Point, Ball
    if name == "Player":
        Play = value
    if P_Num != name and Ball == 0:
        Point = value
        basic.show_icon(IconNames.DIAMOND)
        Ball = 1
radio.on_received_value(on_received_value)

def on_logo_pressed():
    basic.show_number(Point)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

"""

Δημιουργούμε και αρχικοποιούμε της μεταβολικές μας

"""
Z = 0
Y = 0
X = 0
Other_Points = 0
Other_Sets = 0
Your_Points = 0
Your_Sets = 0
Ball = 0
P_Num = ""
Play = 0
Point = 0
radio.set_group(1)
music.set_volume(255)
Point = 0
Play = 0
P_Num = "P0"
Ball = 3
Your_Sets = 0
Your_Points = 0
Other_Sets = 0
Other_Points = 0
basic.show_leds("""
    # . . . #
    # . . . #
    # . . . #
    # . . . #
    # . . . #
    """)
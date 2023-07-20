/**
 * Εμφάνιση των σετ του παίκτη
 */
/**
 * Διαιρούμε τους πόντους του παίκτη και παίρνουμε τον ακέριο αριθμό, στρογγυλοποιώντας προς τα πάνω.
 * 
 * Στην συνέχεια, υπολογίζουμε το μέγεθος του Χ, ώστε αν είναι μικρότερο του 5 να μην γεμίσει ολόκληρη την γραμμή αλλά μόνο το υπόλοιπο των πόντων.
 */
/**
 * Εμφανίζει τους πόντους του αντιπάλου ξεκινώντας από την κάτω δεξιά γωνία.
 */
/**
 * Στην μπάλα δίνεται τυχαίος αριθμός από χτυπήματα
 */
/**
 * Αν κάποιος παίκτης κάνει το τελευταίο χτύπημα, χάνει. Ο αντίπαλος παίρνει έναν πόντο.
 */
/**
 * Για να αχήσει το παιχνίδι, θα πρέπει να πατήσει κάθε παίκτης τα πλήκτρα ΑΒ ταυτόχρονα.
 * 
 * Κάθε παίκτης θα ονομαστεί σε Παίκτης 1 ή 2
 */
input.onButtonPressed(Button.AB, function () {
    if (Play == 0 && P_Num == "P0") {
        basic.showIcon(IconNames.SmallDiamond)
        Ball = 0
        Play = 1
        P_Num = "P1"
        radio.sendValue("Player", Play)
    } else if (Play == 1 && P_Num == "P0") {
        basic.showIcon(IconNames.Diamond)
        Ball = 1
        Play = 2
        P_Num = "P2"
        Point = randint(5, 20)
    }
})
/**
 * Εμφάνιση πόντο του παίκτη
 */
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    X = 0
    Y = 0
    for (let index = 0; index < Math.ceil(Your_Points / 5); index++) {
        for (let index = 0; index < Your_Points - Y * 5; index++) {
            led.plot(X, Y)
            X += 1
        }
        Y += 1
        X = 0
    }
    X = 4
    Y = 4
    Z = 0
    for (let index = 0; index < Math.ceil(Other_Points / 5); index++) {
        for (let index = 0; index < Other_Points - Z * 5; index++) {
            led.plot(X, Y)
            X += -1
        }
        Y += -1
        X = 4
        Z += 1
    }
})
/**
 * Κάθε φορά που έχουμε την μπάλα, στο κούνια, στέλνουμε την μπάλα στον άλλο και αγερούμε ένα πόντο από την μπάλα
 */
input.onGesture(Gesture.SixG, function () {
    if (Ball == 1) {
        Point += -1
        music.play(music.createSoundExpression(WaveShape.Sine, 500, 500, 255, 0, 50, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        basic.pause(50)
        if (0 < Point) {
            Ball = 0
            basic.showIcon(IconNames.SmallDiamond)
            radio.sendValue(P_Num, Point)
        } else if (0 >= Point) {
            basic.showIcon(IconNames.No)
            Ball = 0
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerDown), music.PlaybackMode.UntilDone)
            radio.sendString("Win")
            Other_Points += 1
            if (Other_Points == 11) {
                Other_Sets += 1
                Other_Points = 0
            }
        }
    }
})
radio.onReceivedString(function (receivedString) {
    basic.pause(100)
    if (receivedString == "Win") {
        basic.showIcon(IconNames.Yes)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.UntilDone)
        Your_Points += 1
        basic.pause(200)
        basic.showIcon(IconNames.Diamond)
        Ball = 1
        Point = randint(5, 20)
        if (Your_Points == 11) {
            Your_Sets += 1
            Your_Points = 0
        }
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    X = 0
    Y = 0
    for (let index = 0; index < Math.ceil(Your_Sets / 5); index++) {
        for (let index = 0; index < Your_Sets - Y * 5; index++) {
            led.plot(X, Y)
            X += 1
        }
        Y += 1
        X = 0
    }
    X = 4
    Y = 4
    Z = 0
    for (let index = 0; index < Math.ceil(Other_Sets / 5); index++) {
        for (let index = 0; index < Other_Sets - Z * 5; index++) {
            led.plot(X, Y)
            X += -1
        }
        Y += -1
        X = 4
        Z += 1
    }
})
radio.onReceivedValue(function (name, value) {
    if (name == "Player") {
        Play = value
    }
    if (P_Num != name && Ball == 0) {
        Point = value
        basic.showIcon(IconNames.Diamond)
        Ball = 1
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showNumber(Point)
})
/**
 * Δημιουργούμε και αρχικοποιούμε της μεταβολικές μας
 */
let Z = 0
let Y = 0
let X = 0
let Other_Points = 0
let Other_Sets = 0
let Your_Points = 0
let Your_Sets = 0
let Ball = 0
let P_Num = ""
let Play = 0
let Point = 0
radio.setGroup(1)
music.setVolume(255)
Point = 0
Play = 0
P_Num = "P0"
Ball = 3
Your_Sets = 0
Your_Points = 0
Other_Sets = 0
Other_Points = 0
basic.showLeds(`
    # . . . #
    # . . . #
    # . . . #
    # . . . #
    # . . . #
    `)

def on_up_pressed():
    controller.move_sprite(mySprite, 100, 100)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    controller.move_sprite(mySprite, 100, 100)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    controller.move_sprite(mySprite, 100, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    controller.move_sprite(mySprite, 100, 100)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    controller.move_sprite(mySprite, 100, 100)
    controller.player1.move_sprite(mySprite, 100, 100)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    controller.move_sprite(mySprite, 100, 100)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

mySprite: Sprite = None
scene.set_background_image(assets.image("""
    bextru
"""))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
    sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                . . . . 6 6 6 6 6 6 6 6 . . . . 
                . . . 6 9 6 6 6 6 6 6 c 6 . . . 
                . . 6 c 9 6 6 6 6 6 6 c c 6 . . 
                . 6 c c 9 9 9 9 9 9 6 c c 9 6 d 
                . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6 
                . 6 6 8 b b 8 b b b 8 8 b 9 6 6 
                . 6 8 b b b 8 b b b b 8 6 6 6 6 
                . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6 
                . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d 
                . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d 
                . 8 8 8 8 8 8 f f f 8 8 8 8 8 8 
                . 8 f f f f 8 8 8 8 f f f 8 8 8 
                . . f f f f f 8 8 f f f f f 8 . 
                . . . f f f . . . . f f f f . . 
                . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player))
scene.camera_follow_sprite(mySprite)
_893930101001 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . 9 . . 9 . . . 
            . . . . . . . 9 . . 9 . . . . . 
            . 9 9 . . . . . . . . . . . . 9 
            . 9 9 . . . . . . 9 . . 9 . . . 
            . . . . . . . 9 . . . . . . . 9 
            . . . . . . . . . . . . 9 . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
MakeyMakey.set_simulator_keymap(MakeyMakey.PlayerNumber.ONE,
    MakeyMakey.MakeyMakeyKey.UP,
    MakeyMakey.MakeyMakeyKey.DOWN,
    MakeyMakey.MakeyMakeyKey.LEFT,
    MakeyMakey.MakeyMakeyKey.RIGHT,
    MakeyMakey.MakeyMakeyKey.W,
    MakeyMakey.MakeyMakeyKey.UP)
MakeyMakey.set_simulator_keymap(MakeyMakey.PlayerNumber.TWO,
    MakeyMakey.MakeyMakeyKey.UP,
    MakeyMakey.MakeyMakeyKey.UP,
    MakeyMakey.MakeyMakeyKey.UP,
    MakeyMakey.MakeyMakeyKey.UP,
    MakeyMakey.MakeyMakeyKey.UP,
    MakeyMakey.MakeyMakeyKey.UP)
music.play(music.create_song(assets.song("""
        092829372839
    """)),
    music.PlaybackMode.UNTIL_DONE)
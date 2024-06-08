controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(cube_in_code, 100, 100)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(cube_in_code, 100, 100)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(cube_in_code, 100, 100)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(cube_in_code, 100, 100)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(cube_in_code, 100, 100)
    controller.player1.moveSprite(cube_in_code, 100, 100)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(cube_in_code, 100, 100)
})
let cube_in_code: Sprite = null
scene.setBackgroundImage(assets.image`bextru`)
scene.cameraFollowSprite(cube_in_code)
cube_in_code = sprites.create(assets.image`cube`, SpriteKind.Player)
MakeyMakey.setSimulatorKeymap(
MakeyMakey.PlayerNumber.ONE,
MakeyMakey.MakeyMakeyKey.UP,
MakeyMakey.MakeyMakeyKey.DOWN,
MakeyMakey.MakeyMakeyKey.LEFT,
MakeyMakey.MakeyMakeyKey.RIGHT,
MakeyMakey.MakeyMakeyKey.W,
MakeyMakey.MakeyMakeyKey.UP
)
MakeyMakey.setSimulatorKeymap(
MakeyMakey.PlayerNumber.TWO,
MakeyMakey.MakeyMakeyKey.UP,
MakeyMakey.MakeyMakeyKey.UP,
MakeyMakey.MakeyMakeyKey.UP,
MakeyMakey.MakeyMakeyKey.UP,
MakeyMakey.MakeyMakeyKey.UP,
MakeyMakey.MakeyMakeyKey.UP
)
animation.runMovementAnimation(
cube_in_code,
animation.animationPresets(animation.flyToCenter),
2000,
true
)
music.play(music.createSong(assets.song`092829372839`), music.PlaybackMode.UntilDone)
console.log("6.7.8.9.0")

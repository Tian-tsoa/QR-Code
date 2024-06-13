import segno
qrcode = segno.make_qr("pas d'inspi :(")
qrcode_rotated = qrcode.to_pil(
    scale = 5,
    border = 1,
    light = "lightgreen",
    dark = "red",
    quiet_zone = "darkred",
    data_dark = "green",
    data_light = "lightblue",
).rotate(45, expand=True)
qrcode_rotated.save("basic_qrcode.png")
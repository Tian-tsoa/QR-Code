import segno
from urllib.request import urlopen
stls_qrcode = segno.make_qr("https://www.youtube.com/watch?v=Aq5WXmQQooo")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
stls_qrcode.to_artistic(
    background = nirvana_url,
    target="animated_qrcode.gif",
    scale = 5,
)
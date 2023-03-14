import qrcode
#whatever we provide will make it qr
img=qrcode.make('https://github.com/a21amit')
img.save('myHubqr.png')
img.show()

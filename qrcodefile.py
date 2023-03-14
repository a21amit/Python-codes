import qrcode
img=qrcode.make('https://github.com/a21amit')
img.save('myHubqr.png')
img.show()
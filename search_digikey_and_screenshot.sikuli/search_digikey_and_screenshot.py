parts_list = [	
    "aaa",
    "bbb",
    "ccc"
        ]

for com in parts_list:
    click(Pattern("1508286765749.png").targetOffset(-112,-34))
    paste(com)
    type(Key.ENTER)
    sleep(1)

    # winshot run and setted ALT+z is getting screenshot
    keyDown(Key.ALT)
    type("z")
    keyUp(Key.ALT)
    sleep(1)
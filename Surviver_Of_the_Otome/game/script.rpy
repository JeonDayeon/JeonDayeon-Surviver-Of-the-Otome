# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
init python:
    day = 0
    dtime = '낮'
    i = 0
    ehyeon_love = 0

init:

    screen daytime:
        frame:
            xalign 0.5
            hbox:
                spacing 10
                text "[day]일째"
                text "[dtime]"
    
    image bg_myroomOn = ("images/myroom_dusk_light_on.png")
    image bg_park = ("images/park.jpg")

    image ehyeon :
        im.FactorScale("images/ehyeon_standing.png", 0.3)
        yalign 0.0
        xalign 0.0

    define e = Character('이현', color="#c8ffc8")
# 여기에서부터 게임이 시작합니다.
label start:

    $ day += 1 
    scene bg_park

    show screen daytime 
    show ehyeon at left

    e "새로운 렌파이 게임을 만들었군요."

    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    e "깃허브 데스크탑"




label room:
    $ dtime = '밤'
    $ day += 1
    scene bg_myroomOn

    show screen daytime
    show ehyeon at left 
    e "집집"

    return


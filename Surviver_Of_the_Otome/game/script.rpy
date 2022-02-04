# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
init python:
    ##이름 입력 변수
    player_name='지안'

    ##시간 변수######################
    day = 0
    dtime = '낮'
    ################################

    i = 0
    ehyeon_love = 0
    num = 0




init:

    screen daytime:
        frame:
            xalign 0.5
            yalign 0.02
            hbox:
                spacing 10
                text "[day]일째"
                text "[dtime]"
    
    image box = "gui/selectUI.png"

    image bg_myroomOn = ("images/myroom_dusk_light_on.png")
    image bg_park = ("images/park.jpg")

    image ehyeon :
        im.FactorScale("images/ehyeon_standing.png", 0.3)
        yalign 0.0
        xalign 0.0

    screen name_box(title, inputxt):
        frame:
            background "#fff0"
            image "gui/selectUI.png"
            xalign 0.5 yalign 0.5
        vbox:
            spacing 50
            xalign 0.5
            yalign 0.58
            text "[title]"  color '#000000' size 38
            input default :
                value VariableInputValue("player_name")
                xalign 0.5 ypos -30 color '#000000'

            imagebutton:
                idle "gui/button/selectButtonOK.png" hover "gui/button/selectButtonOK_hover.png"
                action Jump ("meetehyeon")
                xalign 0.5 ypos -33
            
    define e = Character('이현', color="#c8ffc8")
# 여기에서부터 게임이 시작합니다.
label start:

    $ day += 1 
    scene bg_park

    show screen daytime 
    show ehyeon at left

    e "새로운 렌파이 게임을 만들었군요."

    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    e "이름 알려줄래요?"

    menu:
        "그래":
            jump enter_name
        
        "싫어":
            e '...'
            jump room

label enter_name:
    $ player_name = renpy.call_screen("name_box", title = "이름을 입력해주세요.", inputxt = "[player_name]")


label meetehyeon:
    e "[player_name]이군요!"




label room:
    $ dtime = '밤'
    $ day += 1
    scene bg_myroomOn

    show screen daytime
    show ehyeon at left 
    e "집집"

    return


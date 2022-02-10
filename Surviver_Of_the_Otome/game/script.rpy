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

    ##버튼 입력#################################################################    
    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)
    #############################################################################

    tutorial = False
    lmap = False
    location = '공원'



init:
## 이미지 ###############################################################
    image box = "gui/selectUI.png"

    image bg_myroomOn = ("images/myroom_dusk_light_on.png")
    image bg_park = ("images/park.jpg")
    image bg_school = ("images/schoolbg2.png")

## 캐릭터 이미지 
    image ehyeon :
        im.FactorScale("images/ehyeon_standing.png", 0.3)
        yalign 0.0
        xalign 0.0

    image jihun :
        im.FactorScale("images/jihun_1.png", 0.35)
        yalign 0.0
        xalign 0.0

#####################################################################

    screen MapButton:
        frame:
            background "#424242"
            xalign 1.01
            yalign 0.2

            hbox:
                imagebutton:
                    idle ("gui/button/map_idle.png") hover("gui/button/map_hover.png")
                    action Show ("map")

    screen map:
        modal True
        imagemap:
            ground "images/mapimage.jpg"
            hover "images/mapimage.jpg"
            hotspot (596, 4, 723, 504) action Return("School")##학교
            hotspot (1497, 39, 341, 609) action Return("greenhouse")##온실
            hotspot (1158, 643, 449, 433) action Return("mazegarden")##미로
            hotspot (157, 632, 445, 426) action Return("canteen")##매점
            hotspot (46, 31, 427, 492) action Return("cafe")##카페
            xalign 0.5 yalign 0.5
        
        textbutton "X":
            action Hide("map")
            xalign 0.99 yalign 0.0

    screen daytime:
        frame:
            xalign 0.5
            yalign 0.02
            hbox:
                spacing 10
                text "[day]일째"
                text "[dtime]"

    screen name_box(title):
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
                xalign 0.5 ypos -30
                color '#000000'

            imagebutton:
                idle "gui/button/selectButtonOK.png" hover "gui/button/selectButtonOK_hover.png"
                action Jump ("meetehyeon")
                xalign 0.5 ypos -33

## 캐릭터 
    define e = Character('이현', color="#c8ffc8")
    define j = Character('배지훈', color = "#ff0000c2")


# 여기에서부터 게임이 시작합니다.
label start:

    $ day += 1 
    scene bg_park

    show screen daytime
    show screen MapButton 
    show jihun at left

    j "새로운 렌파이 게임을 만들었군요."

    j "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    j "이름 알려줄래요?"

    menu:
        "그래":
            jump enter_name
        
        "싫어":
            e '...'
            return

    return

label enter_name:
    call screen name_box(title = "이름을 입력해주세요.")


label meetehyeon:
    e "[player_name]이군요!"
    e "시 작작 시작"
    e "이제 맵 이동을 해보자 오른쪽 상단에 맵이동을 클릭해서 학교에 가봐요"
     

label School:
    hide screen map
    scene bg_school
    if (tutorial == False):
        show ehyeon at left 
        e "잘하셨어요!"
        e "이제 머하지"
        return

label greenhouse:
    j "여기는 온실이야"

label mazegarden:
    j "여긴 미로정원"

label canteen:
    j "여기는 매점"

label cafe:
    j "여기는 카페"

label room:
    $ dtime = '밤'
    $ day += 1
    scene bg_myroomOn

    show screen daytime
    show ehyeon at left 
    e "집집"

    return


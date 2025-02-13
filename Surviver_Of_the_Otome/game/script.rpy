﻿# 이 파일에 게임 스크립트를 입력합니다.

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

    ##호감도 변수####################
    e_love = 0
    j_love = 0
    ################################

    ##버튼 입력#################################################################    
    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)
    #############################################################################

    ##UI용 변수#####################
    tutorial = False
    lmap = False
    location = '공원'
    ################################



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

##맵 스크린#############################################################################################################
    screen MapButton:
        frame:
            background "#424242"
            xalign 1.01
            yalign 0.2

            hbox:
                imagebutton:
                    idle ("gui/button/map_idle.png") hover("gui/button/map_hover.png")
                    if (lmap == False):
                        action Show ("nloadUI")
                        
                    else:
                        action Show ("map")

    screen map:
        modal True
        imagemap:
            ground "images/mapimage.jpg"
            hover "images/mapimage.jpg"
            hotspot (596, 4, 723, 504) action Jump("school"), SetVariable("location", '학교')##학교
            hotspot (1497, 39, 341, 609) action Jump("greenhouse"), SetVariable("location", '온실')##온실
            hotspot (1158, 643, 449, 433) action Jump("mazegarden"), SetVariable("location", '미로')##미로
            hotspot (157, 632, 445, 426) action Jump("canteen"), SetVariable("location", '매점')##매점
            hotspot (46, 31, 427, 492) action Jump("cafe"), SetVariable("location", '카페')##카페
            xalign 0.5 yalign 0.5
        
        textbutton "X":
            action Hide("map")
            xalign 0.99 yalign 0.0
######################################################################################################################

##안내창###############################################################################################################
    screen nloadUI:
        timer 1 action Hide("nloadUI")
        frame:
            background ('#474747a4')
            padding (300, 90)
            xalign 0.5 yalign 0.5
            text "아직 이용 불가능합니다.":
                xalign 0.5 yalign 0.5
                size 50
######################################################################################################################

######################################################################################################################
    screen daytime:
        frame:
            xalign 0.5
            yalign 0.02
            hbox:
                spacing 10
                text "[day]일째"
                text "[dtime]"

    screen stat:
        frame:
            padding (15, 15)

            xalign 0.0 yalign 0.0

            xmaximum 250
            ymaximum 200

            vbox:
                spacing 10
                vbox:
                    text "이현 [e_love]" size 16
                    bar:
                        value e_love
                        range 100

                        style "fixed_bar"

                vbox:
                    text "배지훈 [j_love]" size 16
                    bar:
                        value j_love
                        range 100

                        style "fixed_bar"    
######################################################################################################################

##입력 스크린##########################################################################################################
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
######################################################################################################################


## 캐릭터 
    define e = Character('이현', color="#c8ffc8")
    define j = Character('배지훈', color = "#ff0000c2")


# 여기에서부터 게임이 시작합니다.
label start:

    $ day += 1 
    scene bg_park

    show screen stat
    show screen daytime
    show screen MapButton 
    show jihun at left

    j "새로운 렌파이 게임을 만들었군요."

    j "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    j "이름 알려줄래요?"

    menu:
        "그래":
            $e_love += 10
            jump enter_name
        
        "싫어":
            j '...'
            return

    return

label enter_name:
    call screen name_box(title = "이름을 입력해주세요.")


label meetehyeon:
    e "[player_name]이군요!"
    e "시 작작 시작" 
    $lmap = True
    e "이제 맵 이동을 해보자 오른쪽 상단에 맵이동을 클릭해서 학교에 가봐요"

label school:
    hide screen map
    scene bg_school
    if (tutorial == False):
        show ehyeon at left 
        e "잘하셨어요!"
        e "이제 머하지"

        jump room

label greenhouse:
    hide screen map
    j "여기는 온실이야"

label mazegarden:
    hide screen map
    j "여긴 미로정원"

label canteen:
    hide screen map
    j "여기는 매점"

label cafe:
    hide screen map
    j "여기는 카페"

label room:
    $ dtime = '밤'
    $ day += 1
    scene bg_myroomOn
    show jihun at left 
    j "어쩌구 저쩌구"
    show screen daytime

    return


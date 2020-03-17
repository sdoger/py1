import pygame

import os

pygame.mixer.init()#初始化音频部分

musicpath = []

num = 0

login = True

path = r"i:\mp3" #音乐文件的路径

musiclist = os.listdir(path)

#print(musiclist)

for musicname in musiclist:#将音乐放入列表中

    if 'mp3' in musicname:

        musicpath.append(os.path.join(path,musicname))

    else:

        continue

#print(musicpath)


def interface():

    print("********************************************")

    print("  1.播放  2.暂停  3.下一曲    4.上一曲")

    print("  5.增大音量      6.减小音量    7.退出  ")

    print("********************************************")



def playMusic():#播放音乐

    if pygame.mixer_music.get_busy() != 1:

        pygame.mixer_music.unpause()

    pygame.mixer.music.load(musicpath[num])

    pygame.mixer_music.play()

def pauseMusic():#暂停音乐

    if pygame.mixer_music.get_busy() != 1:

        pygame.mixer_music.unpause()

    pygame.mixer.music.load(musicpath[num])

    pygame.mixer_music.play()

def nextMusic():#下一曲

    global num

    num += 1

    # pygame.mixer.music.stop()

    pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

    # pygame.mixer.music.queue(filename)

    pygame.mixer_music.load(musicpath[num])

    pygame.mixer_music.play()

    print("当前正在播放:%s" % musiclist[num])

def prevMusic():#上一曲

    global num

    num -= 1

    pygame.mixer.music.stop()

    pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

    # pygame.mixer.music.queue(filename)

    pygame.mixer_music.load(musicpath[num])

    pygame.mixer_music.play()

    print("当前正在播放:%s" % musiclist[num])

def addvolume():#加音量

    global volume

    if volume + 0.5 > 10:

        print("音量不能再加大了...")

    else:

        volume += 0.5

        pygame.mixer_music.set_volume(volume)

        print("音量已增大,当前音量为:%.3s" % volume)

def reducevolume():#减音量

    global volume

    if volume - 0.5 < 0:

        print("音量已经很小的...")

    else:

        volume -= 0.5

        pygame.mixer_music.set_volume(volume)

        print("音量已减小,当前音量为:%.3s" % volume)

def quitSystem():#推出

    global login

    pygame.mixer.music.stop()

    login = False

    print("退出成功...")


def opearting(n):#操作

    global login

    global volume

    global num

    if n == 1:

        playMusic()

    elif n == 2:

        pauseMusic()

    elif n == 3:

        nextMusic()

    elif n == 4:

      prevMusic()

    elif n == 5:

      addvolume()

    elif n == 6:

      reducevolume()

    elif n == 7:

        quitSystem()



if __name__ == '__main__':

    interface()#界面    #选择操作

    while login :

        select = int(input("请输入操作:"))

        opearting(select)#操作函数

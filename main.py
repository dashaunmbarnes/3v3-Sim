import replit
import time
import random
#list for players chosen
p1list=[]
p2list=[]
#list of players
playerlist=["butler","zion","kat","curry","lebron","mj","kd","kareem","magic","kobe","giannis","dame","shaq","lamelo","russ","fox","morant","ingram","luka","bam","klay","trae","wilt","dlo","draymond","kyrie","booker","ad","paul","iggy","embiid","jokic"]
#tendenices for players
#
#
#[pass,turnover,shoot,pull up,drive,post hook,post fade,back down,]
butlert=[10,5,25,30,30,0,20,0]
jokict=[50,5,30,25,30,15,25,15]
embiidt=[20,10,30,25,40,18,29,35]
iggyt=[40,10,30,15,20,0,30,5]
pault=[70,0,30,50,20,0,20,0]
adt=[5,5,40,35,30,10,30,20]
bookert=[5,5,60,50,20,0,40,0]
kyriet=[30,4,30,40,35,0,20,0]
drayt=[70,5,15,10,40,5,5,20]
dlot=[18,9,30,50,40,0,20,0]
wiltt=[5,5,0,0,10,50,10,90]
traet=[15,5,60,60,30,0,0,0]
klayt=[30,0,50,50,20,0,30,0]
ziont=[5,5,20,0,90,12,20,90]
katt=[5,5,40,40,40,30,50,60]
bamt=[5,5,5,10,70,20,15,40]
lukat=[45,9,50,70,35,3,12,0]
ingramt=[9,8,30,62,40,0,0,0]
morantt=[10,9,30,30,55,0,0,0]
foxt=[12,9,40,50,65,0,0,0]
russt=[50,20,30,35,70,0,0,5]
lamelot=[60,8,88,60,55,0,0,0]
shaqt=[6,20,0,0,50,25,0,99]
damet=[55,15,97,88,5,5,20,5]
curryt=[25,10,91,60,60,0,0,0]
lebront=[30,8,55,50,80,5,60,23]
mjt=[60,9,25,70,65,5,80,12]
kdt=[35,9,50,80,55,0,45,0]
kareemt=[25,12,0,0,20,80,30,65]
magict=[85,7,39,68,62,8,53,10]
kobet=[15,11,35,70,60,5,80,25]
giannist=[35,14,12,12,90,60,30,86]
#stats for player
#
#
#[shooting,driving,post hook,post fade,s and f,pd,id,ovr,name,tend]
butlers=[80,87,60,85,75,93,65,84,"butler",butlert]
jokics=[91,88,85,92,90,55,85,94,"jokic",jokict]
embiids=[84,91,85,88,90,60,90,93,"embiid",embiidt]
iggys=[82,79,60,85,75,86,60,80,"iggy",iggyt]
pauls=[91,88,0,88,0,88,20,91,"paul",pault]
ads=[84,88,90,91,90,81,85,90,"ad",adt]
bookers=[91,85,0,88,5,85,75,90,"booker",bookert]
kyries=[90,90,0,85,0,87,30,91,"kyrie",kyriet]
drays=[70,80,75,70,80,93,94,87,"draymond",drayt]
dlos=[83,86,0,85,0,82,60,84,"dlo",dlot]
wilts=[0,91,90,80,96,30,90,93,"wilt",wiltt]
traes=[95,80,0,80,0,85,60,88,"trae",traet]
klays=[97,80,0,90,0,93,70,90,"klay",klayt]
zions=[70,94,80,70,98,80,83,92,"zion",ziont]
kats=[88,85,80,92,90,60,90,88,"kat",katt]
bams=[65,90,80,83,90,88,93,87,"bam",bamt]
lukas=[93,88,30,88,70,79,70,94,"luka",lukat]
ingrams=[85,80,75,60,85,68,86,85,"ingram",ingramt]
morants=[89,96,75,78,65,85,70,93,"morant",morantt]
foxs=[83,92,78,75,65,72,70,89,"fox",foxt]
russs=[70,90,80,78,70,87,74,89,"russ",russt]
lamelos=[90,88,70,82,65,84,70,90,"lamelo",lamelot]
shaqs=[0,88,75,50,99,50,95,94,"shaq",shaqt]
dames=[96,75,65,80,5,77,26,93,"dame",damet]
currys=[99,90,80,93,50,90,25,98,"curry",curryt]
lebrons=[90,99,85,97,93,91,90,99,"lebron",lebront]
mjs=[93,97,90,99,90,97,88,99,"mj",mjt]
kds=[94,90,75,88,80,88,79,96,"kd",kdt]
kareems=[5,89,99,75,89,65,94,94,"kareem",kareemt]
magics=[65,85,70,85,70,90,89,97,"magic",magict]
kobes=[90,91,75,98,65,96,67,96,"kobe",kobet]
gianniss=[60,99,70,75,96,88,92,95,"giannis",giannist]
plfs=[lukas,ingrams,morants,foxs,russs,lamelos,shaqs,dames,currys,lebrons,mjs,kds,kareems,magics,kobes,gianniss,bams,kats,zions,klays,traes,wilts,dlos,drays,kyries,bookers,ads,pauls,iggys,embiids,jokics,butlers]
#program variables
scene=0
C1P1=0
C2P1=0
C3P1=0
C1P2=0
C2P2=0
C3P2=0
score1=0
score2=0
pos=1
wt=0
fga1=0
fga2=0
fga3=0
fgm1=0
fgm2=0
fgm3=0
tfga1=0
tfga2=0
tfga3=0
tfgm1=0
tfgm2=0
tfgm3=0
ps1=0
ps2=0
ps3=0
tps1=0
tps2=0
tps3=0
CA=0
def AC():
  CAT=[]
  passtend=int(input("What is your players pass tendency?"))
  CAT.append(passtend)
  turntend=int(input("What is your players turnover tendency?"))
  CAT.append(turntend)
  shoottend=int(input("What is your players shoot tendency?"))
  CAT.append(shoottend)
  pulltend=int(input("What is your players pull-up tendency?"))
  CAT.append(pulltend)
  drivetend=int(input("What is your players drive tendency?"))
  CAT.append(drivetend)
  phtend=int(input("What is your players post-hook tendency?"))
  CAT.append(phtend)
  pftend=int(input("What is your players post-fade tendency?"))
  CAT.append(pftend)
  bdtend=int(input("What is your players backdown tendency?"))
  CAT.append(bdtend)
  replit.clear()
  CAS=[]
  shootstat=int(input("What is your players shooting stat?"))
  CAS.append(shootstat)
  drivestat=int(input("What is your players driving stat?"))
  CAS.append(drivestat)
  phstat=int(input("What is your players post-hook stat?"))
  CAS.append(phstat)
  shootstat=int(input("What is your players postfade stat?"))
  CAS.append(shootstat)
  sfstat=int(input("What is your players strength and finishing?"))
  CAS.append(sfstat)
  pdstat=int(input("What is your players perimeter defense?"))
  CAS.append(pdstat)
  idstat=int(input("What is your players interior defense?"))
  CAS.append(idstat)
  ovrstat=int(input("What is your players overall?"))
  CAS.append(ovrstat)
  CAN=input("What is your players name?")
  CAS.append(CAN)
  playerlist.append(CAN)
  CAS.append(CAT)
  plfs.append(CAS)
  replit.clear()
  Menu()
  
def Menu():
  print("Welcome to 3v3 sim")
  print("1: To start Game")
  print("2: Add custom players")
  wwyd=input("")
  if wwyd=="1":
    replit.clear()
  if wwyd=="2":
    AC()
replit.clear()
Menu()
def ShowPlayers():
  for item in plfs:
    print(item[8],"","","","overall:",item[7])
def showScore():
  print("Team1:",score1,"Team2:",score2)
  time.sleep(wt)
  print("Team",pos,"has possesion")
  time.sleep(wt)
  replit.clear()
while scene==0:
  while C1P1==0:
    ShowPlayers()
    print("Player 1 Who would you like to pick first")
    P1P1=input("").lower()
    for item in playerlist:
      if item==P1P1:
        C1P1=1
        p1list.append(P1P1)

    replit.clear()
  while C2P1==0:
    ShowPlayers()
    print("Player 1 Who would you like to pick second")
    P1P2=input("").lower()
    for item in playerlist:
      if item==P1P2:
        C2P1=1
        p1list.append(P1P2)
    replit.clear()
  while C3P1==0:
    ShowPlayers()
    print("Player 1 Who would you like to pick last")
    P1P3=input("").lower()
    for item in playerlist:
      if item==P1P3:
        C3P1=1
        p1list.append(P1P3)
    replit.clear()
  while C1P2==0:
    ShowPlayers()
    print("Player 2 Who would you like to pick first")
    P2P1=input("").lower()
    for item in playerlist:
      if item==P2P1:
        C1P2=1
        p2list.append(P2P1)
    replit.clear()
  while C2P2==0:
    ShowPlayers()
    print("Player 2 Who would you like to pick second")
    P2P2=input("").lower()
    for item in playerlist:
      if item==P2P2:
        C2P2=1
        p2list.append(P2P2)
    replit.clear()
  while C3P2==0:
    ShowPlayers()
    print("Player 2 Who would you like to pick last")
    P2P3=input("").lower()
    for item in playerlist:
      if item==P2P3:
        C3P2=1
        p2list.append(P2P3)
    replit.clear()
  scene=1
while scene==1:
#setting stats player 1
  for item in plfs:
    if P1P1==item[8]:
      tend1=item[9]
      stats1=item
  for item in plfs:
    if P1P2==item[8]:
      tend2=item[9]
      stats2=item
  for item in plfs:
    if P1P3==item[8]:
      tend3=item[9]
      stats3=item
#setting stats player 2
  for item in plfs:
    if P2P1==item[8]:
      ttend1=item[9]
      tstats1=item
  for item in plfs:
    if P2P2==item[8]:
      ttend2=item[9]
      tstats2=item
  for item in plfs:
    if P2P3==item[8]:
      ttend3=item[9]
      tstats3=item
  cont=0
  while cont==0:
    print("Player 1 who do you want guarding",P2P1)
    muf1=input("")
    if muf1==P1P1:
      pdmuf1=stats1[5]
      dmuf1=stats1[6]
    if muf1==P1P2:
      pdmuf1=stats2[5]
      dmuf1=stats2[6]
    if muf1==P1P3:
      pdmuf1=stats3[5]
      dmuf1=stats3[6]
    for item in p1list:
      if muf1==item:
        p1list.remove(item)
        cont=1
  cont=0
  while cont==0:
    print("Player 1 who do you want guarding",P2P2)
    muf2=input("")
    if muf2==P1P1:
      pdmuf2=stats1[5]
      dmuf2=stats1[6]
    if muf2==P1P2:
      pdmuf2=stats2[5]
      dmuf2=stats2[6]
    if muf2==P1P3:
      pdmuf2=stats3[5]
      dmuf2=stats3[6]
    for item in p1list:
      if muf2==item:
        p1list.remove(item)
        cont=1
  cont=0
  while cont==0:
    print("Player 1 who do you want guarding",P2P3)
    muf3=input("")
    if muf3==P1P1:
      pdmuf3=stats1[5]
      dmuf3=stats1[6]
    if muf3==P1P2:
      pdmuf3=stats2[5]
      dmuf3=stats2[6]
    if muf3==P1P3:
      pdmuf3=stats3[5]
      dmuf3=stats3[6]
    for item in p1list:
      if muf3==item:
        p1list.remove(item)
        cont=1
  cont=0
  while cont==0:
    print("Player 2 who do you want guarding",P1P1)
    tmuf1=input("")
    if tmuf1==P2P1:
      ptdmuf1=tstats1[5]
      tdmuf1=tstats1[6]
    if tmuf1==P2P2:
      ptdmuf1=tstats2[5]
      tdmuf1=tstats2[6]
    if tmuf1==P2P3:
      ptdmuf1=tstats3[5]
      tdmuf1=tstats3[6]
    for item in p2list:
      if tmuf1==item:
        p2list.remove(item)
        cont=1
  cont=0
  while cont==0:
    print("Player 2 who do you want guarding",P1P2)
    tmuf2=input("")
    if tmuf2==P2P1:
      ptdmuf2=tstats1[5]
      tdmuf2=tstats1[6]
    if tmuf2==P2P2:
      ptdmuf2=tstats2[5]
      tdmuf2=tstats2[6]
    if tmuf2==P2P3:
      ptdmuf2=tstats3[5]
      tdmuf2=tstats3[6]
    for item in p2list:
      if tmuf2==item:
        p2list.remove(item)
        cont=1
  cont=0
  while cont==0:
    print("Player 2 who do you want guarding",P1P3)
    tmuf3=input("")
    if tmuf3==P2P1:
      ptdmuf3=tstats1[5]
      tdmuf3=tstats1[6]
    if tmuf3==P2P2:
      ptdmuf3=tstats2[5]
      tdmuf3=tstats2[6]
    if tmuf3==P2P3:
      ptdmuf3=tstats3[5]
      tdmuf3=tstats3[6]
    for item in p2list:
      if tmuf3==item:
        p2list.remove(item)
        cont=1
      
  replit.clear()
  scene=2
  
  
while scene==2:
  wt=int(input("Enter a reading speed[seconds]"))
  replit.clear()
  fs=int(input("What score will you play to?[2s and 3s]"))
  replit.clear()
  pos=random.randint(1,1)
  while score1<fs and score2<fs:
    if pos==1:
      showScore()
      ws=random.randint(1,3)
      if ws==1:
        pp=tend1[0]*random.randint(0,100)
        tp=tend1[1]*random.randint(0,100)
        sp=tend1[2]*random.randint(0,100)
        pup=tend1[3]*random.randint(0,100)
        d=tend1[4]*random.randint(0,100)
        php=tend1[5]*random.randint(0,100)
        pfp=tend1[6]*random.randint(0,100)
        bdp=tend1[7]*random.randint(0,100)
        wwc=[]
        wwc.append(pp)
        wwc.append(tp)
        wwc.append(sp)
        wwc.append(pup)
        wwc.append(d)
        wwc.append(php)
        wwc.append(pfp)
        wwc.append(bdp)
        wwc.sort()
        if wwc[7]==pp:
          rnfp=random.randint(1,2)
          if rnfp==1:
            print(P1P1,"passes to",P1P2)
            time.sleep(wt)
            ws=2
          if rnfp==2:
            print(P1P1,"passes to",P1P3)
            time.sleep(wt)
            ws=3
        if wwc[7]==tp:
          print("Turnover")
          time.sleep(wt)
          pos=2
        if wwc[7]==sp:
          print(P1P1,"shoots over",tmuf1)
          time.sleep(wt)
          if stats1[0]*random.randint(0,90)>ptdmuf1*random.randint(20,100):
            print(P1P1,"for three")
            fga1=fga1+1
            fgm1=fgm1+1
            time.sleep(wt)
            replit.clear()
            score1=score1+3
            ps1=ps1+3
            pos=2
          else:
            fga1=fga1+1
            print("No good")
            time.sleep(wt)
            replit.clear()
            pos=2
          
        if wwc[7]==pup:
          
          print(P1P1,"pulls up over",tmuf1)
          time.sleep(wt)
          if stats1[0]*random.randint(0,90)>ptdmuf1*random.randint(20,100):
            print(P1P1,"good for two")
            fga1=fga1+1
            fgm1=fgm1+1
            time.sleep(wt)
            replit.clear()
            ps1=ps1+2
            score1=score1+2
            pos=2
          else:
            wdtbg=random.randint(1,4)
            if wdtbg==1:
              print("It rims in and out")
              fga1=fga1+1
            if wdtbg==2:
              print("Just a bit too hard")
              fga1=fga1+1
            if wdtbg==3:
              print("Its short")
              
            if wdtbg==4:
              fga1=fga1+1
              print("Oh its blocked by",tmuf1)
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==d:
          print(P1P1,"drives on",tmuf1)
          time.sleep(wt)
          if stats1[1]*random.randint(0,90)>tdmuf1*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P1P1,"with a beautiful finish at the rim")
              fga1=fga1+1
              fgm1=fgm1+1
            if wdtbg==2:
              print(tmuf1,"didnt stand a chance")
              print("Great move by",P1P1)
              fga1=fga1+1
              fgm1=fgm1+1
            if wdtbg==3:
              print(P1P1,"accelerates to the basket and finishes")
              fga1=fga1+1
              fgm1=fgm1+1
            time.sleep(wt)
            replit.clear()
            ps1=ps1+2
            score1=score1+2
            pos=2
          else:
            fga1=fga1+1
            print(P1P1,"cant finish")
            print("Great defense by",tmuf1)
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==php:
          print(P1P1,"is gonna try the post hook over",tmuf1)
          time.sleep(wt)
          if stats1[2]*random.randint(0,90)>tdmuf1*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              fga1=fga1+1
              fgm1=fgm1+1
              print(P1P1,"converts the hook")
            if wdtbg==2:
              fga1=fga1+1
              fgm1=fgm1+1
              print(tmuf1,"just cant reach the ball on that beautiful hook")
              print("Great move by",P1P1)
            if wdtbg==3:
              fga1=fga1+1
              fgm1=fgm1+1
              print(P1P1,"makes the hook look effortless, good for two")
            time.sleep(wt)
            replit.clear()
            ps1=ps1+2
            score1=score1+2
            pos=2
          else:
            fga1=fga1+1
            print(P1P1,"cant get the post hook to go")
            print(tmuf1,"way to stay in front of it")
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==pfp:
          frn=random.randint(1,3)
          if frn==1:
            print(P1P1,"is gonna try the post fade over",tmuf1)
            time.sleep(wt)
          if frn==2:
            print(P1P1,"sets up a fade on ",tmuf1)
            time.sleep(wt)
          if frn==3:
            print(P1P1,"with the fadeaway")
            time.sleep(wt)
          
          if stats1[3]*random.randint(0,90)>ptdmuf2*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P1P1,"converts the fade")
              fga1=fga1+1
              fgm1=fgm1+1
            if wdtbg==2:
              print("Wow",P1P1,"right over",tmuf1,"and in")
              fga1=fga1+1
              fgm1=fgm1+1
              print("Great move by",P1P1)
            if wdtbg==3:
              print(P1P1,"smooth fade for 2")
              fga1=fga1+1
              fgm1=fgm1+1
            time.sleep(wt)
            replit.clear()
            ps1=ps1+2
            score1=score1+2
            pos=2
          else:
            print(P1P1,"cant get the fade in")
            print(tmuf1,"with the impressive defense")
            fga1=fga1+1
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==bdp:
          frn=random.randint(1,3)
          if frn==1:
            print(P1P1,"tryna play bully ball taking",tmuf1,"down low")
            time.sleep(wt)
          if frn==2:
            print("Here we go",P1P1,"backing down",tmuf1)
            time.sleep(wt)
          if frn==3:
            print(P1P1,"backing down",tmuf1)
            time.sleep(wt)
          if stats1[4]*random.randint(0,90)>tdmuf1*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              fga1=fga1+1
              fgm1=fgm1+1
              print(P1P1,"with the BIG-MAN finish")
              print("Making",tmuf1,"look like a little boy")
            if wdtbg==2:
              fga1=fga1+1
              fgm1=fgm1+1
              print(P1P1,"making it look easy with the strong finish")
            if wdtbg==3:
              fga1=fga1+1
              fgm1=fgm1+1
              print("Wow",P1P1,"thats a big man finish throwing it down with two hands!")
            time.sleep(wt)
            replit.clear()
            score1=score1+2
            ps1=ps1+2
            pos=2
          else:
            fga1=fga1+1
            print("Great defense by",tmuf1)
            print(P1P1,"unable to convert")
            time.sleep(wt)
            replit.clear()
            pos=2
        
      if ws==2:
        pp=tend2[0]*random.randint(0,100)
        tp=tend2[1]*random.randint(0,100)
        sp=tend2[2]*random.randint(0,100)
        pup=tend2[3]*random.randint(0,100)
        d=tend2[4]*random.randint(0,100)
        php=tend2[5]*random.randint(0,100)
        pfp=tend2[6]*random.randint(0,100)
        bdp=tend2[7]*random.randint(0,100)
        wwc=[]
        wwc.append(pp)
        wwc.append(tp)
        wwc.append(sp)
        wwc.append(pup)
        wwc.append(d)
        wwc.append(php)
        wwc.append(pfp)
        wwc.append(bdp)
        wwc.sort()
        if wwc[7]==pp:
          rnfp=random.randint(1,2)
          if rnfp==1:
            print(P1P2,"passes to",P1P1)
            time.sleep(wt)
            replit.clear()
            ws=1
          if rnfp==2:
            print(P1P2,"passes to",P1P3)
            time.sleep(wt)
            replit.clear()
            ws=3
        if wwc[7]==tp:
          print("Turnover")
          time.sleep(wt)
          replit.clear()
          pos=2
        if wwc[7]==sp:
          print(P1P2,"shoots over",tmuf2)
          time.sleep(wt)
          if stats2[0]*random.randint(0,90)>ptdmuf2*random.randint(20,100):
            print(P1P2,"for three")
            time.sleep(wt)
            replit.clear()
            score1=score1+3
            ps2=ps2+3
            fga2=fga2+1
            fgm2=fgm2+1
            pos=2
          else:
            fga2=fga2+1
            print("No good")
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==pup:
          print(P1P2,"pulls up over",tmuf2)
          time.sleep(wt)
          if stats2[0]*random.randint(0,90)>ptdmuf2*random.randint(20,100):
            print(P1P2,"good for two")
            fga2=fga2+1
            fgm2=fgm2+1
            time.sleep(wt)
            replit.clear()
            ps2=ps2+2
            score1=score1+2
            pos=2
          else:
            wdtbg=random.randint(1,4)
            if wdtbg==1:
              print("It rims in and out")
              fga2=fga2+1
            if wdtbg==2:
              print("Just a bit too hard")
              fga2=fga2+1
            if wdtbg==3:
              print("Its short")
              fga2=fga2+1
            if wdtbg==4:
              print("Oh its blocked by",tmuf2)
              fga2=fga2+1
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==d:
          print(P1P2,"drives on",tmuf2)
          time.sleep(wt)
          if stats2[1]*random.randint(0,90)>tdmuf2*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P1P2,"with a beautiful finish at the rim")
              fga2=fga2+1
              fgm2=fgm2+1
            if wdtbg==2:
              print(tmuf2,"didnt stand a chance")
              print("Great move by",P1P2)
              fga2=fga2+1
              fgm2=fgm2+1
            if wdtbg==3:
              print(P1P2,"accelerates to the basket and finishes")
              fga2=fga2+1
              fgm2=fgm2+1
            time.sleep(wt)
            replit.clear()
            ps2=ps2+2
            score1=score1+2
            pos=2
          else:
            fga2=fga2+1
            print(P1P2,"cant finish")
            print("Great defense by",tmuf2)
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==php:
          print(P1P2,"is gonna try the post hook over",tmuf2)
          time.sleep(wt)
          if stats2[2]*random.randint(0,90)>tdmuf2*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              fga2=fga2+1
              fgm2=fgm2+1
              print(P1P2,"converts the hook")
            if wdtbg==2:
              fga2=fga2+1
              fgm2=fgm2+1
              print(tmuf2,"just cant reach the ball on that beautiful hook")
              print("Great move by",P1P2)
            if wdtbg==3:
              fga2=fga2+1
              fgm2=fgm2+1
              print(P1P2,"makes the hook look effortless")
            time.sleep(wt)
            replit.clear()
            ps2=ps2+2
            score1=score1+2
            pos=2
          else:
            fga2=fga2+1
            print(P1P2,"cant get the post hook to go")
            print(tmuf2,"way to stay in front of it")
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==pfp:
          frn=random.randint(1,3)
          if frn==1:
            print(P1P2,"is gonna try the post fade over",tmuf2)
            time.sleep(wt)
          if frn==2:
            print(P1P2,"sets up a fade on ",tmuf2)
            time.sleep(wt)
          if frn==3:
            print(P1P2,"with the fadeaway")
            time.sleep(wt)
          
          if stats2[3]*random.randint(0,90)>ptdmuf2*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              fga2=fga2+1
              fgm2=fgm2+1
              print(P1P2,"converts the fade")
            if wdtbg==2:
              fga2=fga2+1
              fgm2=fgm2+1
              print("Wow",P1P2,"right over",tmuf2,"and in")
              print("Great move by",P1P2)
            if wdtbg==3:
              fga2=fga2+1
              fgm2=fgm2+1
              print(P1P2,"smooth fade for 2")
            time.sleep(wt)
            replit.clear()
            ps2=ps2+2
            score1=score1+2
            pos=2
          else:
            fga2=fga2+1
            print(P1P2,"cant get the fade in")
            print(tmuf2,"with the impressive defense")
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==bdp:
          frn=random.randint(1,3)
          if frn==1:
            print(P1P2,"tryna play bully ball taking",tmuf2,"down low")
            time.sleep(wt)
          if frn==2:
            print("Here we go",P1P2,"backing down",tmuf2)
            time.sleep(wt)
          if frn==3:
            print(P1P2,"backing down",tmuf2)
            time.sleep(wt)
          
          if stats2[4]*random.randint(0,90)>tdmuf2*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              fga2=fga2+1
              fgm2=fgm2+1
              print(P1P2,"with the BIG-MAN finish")
              time.sleep(wt/2)
              print("Making",tmuf2,"look like a little boy")
              
            if wdtbg==2:
              fga2=fga2+1
              fgm2=fgm2+1
              print(P1P2,"making it look easy with the strong finish")
              
            if wdtbg==3:
              fga2=fga2+1
              fgm2=fgm2+1
              print("Wow",P1P2,"thats a big man finish throwing it down with two hands!")
              
            time.sleep(wt)
            replit.clear()
            ps2=ps2+2
            score1=score1+2
            pos=2
          else:
            fga2=fga2+1
            print("Great defense by",tmuf2)
            print(P1P2,"unable to convert")
            time.sleep(wt)
            replit.clear()
            pos=2
            
      if ws==3:
        pp=tend3[0]*random.randint(0,100)
        tp=tend3[1]*random.randint(0,100)
        sp=tend3[2]*random.randint(0,100)
        pup=tend3[3]*random.randint(0,100)
        d=tend3[4]*random.randint(0,100)
        php=tend3[5]*random.randint(0,100)
        pfp=tend3[6]*random.randint(0,100)
        bdp=tend3[7]*random.randint(0,100)
        wwc=[]
        wwc.append(pp)
        wwc.append(tp)
        wwc.append(sp)
        wwc.append(pup)
        wwc.append(d)
        wwc.append(php)
        wwc.append(pfp)
        wwc.append(bdp)
        wwc.sort()
        if wwc[7]==pp:
          rnfp=random.randint(1,2)
          if rnfp==1:
            print(P1P3,"passes to",P1P1)
            time.sleep(wt)
            replit.clear()
            ws=1
          if rnfp==2:
            print(P1P3,"passes to",P1P2)
            time.sleep(wt)
            replit.clear()
            ws=2
        if wwc[7]==tp:
          print("Turnover")
          time.sleep(wt)
          replit.clear()
          pos=2
        if wwc[7]==sp:
          print(P1P3,"shoots over",tmuf3)
          time.sleep(wt)
          if stats3[0]*random.randint(0,90)>ptdmuf3*random.randint(20,100):
            print(P1P3,"for three")
            fga3=fga3+1
            fgm3=fgm3+1
            time.sleep(wt)
            replit.clear()
            score1=score1+3
            ps3=ps3+3
            pos=2
          else:
            fga3=fga3+1
            print("No good")
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==pup:
          
          print(P1P3,"pulls up over",tmuf3)
          time.sleep(wt)
          if stats3[0]*random.randint(0,90)>ptdmuf3*random.randint(20,100):
            print(P1P3,"good for two")
            fga3=fga3+1
            fgm3=fgm3+1
            time.sleep(wt)
            replit.clear()
            ps3=ps3+2
            score1=score1+2
            pos=2
          else:
            wdtbg=random.randint(1,4)
            if wdtbg==1:
              print("It rims in and out")
              fga3=fga3+1
            if wdtbg==2:
              fga3=fga3+1
              print("Just a bit too hard")
            if wdtbg==3:
              fga3=fga3+1
            
              print("Its short")
              fga3=fga3+1
            if wdtbg==4:
              fga3=fga3+1
              print("Oh its blocked by",tmuf3)
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==d:
          print(P1P3,"drives on",tmuf3)
          time.sleep(wt)
          if stats3[1]*random.randint(0,90)>tdmuf3*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              fga3=fga3+1
              fgm3=fgm3+1
              print(P1P3,"with a beautiful finish at the rim")
            if wdtbg==2:
              fga3=fga3+1
              fgm3=fgm3+1
              print(tmuf3,"didnt stand a chance")
              print("Great move by",P1P3)
            if wdtbg==3:
              fga3=fga3+1
              fgm3=fgm3+1
              print(P1P3,"accelerates to the basket and finishes")
            time.sleep(wt)
            replit.clear()
            ps3=ps3+2
            score1=score1+2
            pos=2
          else:
            fga3=fga3+1
            print(P1P3,"cant finish")
            print("Great defense by",tmuf3)
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==php:
          print(P1P3,"is gonna try the post hook over",tmuf3)
          time.sleep(wt)
          if stats3[2]*random.randint(0,90)>tdmuf3*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P1P3,"converts the hook")
              fga3=fga3+1
              fgm3=fgm3+1
            if wdtbg==2:
              print(tmuf3,"just cant reach the ball on that beautiful hook")
              print("Great move by",P1P3)
              fga3=fga3+1
              fgm3=fgm3+1
            if wdtbg==3:
              print(P1P3,"makes the hook look effortless")
              fga3=fga3+1
              fgm3=fgm3+1
            time.sleep(wt)
            replit.clear()
            ps3=ps3+2
            score1=score1+2
            pos=2
          else:
            fga3=fga3+1
            print(P1P3,"cant get the post hook to go")
            print(tmuf3,"way to stay in front of it")
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==pfp:
          frn=random.randint(1,3)
          if frn==1:
            print(P1P3,"is gonna try the post fade over",tmuf3)
            time.sleep(wt)

          if frn==2:
            print(P1P3,"sets up a fade on ",tmuf3)
            time.sleep(wt)
          if frn==3:
            print(P1P3,"with the fadeaway")
            time.sleep(wt)
          if stats3[3]*random.randint(0,90)>ptdmuf3*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              fga3=fga3+1
              fgm3=fgm3+1
              print(P1P3,"converts the fade")
            if wdtbg==2:
              fga3=fga3+1
              fgm3=fgm3+1
              print("Wow",P1P3,"right over",tmuf3,"and in")
              print("Great move by",P1P3)
            if wdtbg==3:
              fga3=fga3+1
              fgm3=fgm3+1
              print(P1P3,"smooth fade for 2")
            time.sleep(wt)
            replit.clear()
            ps3=ps3+2
            score1=score1+2
            pos=2
          else:
            fga3=fga3+1
            print(P1P3,"cant get the fade in")
            print(tmuf3,"with the impressive defense")
            time.sleep(wt)
            replit.clear()
            pos=2
        if wwc[7]==bdp:
          frn=random.randint(1,3)
          if frn==1:
            print(P1P3,"tryna play bully ball taking",tmuf3,"down low")
            time.sleep(wt)
          if frn==2:
            print("Here we go",P1P3,"backing down",tmuf3)
            time.sleep(wt)
          if frn==3:
            print(P1P3,"backing down",tmuf3)
            time.sleep(wt)
          if stats3[4]*random.randint(0,90)>tdmuf3*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              fga3=fga3+1
              fgm3=fgm3+1
              print(P1P3,"with the BIG-MAN finish")
              print("Making",tmuf3,"look like a little boy")
            if wdtbg==2:
              fga3=fga3+1
              fgm3=fgm3+1
              print(P1P3,"making it look easy with the strong finish")
            if wdtbg==3:
              fga3=fga3+1
              fgm3=fgm3+1
              print("Wow",P1P3,"thats a big man finish throwing it down with two hands!")
            time.sleep(wt)
            replit.clear()
            ps3=ps3+2
            score1=score1+2
            pos=2
          else:
            fga3=fga3+1
            print("Great defense by",tmuf3)
            print(P1P3,"unable to convert")
            time.sleep(wt)
            replit.clear()
            pos=2
    #Possession 2
    if pos==2:
      showScore()
      ws=random.randint(1,3)
      if ws==1:
        pp=ttend1[0]*random.randint(0,100)
        tp=ttend1[1]*random.randint(0,100)
        sp=ttend1[2]*random.randint(0,100)
        pup=ttend1[3]*random.randint(0,100)
        d=ttend1[4]*random.randint(0,100)
        php=ttend1[5]*random.randint(0,100)
        pfp=ttend1[6]*random.randint(0,100)
        bdp=ttend1[7]*random.randint(0,100)
        wwc=[]
        wwc.append(pp)
        wwc.append(tp)
        wwc.append(sp)
        wwc.append(pup)
        wwc.append(d)
        wwc.append(php)
        wwc.append(pfp)
        wwc.append(bdp)
        wwc.sort()
        if wwc[7]==pp:
          rnfp=random.randint(1,2)
          if rnfp==1:
            print(P2P1,"passes to",P2P2)
            time.sleep(wt)
            ws=2
          if rnfp==2:
            print(P2P1,"passes to",P2P3)
            time.sleep(wt)
            ws=3
        if wwc[7]==tp:
          print("Turnover")
          time.sleep(wt)
          pos=1
        if wwc[7]==sp:
          print(P2P1,"shoots over",muf1)
          time.sleep(wt)
          if tstats1[0]*random.randint(0,90)>dmuf1*random.randint(20,100):
            print(P2P1,"for three")
            tfgm1=tfgm1+1
            tfga1=tfga1+1
            time.sleep(wt)
            replit.clear()
            score2=score2+3
            tps1=tps1+3
            pos=1
          else:
            tfga1=tfga1+1
            print("No good")
            time.sleep(wt)
            replit.clear()
            pos=1
          
        if wwc[7]==pup:
          print(P2P1,"pulls up over",muf1)
          time.sleep(wt)
          if tstats1[0]*random.randint(0,90)>pdmuf1*random.randint(20,100):
            print(P2P1,"good for two")
            tfgm1=tfgm1+1
            tfga1=tfga1+1
            time.sleep(wt)
            replit.clear()
            tps1=tps1+2
            score2=score2+2
            pos=1
          else:
            wdtbg=random.randint(1,4)
            if wdtbg==1:
              print("It rims in and out")
              tfga1=tfga1+1
            if wdtbg==2:
              tfga1=tfga1+1
              print("Just a bit too hard")
              
            if wdtbg==3:
              tfga1=tfga1+1
              print("Its short")
              
            if wdtbg==4:
              tfga1=tfga1+1
              print("Oh its blocked by",muf1)
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==d:
          print(P2P1,"drives on",muf1)
          time.sleep(wt)
          if tstats1[1]*random.randint(0,90)>dmuf1*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P2P1,"with a beautiful finish at the rim")
              tfgm1=tfgm1+1
              tfga1=tfga1+1
            if wdtbg==2:
              print(muf1,"didnt stand a chance")
              print("Great move by",P2P1)
              tfgm1=tfgm1+1
            tfga1=tfga1+1
            if wdtbg==3:
              print(P2P1,"accelerates to the basket and finishes")
              tfgm1=tfgm1+1
              tfga1=tfga1+1
            time.sleep(wt)
            replit.clear()
            tps1=tps1+2
            score2=score2+2
            pos=1
          else:
            tfga1=tfga1+1
            print(P2P1,"cant finish")
            print("Great defense by",muf1)
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==php:
          print(P2P1,"is gonna try the post hook over",muf1)
          time.sleep(wt)
          if tstats1[2]*random.randint(0,90)>dmuf1*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P2P1,"converts the hook")
              tfgm1=tfgm1+1
              tfga1=tfga1+1
            if wdtbg==2:
              print(muf1,"just cant reach the ball on that beautiful hook")
              tfgm1=tfgm1+1
              tfga1=tfga1+1
              print("Great move by",P2P1)
            if wdtbg==3:
              print(P2P1,"makes the hook look effortless")
              tfgm1=tfgm1+1
              tfga1=tfga1+1
            time.sleep(wt)
            replit.clear()
            tps1=tps1+2
            score2=score2+2
            pos=1
          else:
            
            tfga1=tfga1+1
            print(P2P1,"cant get the post hook to go")
            print(muf1,"way to stay in front of it")
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==bdp:
          frn=random.randint(1,3)
          if frn==1:
            print(P2P1,"tryna play bully ball taking",muf1,"down low")
            time.sleep(wt)
          if frn==2:
            print("Here we go",P2P1,"backing down",muf1)
            time.sleep(wt)
          if frn==3:
            print(P2P1,"backing down",muf1)
            time.sleep(wt)
          if tstats1[4]*random.randint(0,90)>pdmuf1*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              tfgm1=tfgm1+1
              tfga1=tfga1+1
              print(P2P1,"with the BIG-MAN finish")
              print("Making",muf1,"look like a little boy")
            if wdtbg==2:
              tfgm1=tfgm1+1
              tfga1=tfga1+1
              print(P2P1,"making it look easy with the strong finish")
            if wdtbg==3:
              tfgm1=tfgm1+1
              tfga1=tfga1+1
              print("Wow",P2P1,"thats a big man finish throwing it down with two hands!")
            time.sleep(wt)
            replit.clear()
            tps1=tps1+2
            score2=score2+2
            pos=1
          else:
            tfga1=tfga1+1
            print("Great defense by",muf1)
            print(P2P1,"unable to convert")
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==pfp:
          print(P2P1,"is gonna try the fade")
          time.sleep(wt)
          if tstats1[3]*random.randint(0,90)>pdmuf1*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              tfgm1=tfgm1+1
              tfga1=tfga1+1
              print(P2P1,"with a beautiful fade right over",muf1)
            if wdtbg==2:
              tfgm1=tfgm1+1
              tfga1=tfga1+1
              print(muf1,"didnt stand a chance")
              print("Great move by",P2P1)
            if wdtbg==3:
              tfgm1=tfgm1+1
              tfga1=tfga1+1
              print(P2P1,"beatiful move and shot on the fade")
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps1=tps1+2
            pos=1
          else:
            tfga1=tfga1+1
            print(P2P1,"cant hit the fade")
            print("Great defense by",muf1)
            time.sleep(wt)
            replit.clear()
            pos=1
      if ws==2:
        pp=ttend2[0]*random.randint(0,100)
        tp=ttend2[1]*random.randint(0,100)
        sp=ttend2[2]*random.randint(0,100)
        pup=ttend2[3]*random.randint(0,100)
        d=ttend2[4]*random.randint(0,100)
        php=ttend2[5]*random.randint(0,100)
        pfp=ttend2[6]*random.randint(0,100)
        bdp=ttend2[7]*random.randint(0,100)
        wwc=[]
        wwc.append(pp)
        wwc.append(tp)
        wwc.append(sp)
        wwc.append(pup)
        wwc.append(d)
        wwc.append(php)
        wwc.append(pfp)
        wwc.append(bdp)
        wwc.sort()
        if wwc[7]==pp:
          rnfp=random.randint(1,2)
          if rnfp==1:
            print(P2P2,"passes to",P2P1)
            time.sleep(wt)
            replit.clear()
            ws=1
          if rnfp==2:
            print(P2P2,"passes to",P2P3)
            time.sleep(wt)
            replit.clear()
            ws=3
        if wwc[7]==tp:
          print("Turnover")
          time.sleep(wt)
          replit.clear()
          pos=1
        if wwc[7]==sp:
          print(P2P2,"shoots over",muf2)
          time.sleep(wt)
          if tstats2[0]*random.randint(0,90)>pdmuf2*random.randint(20,100):
            print(P2P2,"for three")
            tfga2=tfga2+1
            tfgm2=tfgm2+1
            time.sleep(wt)
            replit.clear()
            score2=score2+3
            tps2=tps2+3
            pos=1
          else:
            tfga2=tfga2+1
            print("No good")
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==pup:
          print(P2P2,"pulls up over",muf2)
          time.sleep(wt)
          if tstats2[0]*random.randint(0,90)>pdmuf2*random.randint(20,100):
            print(P2P2,"good for two")
            tfga2=tfga2+1
            tfgm2=tfgm2+1
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps2=tps2+2
            pos=1
          else:
            wdtbg=random.randint(1,4)
            if wdtbg==1:
              print("It rims in and out")
              tfga2=tfga2+1
            if wdtbg==2:
              print("Just a bit too hard")
              tfga2=tfga2+1
            if wdtbg==3:
              print("Its short")
              tfga2=tfga2+1
            if wdtbg==4:
              print("Oh its blocked by",muf2)
              tfga2=tfga2+1
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==d:
          print(P2P2,"drives on",muf2)
          time.sleep(wt)
          if tstats2[1]*random.randint(0,90)>dmuf2*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P2P2,"with a beautiful finish at the rim")
              tfga2=tfga2+1
              tfgm2=tfgm2+1
            if wdtbg==2:
              print(muf2,"didnt stand a chance")
              print("Great move by",P2P2)
              tfga2=tfga2+1
              tfgm2=tfgm2+1
            if wdtbg==3:
              print(P2P2,"accelerates to the basket and finishes")
              tfga2=tfga2+1
              tfgm2=tfgm2+1
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps2=tps2+2
            pos=1
          else:
            tfga2=tfga2+1
            print(P2P2,"cant finish")
            print("Great defense by",muf2)
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==php:
          print(P2P2,"is gonna try the post hook over",tmuf2)
          time.sleep(wt)
          if tstats2[2]*random.randint(0,90)>dmuf2*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P2P2,"converts the hook")
              tfga2=tfga2+1
              tfgm2=tfgm2+1
            if wdtbg==2:
              print(muf2,"just cant reach the ball on that beautiful hook")
              tfga2=tfga2+1
              tfgm2=tfgm2+1
              print("Great move by",P2P2)
            if wdtbg==3:
              tfga2=tfga2+1
              tfgm2=tfgm2+1
              print(P2P2,"makes the hook look effortless")
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps2=tps2+2
            pos=1
          else:
            tfga2=tfga2+1
            print(P2P2,"cant get the post hook to go")
            print(muf2,"way to stay in front of it")
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==pfp:
          frn=random.randint(1,3)
          if frn==1:

            print(P2P2,"is gonna try the post fade over",muf2)
            time.sleep(wt)
          if frn==2:
            print(P2P2,"sets up a fade on ",muf2)
            time.sleep(wt)
          if frn==3:
            print(P2P2,"with the fadeaway")
            time.sleep(wt)
          
          if tstats2[3]*random.randint(0,90)>pdmuf2*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P2P2,"converts the fade")
              tfga2=tfga2+1
              tfgm2=tfgm2+1
            if wdtbg==2:
              tfga2=tfga2+1
              tfgm2=tfgm2+1
              print("Wow",P2P2,"right over",muf2,"and in")
              print("Great move by",P2P2)
            if wdtbg==3:
              tfga2=tfga2+1
              tfgm2=tfgm2+1
              print(P2P2,"smooth fade for 2")
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps2=tps2+2
            pos=1
          else:
            tfga2=tfga2+1
            print(P2P2,"cant get the fade in")
            print(muf2,"with the impressive defense")
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==bdp:
          frn=random.randint(1,3)
          if frn==1:
            print(P2P2,"tryna play bully ball taking",muf2,"down low")
            time.sleep(wt)
          if frn==2:
            print("Here we go",P2P2,"backing down",muf2)
            time.sleep(wt)
          if frn==3:
            print(P2P2,"backing down",muf2)
            time.sleep(wt)
          
          if tstats2[4]*random.randint(0,90)>dmuf2*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              tfga2=tfga2+1
              tfgm2=tfgm2+1
              print(P2P2,"with the BIG-MAN finish")
              time.sleep(wt/2)
              print("Making",muf2,"look like a little boy")
              
            if wdtbg==2:
              tfga2=tfga2+1
              tfgm2=tfgm2+1
              print(P2P2,"making it look easy with the strong finish")
              
            if wdtbg==3:
              tfga2=tfga2+1
              tfgm2=tfgm2+1
              print("Wow",P2P2,"thats a big man finish throwing it down with two hands!")
              
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps2=tps2+2
            pos=1
          else:
            tfga2=tfga2+1
            print("Great defense by",muf2)
            print(P2P2,"unable to convert")
            time.sleep(wt)
            replit.clear()
            pos=1
            
      if ws==3:
        pp=ttend3[0]*random.randint(0,100)
        tp=ttend3[1]*random.randint(0,100)
        sp=ttend3[2]*random.randint(0,100)
        pup=ttend3[3]*random.randint(0,100)
        d=ttend3[4]*random.randint(0,100)
        php=ttend3[5]*random.randint(0,100)
        pfp=ttend3[6]*random.randint(0,100)
        bdp=ttend3[7]*random.randint(0,100)
        wwc=[]
        wwc.append(pp)
        wwc.append(tp)
        wwc.append(sp)
        wwc.append(pup)
        wwc.append(d)
        wwc.append(php)
        wwc.append(pfp)
        wwc.append(bdp)
        wwc.sort()
        if wwc[7]==pp:
          rnfp=random.randint(1,2)
          if rnfp==1:
            print(P2P3,"passes to",P2P1)
            time.sleep(wt)
            replit.clear()
            ws=1
          if rnfp==2:
            print(P2P3,"passes to",P2P2)
            time.sleep(wt)
            replit.clear()
            ws=2
        if wwc[7]==tp:
          print("Turnover")
          time.sleep(wt)
          replit.clear()
          pos=1
        if wwc[7]==sp:
          print(P2P3,"shoots over",muf3)
          time.sleep(wt)
          if tstats3[0]*random.randint(0,90)>pdmuf3*random.randint(20,100):
            print(P2P3,"for three")
            tfga3=tfga3+1
            tfgm3=tfgm3+1
            time.sleep(wt)
            replit.clear()
            score2=score2+3
            tps3=tps3+3
            pos=1
          else:
            print("No good")
            tfga3=tfga3+1
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==pup:
          
          print(P2P3,"pulls up over",muf3)
          time.sleep(wt)
          if tstats3[0]*random.randint(0,90)>pdmuf3*random.randint(20,100):
            print(P2P3,"good for two")
            tfga3=tfga3+1
            tfgm3=tfgm3+1
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps3=tps3+2
            pos=1
          else:
            wdtbg=random.randint(1,4)
            if wdtbg==1:
              print("It rims in and out")
              tfga3=tfga3+1
            if wdtbg==2:
              print("Just a bit too hard")
              tfga3=tfga3+1
            if wdtbg==3:
              print("Its short")
              tfga3=tfga3+1
            
            if wdtbg==4:
              tfga3=tfga3+1
            
              print("Oh its blocked by",muf3)
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==d:
          print(P2P3,"drives on",muf3)
          time.sleep(wt)
          if tstats3[1]*random.randint(0,90)>dmuf3*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P2P3,"with a beautiful finish at the rim")
              tfga3=tfga3+1
              tfgm3=tfgm3+1
            if wdtbg==2:
              tfga3=tfga3+1
              tfgm3=tfgm3+1
              print(muf3,"didnt stand a chance")
              print("Great move by",P2P3)
            if wdtbg==3:
              tfga3=tfga3+1
              tfgm3=tfgm3+1
              print(P2P3,"accelerates to the basket and finishes")
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps3=tps3+2
            pos=1
          else:
            tfga3=tfga3+1
            print(P2P3,"cant finish")
            print("Great defense by",muf3)
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==php:
          print(P2P3,"is gonna try the post hook over",muf3)
          time.sleep(wt)
          if tstats3[2]*random.randint(0,90)>dmuf3*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              tfga3=tfga3+1
              tfgm3=tfgm3+1
              print(P2P3,"converts the hook")
            if wdtbg==2:
              tfga3=tfga3+1
              tfgm3=tfgm3+1
              print(muf3,"just cant reach the ball on that beautiful hook")
              print("Great move by",P2P3)
            if wdtbg==3:
              tfga3=tfga3+1
              tfgm3=tfgm3+1
              print(P2P3,"makes the hook look effortless")
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps3=tps3+2
            pos=1
          else:
            tga3=tfga3+1
            print(P2P3,"cant get the post hook to go")
            print(muf3,"way to stay in front of it")
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==pfp:
          frn=random.randint(1,3)
          if frn==1:
            print(P2P3,"is gonna try the post fade over",muf3)
            time.sleep(wt)

          if frn==2:
            print(P2P3,"sets up a fade on ",muf3)
            time.sleep(wt)
          if frn==3:
            print(P2P3,"with the fadeaway")
            time.sleep(wt)
          if tstats3[3]*random.randint(0,90)>pdmuf3*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              print(P2P3,"converts the fade")
              tfga3=tfga3+1
              tfgm3=tfgm3+1
            if wdtbg==2:
              print("Wow",P2P3,"right over",muf3,"and in")
              print("Great move by",P2P3)
              tfga3=tfga3+1
              tfgm3=tfgm3+1
            if wdtbg==3:
              print(P2P3,"smooth fade for 2")
              tfga3=tfga3+1
              tfgm3=tfgm3+1
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps3=tps3+2
            pos=1
          else:
            tfga3=tfga3+1
            print(P2P3,"cant get the fade in")
            print(muf3,"with the impressive defense")
            time.sleep(wt)
            replit.clear()
            pos=1
        if wwc[7]==bdp:
          frn=random.randint(1,3)
          if frn==1:
            print(P2P3,"tryna play bully ball taking",muf3,"down low")
            time.sleep(wt)
          if frn==2:
            print("Here we go",P2P3,"backing down",muf3)
            time.sleep(wt)
          if frn==3:
            print(P2P3,"backing down",muf3)
            time.sleep(wt)
          if tstats3[4]*random.randint(0,90)>dmuf3*random.randint(20,100):
            wdtbg=random.randint(1,3)
            if wdtbg==1:
              tfga3=tfga3+1
              tfgm3=tfgm3+1
              print(P2P3,"with the BIG-MAN finish")
              print("Making",muf3,"look like a little boy")
            if wdtbg==2:
              tfga3=tfga3+1
              tfgm3=tfgm3+1
              print(P2P3,"making it look easy with the strong finish")
            if wdtbg==3:
              tfga3=tfga3+1
              tfgm3=tfgm3+1
              print("Wow",P2P3,"thats a big man finish throwing it down with two hands!")
            time.sleep(wt)
            replit.clear()
            score2=score2+2
            tps3=tps3+2
            pos=1
          else:
            tfga3=tfga3+1
            print("Great defense by",muf3)
            print(P2P3,"unable to convert")
            time.sleep(wt)
            replit.clear()
            pos=1
  if score1>20 or score2>20:
    scene=3
while scene==3:
  print("Team1:")
  print(P1P1,"Points:",ps1,"FG%:",(fgm1/fga1)*100)
  print(P1P2,"Points:",ps2,"FG%:",(fgm2/fga2)*100)
  print(P1P3,"Points:",ps3,"FG%:",(fgm3/fga3)*100)
  print("")
  print("")
  print("")
  print("")
  print("Team2:")
  print(P2P1,"Points:",tps1,"FG%:",(tfgm1/tfga1)*100)
  print(P2P2,"Points:",tps2,"FG%:",(tfgm2/tfga2)*100)
  print(P2P3,"Points:",tps3,"FG%:",(tfgm3/tfga3)*100)
  if score1>score2:
    print("Team 1 Wins")
    mvps1=0
    mvps2=0
    mvps3=0
    mvpsl=[]
    mvps1=ps1*(fgm1/fga1)
    mvps2=ps2*(fgm2/fga2)
    mvps3=ps3*(fgm3/fga3)
    mvpsl.append(mvps1)
    mvpsl.append(mvps2)
    mvpsl.append(mvps3)
    mvpsl.sort()
    if mvpsl[2]==mvps1:
      print(P1P1,"is the MVP")
    if mvpsl[2]==mvps2:
      print(P1P2,"is the MVP")
    if mvpsl[2]==mvps3:
      print(P1P3,"is the MVP")
    pause=input("Say anything to continue")
    replit.clear()
    Menu()
    
  if score2>score1:
    print("Team 2 Wins")
    tmvps1=0
    tmvps2=0
    tmvps3=0
    tmvpsl=[]
    tmvps1=tps1*(tfgm1/tfga1)
    tmvps2=tps2*(tfgm2/tfga2)
    tmvps3=tps3*(tfgm3/tfga3)
    tmvpsl.append(tmvps1)
    tmvpsl.append(tmvps2)
    tmvpsl.append(tmvps3)
    tmvpsl.sort()
    if tmvpsl[2]==tmvps1:
      print(P2P1,"is the MVP")
    if tmvpsl[2]==tmvps2:
      print(P2P2,"is the MVP")
    if tmvpsl[2]==tmvps3:
      print(P2P3,"is the MVP")
    pause=input("Say anything to continue")
    replit.clear()
    Menu()
# Imports
# -----------------------------------------------------------
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import math

# Time
time = []
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
# offense eff lists
doea = []
doeb = []
# Defensive eff lists
ddea = []
ddeb = []
# Winning % List
dwp = []


t = 0
t_start = 0
t_end = 40
step = 1/60
n = int(round(t_end - t_start)/step)


# Offensive Efficiency
oea = 1
oeb = 1
# Defensive Effeciency
dea = 1
deb = 1
# Win Probability
wp = .5

doea.append(oea)
doeb.append(oeb)
ddea.append(dea)
ddeb.append(deb)
dwp.append(wp)
time.append(t)


t_offense = 30  # seconds
t_defense = 30  # seconds


# Offense A
offensive_possessionsa = 0
aa = [0]
assist_counta = 0
tna = [0]
turnover_counta = 0
shootinga = [0]
shooting_counta = 0
ora = [0]
ora_count = 0
orb = [0]
orb_count = 0
st_counta = 0
sta = []

# offense B
offensive_possessionsb = 0
ab = [0]
assist_countb = 0
tnb = [0]
turnover_countb = 0
shootingb = [0]
shooting_countb = 0
total = 0
score_a = 0
score_b = 0
st_countb = 0
stb = []


for i in range(n):

    # Offense A
    if ((i/30) % 2) == 0:
        total += 1
        time.append(total)
        offensive_possessionsa += 1

        # assist chance
        assist_floata = random.random()
        if assist_floata > 0.35:
            assist_counta = assist_counta
        else:
            assist_counta += 1
        assist_a = assist_counta/offensive_possessionsa
        aa.append(assist_a)

        # turnover
        turnover_floata = random.random()
        if turnover_floata > 0.12:
            turnover_counta = turnover_counta
        else:
            turnover_counta += 1
        turnover_a = turnover_counta / offensive_possessionsa
        tna.append(turnover_a)

        # shooting
        shooting_floata = random.random()
        if shooting_floata > 0.47:
            shooting_counta = shooting_counta
        else:
            shooting_counta += 1
            score_floata = random.random()
            if score_floata > .5:
                score_a += 2
            else:
                score_a += 3
        shooting_a = shooting_counta / offensive_possessionsa
        shootinga.append(shooting_a)

        # offensive rebounds
        or_floata = random.random()
        if or_floata > .2:
            ora_count = ora_count
        else:
            ora_count += 1
        offensive_a = ora_count / offensive_possessionsa
        ora.append(offensive_a)

        # steal
        st_floata = random.random()
        if st_floata > .15:
            st_counta = st_counta
        else:
            st_counta += 1
        st_a = st_counta / offensive_possessionsa
        sta.append(st_a)

    # Offense B
    if ((i/30) % 2) == 1:
        # total += 1
        # time.append(total)
        offensive_possessionsb += 1

        # assist chance
        assist_floatb = random.random()
        if assist_floatb > 0.35:
            assist_countb = assist_countb
        else:
            assist_countb += 1
        assist_b = assist_countb/offensive_possessionsb
        ab.append(assist_b)

        # turnover
        turnover_floatb = random.random()
        if turnover_floatb > 0.12:
            turnover_countb = turnover_countb
        else:
            turnover_countb += 1
        turnover_b = turnover_countb / offensive_possessionsb
        tna.append(turnover_b)

        # shooting
        shooting_floatb = random.random()
        if shooting_floatb > 0.47:
            shooting_countb = shooting_countb
        else:
            shooting_countb += 1
            score_floatb = random.random()
            if score_floatb > .5:
                score_b += 2
            else:
                score_b += 3
        shooting_b = shooting_countb / offensive_possessionsb
        shootingb.append(shooting_b)

        # offensive rebounds
        or_floatb = random.random()
        if or_floatb > .2:
            orb_count = orb_count
        else:
            orb_count += 1
        offensive_b = ora_count / offensive_possessionsb
        orb.append(offensive_b)

        # steal
        st_floatb = random.random()
        if st_floatb > .15:
            st_countb = st_countb
        else:
            st_countb += 1
        st_b = st_countb / offensive_possessionsb
        stb.append(st_b)

        s_effect = shooting_a - shooting_b

        a_effect = assist_a - assist_b

        t_effect = turnover_a - turnover_b

        or_effect = offensive_a - offensive_b

        dr_effect = (1-offensive_b) - (1-offensive_a)

        st_effect = st_a - st_b

        doea_dt = (s_effect+a_effect+or_effect-t_effect) * \
            oea - ((oea-1.15)/.2)*.3
        ddea_dt = (s_effect + st_effect - t_effect +
                   dr_effect) - ((dea-1.15)/.2)*.3

        oea = doea_dt*step + oea
        dea = ddea_dt*step + dea
        doea.append(oea)
        ddea.append(dea)


plt.plot(time, doea, label='Offensive Efficiency Differnce')
plt.xlabel('Time (Minutes)')
plt.ylabel('Offensive Efficiency Difference')
plt.title('Off Eff Dif')
plt.legend()
plt.show()

plt.plot(time, ddea, label='Offensive Efficiency Differnce')
plt.xlabel('Time (Minutes)')
plt.ylabel('Offensive Efficiency Difference')
plt.title('Off Eff Dif')
plt.legend()
plt.show()

# Imports
# -----------------------------------------------------------
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import math


time = []
doea = []
doeb = []
ddea = []
ddeb = []
dwp = []
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

t = 0
t_start = 0
t_end = 40
step = 1/60
n = int(round(t_end - t_start)/step)


# Offensive Efficiency
oea = 1.5
oeb = 1.4
# Defensive Effeciency
dea = 1.5
deb = 1.3
# Win Probability
wp = .5

doea.append(oea)
doeb.append(oeb)
ddea.append(dea)
ddeb.append(deb)
dwp.append(wp)
time.append(t)

offense = 30  # seconds
defense = 30  # seconds
switch_list = []
sw = 0


for i in range(int(offense/step)):
    switch_list.append(round(sw, 4))
    if i < .5 * (offense/step):
        sw += 1*step
        if sw > 1:
            sw = 1
    if i > .5 * (offense/step):
        sw -= .1*step
        if sw < 0:
            sw = 0


sw = 0
ul = 0
for i in range(n):
    if (i+1) % (1/step) == 0:
        ul += 1
    if sw >= len(switch_list):
        sw = 0


# Magnitude
    limiter = 100
# Assist
    a = .1
# Shooting
    s = .5
# Rebound
    e = .1
# Turnover
    t = -.3


# steals
    st = .3
# opponent shooting percentage
    so = 0.5
# Rebound
    rd = 0.2

# 24 Hour Time
    t_module = t % 60
# Natural Return to Average
    weight = .3
# Effeciency On/Off Switch
    switch = 0

# Assist Change
    # if t > 30 and not teamwork:
    #     b = .25 / limiter
    #     b = b - 17.5 / limiter * step
    # if b < -1 / limiter:
    #     b = -1 / limiter
    # if t > 39 and teamwork:
    #     b = .25 / limiter
    #     b = b - 20 / limiter * step
    # if b < -1 / limiter:
    #     b = -1 / limiter
    # if t > 39 and t < 168:
    #     tr = .1 / limiter

#     ### Parameter Changes ###
#     # Sleep Time
#         if t_module < sleep:
#             s = .91/limiter
#             b = 0
#             z = 0

#     # Relax Time
#         if t_module > sleep and t_module < (sleep + .5*relax):
#             r = 5/limiter
#             b = 0

#     # Work Time
#         if t_module > (sleep + .5*relax) and t_module < (sleep + .5*work + .5*relax):
#             w = 250/limiter
#             switch = switch_list[sw]
#             sw += 1
#             if t > 39:
#                 w = 750/limiter

#     # Exercise Time
#         if t_module > (sleep + .5*work + .5*relax) and t_module < (sleep + .5*work + .5*relax + .5*exercise):
#             e = .8/limiter
#             b = 0

#     # Work Time
#         if t_module > (sleep + .5*work + .5*relax + .5*exercise) and t_module < (sleep + work + .5*relax + .5*exercise):
#             w = 250/limiter
#             switch = switch_list[sw]
#             sw += 1
#             if t > 39:
#                 w = 750/limiter
#     # Exercise Time
#         if t_module > (sleep + work + .5*relax + .5*exercise) and t_module < (sleep + work + .5*relax + exercise):
#             e = .8/limiter
#             b = 0

#     # Relaxation Time
#         if t_module > (sleep + work + .5*relax + exercise) and t_module <= 24:
#             r = 5/limiter
#             b = 0

#     # Initial Flight
#         if t <= 39:
#             d = 2.16 / limiter
#             w_g = 0

#     # Population Change
#         if t > 39:
#             w_g = w
#             p = p + 1.1 * step
#         if p > 14:
#             p = 14
#     ##########################

#     ### Equations ###
#         doe_dt = b * (c_s * c_g) * (w / p) + (-s - r + e -
#                                                z + tr) * c_s - ((c_s - 20.39) / 7.74) * weight
#         dde_dt = b * (c_s * c_g) * (w_g / p) + (-s - r +
#                                                  e + d - z) * c_g - ((c_g - 20.39) / 7.74) * weight
#         p_t = math.exp(-(((((c_s + c_g) / 2) - 20.39)**2) /
#                        (2 * 7.74**2))) * switch
#     #################

#     ### Euler's Method ###
#         doe = doe + step * doe_dt
#         dde = dde + step * dde_dt


#     ######################

#     # Crew Stress Convergence
#         if t > 168 and np.abs(c_g - c_s) < .001:
#             c_g = c_s

#         t = step * (i + 1)
#         total_p.append(p_t)
#         if t % 24 == 0:
#             daily_ave_p.append(sum(total_p)/len(total_p))
#             total_p = []
#         c_ss.append(c_s)
#         c_gs.append(c_g)
#         p_ts.append(p_t)
#         ts.append(t)
# if i == 2399:
#         if diff_score > 0:
#             wa.append(1)
#         elif diff_score < 0:
#             wa.append(0)
#         else:
#             wa.append(.5)
#     else:
#         wa.append((score_weight * point_w +
#                   defensive_weight*dd + offence_weight*do))


# Winning Percentage Fixed

# for i in range(int(l)):
#     tl.append(i)
#     # Update offensive and defensive efficiency
#     diff_off_eff += random.uniform(-0.011, 0.01)
#     diff_def_eff += random.uniform(-0.011, 0.01)
#     diff_score += random.uniform(-1, 1)
#     score.append(diff_score)
#     deff.append(diff_def_eff)
#     off.append(diff_off_eff)

#     # Off Reset
#     if diff_off_eff > 1:
#         diff_off_eff = 1
#     if diff_off_eff < 0:
#         diff_off_eff = 0
#     # Def Reset
#     if diff_def_eff > 1:
#         diff_def_eff = 1
#     if diff_def_eff < 0:
#         diff_def_eff = 0
#     # Score Reset
#     if diff_score > 25:
#         diff_score = 25
#     if diff_score < -25:
#         diff_score = -25

#     # Calculate Weights

#     # Score Weight
#     score_weight = 0
#     if diff_score >= -3 and diff_score < 3:
#         score_weight = .5
#     elif diff_score >= 3 and diff_score < 8:
#         score_weight = .6
#     elif diff_score >= 8 and diff_score < 12:
#         score_weight = .7
#     elif diff_score >= 12 and diff_score < 18:
#         score_weight = .8
#     elif diff_score >= 18 and diff_score < 25:
#         score_weight = .9
#     elif diff_score >= 25:
#         score_weight = 1
#     elif diff_score >= -8 and diff_score < -3:
#         score_weight = .4
#     elif diff_score >= -12 and diff_score < -8:
#         score_weight = .3
#     elif diff_score >= -18 and diff_score < -12:
#         score_weight = .2
#     elif diff_score >= -25 and diff_score < -18:
#         score_weight = .1
#     else:
#         score_weight = 0

#     scd.append(score_weight)
#     # Offensive Weight
#     offence_weight = 0
#     if diff_off_eff >= -.05 and diff_off_eff < .05:
#         offence_weight = .5
#     elif diff_off_eff >= .05 and diff_off_eff < .1:
#         offence_weight = .6
#     elif diff_off_eff >= .1 and diff_off_eff < .2:
#         offence_weight = .7
#     elif diff_off_eff >= .2 and diff_off_eff < .3:
#         offence_weight = .8
#     elif diff_off_eff >= .3 and diff_off_eff < .4:
#         offence_weight = .9
#     elif diff_off_eff >= .4:
#         offence_weight = 1
#     elif diff_off_eff >= -.1 and diff_off_eff < -.05:
#         offence_weight = .4
#     elif diff_off_eff >= -.2 and diff_off_eff < -.1:
#         offence_weight = .3
#     elif diff_off_eff >= -.3 and diff_off_eff < -.2:
#         offence_weight = .2
#     elif diff_off_eff >= -.4 and diff_off_eff < -.3:
#         offence_weight = .1
#     else:
#         offence_weight = 0

#     defensive_weight = 0
#     # offence_weight = 0
#     if diff_def_eff >= -.05 and diff_def_eff < .05:
#         defensive_weight = .5
#     elif diff_def_eff >= .05 and diff_def_eff < .1:
#         defensive_weight = .6
#     elif diff_def_eff >= .1 and diff_def_eff < .2:
#         defensive_weight = .7
#     elif diff_def_eff >= .2 and diff_def_eff < .3:
#         defensive_weight = .8
#     elif diff_def_eff >= .3 and diff_def_eff < .4:
#         defensive_weight = .9
#     elif diff_def_eff >= .4:
#         defensive_weight = 1
#     elif diff_def_eff >= -.1 and diff_def_eff < -.05:
#         defensive_weight = .4
#     elif diff_def_eff >= -.2 and diff_def_eff < -.1:
#         defensive_weight = .3
#     elif diff_def_eff >= -.3 and diff_def_eff < -.2:
#         defensive_weight = .2
#     elif diff_def_eff >= -.4 and diff_def_eff < -.3:
#         defensive_weight = .1
#     else:
#         defensive_weight = 0

#     # Weights will change over time
#     point_w = 0
#     point_w = 1-((duration - weight_time)/duration)
#     do = (1-point_w)/2
#     dd = do

#     # Eulers Method

#     if i == 2399:
#         if diff_score > 0:
#             wa.append(1)
#         elif diff_score < 0:
#             wa.append(0)
#         else:
#             wa.append(.5)
#     else:
#         wa.append((score_weight * point_w +
#                   defensive_weight*dd + offence_weight*do))

#     weight_time = i

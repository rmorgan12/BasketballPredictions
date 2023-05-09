# Imports
# -----------------------------------------------------------
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


# Initial Team Values
# -----------------------------------------------------------
# Teams
teamA = "Utah Tech University"
teamB = "Oregon State University"

# Initial Offensive Effeciencies
initial_off_eff_a = 0.7  # Offensive effiency of team A
initial_off_eff_b = 0.7  # Offensive effiency of team B
diff_off_eff = initial_off_eff_a - initial_off_eff_b

# Initial Deffensive Effeciencies
initial_def_eff_a = 0.7  # Deffensive efficieny of team A
initial_def_eff_b = 0.7  # Deffensive efficieny of team B
diff_def_eff = initial_def_eff_a - initial_def_eff_b

# Initial Score
score_team_a = 0  # Team A Score
score_team_b = 0  # Team B Score
diff_score = score_team_a - score_team_b  # Difference between two scores (A-B)

# Initial Win Probability
initial_prob_a = 0.5  # initial probability of winning
initial_prob_b = 0.5  # initial probability of winning

# Time Set-Up
total_time = 40  # Minutes in the game
dt = 1/60  # Seconds per Minute
duration = total_time/dt
weight_time = 0  # Used to measure the weight score should have on %


# Define the time array
# -----------------------------------------------------------
t = np.arange(0, total_time, dt)  # creates empty time array
l = duration
# do I need the time array? Can I create


# Define the arrays to store the population values at each time step
wa = []
wb = []
score = []
deff = []
off = []
tl = [0]
scd = [0]
wa.append(initial_prob_a)
wb.append(initial_prob_b)
score.append(diff_score)
deff.append(diff_def_eff)
off.append(diff_off_eff)
x = 0
# Euler's method
# -----------------------------------------------------------
for i in range(int(l)):
    tl.append(i)
    # Update offensive and defensive efficiency
    diff_off_eff += random.uniform(-0.011, 0.01)
    diff_def_eff += random.uniform(-0.011, 0.01)
    diff_score += random.uniform(-1, 1)
    score.append(diff_score)
    deff.append(diff_def_eff)
    off.append(diff_off_eff)

    # Off Reset
    if diff_off_eff > 1:
        diff_off_eff = 1
    if diff_off_eff < 0:
        diff_off_eff = 0
    # Def Reset
    if diff_def_eff > 1:
        diff_def_eff = 1
    if diff_def_eff < 0:
        diff_def_eff = 0
    # Score Reset
    if diff_score > 25:
        diff_score = 25
    if diff_score < -25:
        diff_score = -25

    # Calculate Weights

    # Score Weight
    score_weight = 0
    if diff_score >= -3 and diff_score < 3:
        score_weight = .5
    elif diff_score >= 3 and diff_score < 8:
        score_weight = .6
    elif diff_score >= 8 and diff_score < 12:
        score_weight = .7
    elif diff_score >= 12 and diff_score < 18:
        score_weight = .8
    elif diff_score >= 18 and diff_score < 25:
        score_weight = .9
    elif diff_score >= 25:
        score_weight = 1
    elif diff_score >= -8 and diff_score < -3:
        score_weight = .4
    elif diff_score >= -12 and diff_score < -8:
        score_weight = .3
    elif diff_score >= -18 and diff_score < -12:
        score_weight = .2
    elif diff_score >= -25 and diff_score < -18:
        score_weight = .1
    else:
        score_weight = 0

    scd.append(score_weight)
    # Offensive Weight
    offence_weight = 0
    if diff_off_eff >= -.05 and diff_off_eff < .05:
        offence_weight = .5
    elif diff_off_eff >= .05 and diff_off_eff < .1:
        offence_weight = .6
    elif diff_off_eff >= .1 and diff_off_eff < .2:
        offence_weight = .7
    elif diff_off_eff >= .2 and diff_off_eff < .3:
        offence_weight = .8
    elif diff_off_eff >= .3 and diff_off_eff < .4:
        offence_weight = .9
    elif diff_off_eff >= .4:
        offence_weight = 1
    elif diff_off_eff >= -.1 and diff_off_eff < -.05:
        offence_weight = .4
    elif diff_off_eff >= -.2 and diff_off_eff < -.1:
        offence_weight = .3
    elif diff_off_eff >= -.3 and diff_off_eff < -.2:
        offence_weight = .2
    elif diff_off_eff >= -.4 and diff_off_eff < -.3:
        offence_weight = .1
    else:
        offence_weight = 0

    defensive_weight = 0
    # offence_weight = 0
    if diff_def_eff >= -.05 and diff_def_eff < .05:
        defensive_weight = .5
    elif diff_def_eff >= .05 and diff_def_eff < .1:
        defensive_weight = .6
    elif diff_def_eff >= .1 and diff_def_eff < .2:
        defensive_weight = .7
    elif diff_def_eff >= .2 and diff_def_eff < .3:
        defensive_weight = .8
    elif diff_def_eff >= .3 and diff_def_eff < .4:
        defensive_weight = .9
    elif diff_def_eff >= .4:
        defensive_weight = 1
    elif diff_def_eff >= -.1 and diff_def_eff < -.05:
        defensive_weight = .4
    elif diff_def_eff >= -.2 and diff_def_eff < -.1:
        defensive_weight = .3
    elif diff_def_eff >= -.3 and diff_def_eff < -.2:
        defensive_weight = .2
    elif diff_def_eff >= -.4 and diff_def_eff < -.3:
        defensive_weight = .1
    else:
        defensive_weight = 0

    # Weights will change over time
    point_w = 0
    point_w = 1-((duration - weight_time)/duration)
    do = (1-point_w)/2
    dd = do

    # Eulers Method

    if i == 2399:
        if diff_score > 0:
            wa.append(1)
        elif diff_score < 0:
            wa.append(0)
        else:
            wa.append(.5)
    else:
        wa.append((score_weight * point_w +
                  defensive_weight*dd + offence_weight*do))

    weight_time = i

# Plot the results
# -----------------------------------------------------------
plt.plot(tl, wa, label='Winning Percentage of ' + teamA)
plt.xlabel('Time (Seconds)')
plt.ylabel('Probability of Winning')
plt.title(teamA + " Win Probability")
plt.legend()
plt.show()

plt.plot(tl, score, label='Score Difference')
plt.xlabel('Time (Seconds)')
plt.ylabel('Score Difference')
plt.title('Score Difference')
plt.legend()
plt.show()


# plt.plot(tl, deff, label='Deffensive Efficiency Difference')
# plt.xlabel('Time (Seconds)')
# plt.ylabel('Deffensive Effeciency Difference')
# plt.title('Def Eff Dif')
# plt.legend()
# plt.show()

# plt.plot(tl, off, label='Offensive Efficiency Differnce')
# plt.xlabel('Time (Seconds)')
# plt.ylabel('Offensive Efficiency Difference')
# plt.title('Off Eff Dif')
# plt.legend()
# plt.show()

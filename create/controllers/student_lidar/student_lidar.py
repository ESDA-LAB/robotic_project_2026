"""ESDA LAB – Φοιτητικό αρχείο εργασίας, Webots R2025a.
Υλοποιήστε τα TODO. Ο starter controller αρχικά κρατά το ρομπότ ακίνητο.
"""
from controller import Robot
import math
import csv
from pathlib import Path

FRONT_LIMIT_M = 0.65
CAUTION_LIMIT_M = 0.95
CRUISE_RAD_S = 7.0
TURN_RAD_S = 5.0

robot = Robot()
step_ms = int(robot.getBasicTimeStep())
lidar = robot.getDevice('esda_lidar')
lidar.enable(step_ms)
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
for motor in (left_motor, right_motor):
    motor.setPosition(float('inf'))
    motor.setVelocity(0.0)

# ΣΤΑΔΙΟ 1: ολοκληρώστε τη συνάρτηση ώστε να επιστρέφει ελάχιστη
# έγκυρη απόσταση (m) μέσα σε γωνιακό τομέα.
# Στο συγκεκριμένο παράδειγμα ελέγξτε οπτικά τον προσανατολισμό LiDAR.
def sector_min(ranges, start_deg, stop_deg):
    # TODO 1: αντιστοίχιση index → γωνία, φιλτράρισμα inf/NaN/μη έγκυρων
    raise NotImplementedError('TODO 1: sector_min')

# ΣΤΑΔΙΟ 2: επιστρέψτε (left_speed, right_speed, mode).
# Θυμηθείτε: θετικές ίσες ταχύτητες → ευθύγραμμη κίνηση,
# αντίθετες → περιστροφή. Προσθέστε υστέρηση/χρόνο στροφής αν χρειάζεται.
def decide(front_m, left_m, right_m):
    # TODO 2: FORWARD / SLOW / TURN σύμφωνα με τις αποστάσεις.
    raise NotImplementedError('TODO 2: decide')

print('[ESDA STUDENT] Controller loaded. Complete TODO 1 & 2 before running.', flush=True)
while robot.step(step_ms) != -1:
    ranges = lidar.getRangeImage()
    if not ranges:
        continue
    # TODO 3: υπολογίστε front, left, right από τρεις τομείς.
    # front = sector_min(ranges, -28, 28)
    # left  = sector_min(ranges, ... , ...)
    # right = sector_min(ranges, ... , ...)
    # left_speed, right_speed, mode = decide(front, left, right)
    # left_motor.setVelocity(left_speed)
    # right_motor.setVelocity(right_speed)

    # TODO 4: CSV με simulation time, front, speeds, mode.
    # Σκοπίμως το ρομπότ παραμένει ακίνητο μέχρι να ολοκληρώσετε τα TODO.
    pass

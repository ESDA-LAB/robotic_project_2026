"""ESDA LAB – Φοιτητικό αρχείο εργασίας, Webots R2025a.
Υλοποιήστε τα TODO. Ο starter controller αρχικά κρατά το ρομπότ ακίνητο.
"""
from controller import Robot
import math
import csv
import atexit
from pathlib import Path

FRONT_LIMIT_M = 0.65
CAUTION_LIMIT_M = 0.95
CRUISE_RAD_S = 7.0
TURN_RAD_S = 5.0

# CSV logging configuration
# Common data format for all simulation experiments

CSV_COLUMNS = [
    "time_s",
    "front_m",
    "left_m",
    "right_m",
    "left_speed",
    "right_speed",
    "mode",
    "avoidance_events",
    "bumper_events"
]

# Folder for experiment results
LOG_DIR = Path(__file__).resolve().parents[2] / "results"

# Create results folder if it does not exist
LOG_DIR.mkdir(parents=True, exist_ok=True)

# CSV file for the current experiment
CSV_FILE = LOG_DIR / "run_log.csv"

# Open CSV file and write column headers
csv_file = CSV_FILE.open("w", newline="", encoding="utf-8")
csv_writer = csv.DictWriter(csv_file, fieldnames=CSV_COLUMNS)
csv_writer.writeheader()
csv_file.flush()

# Close the CSV file on normal Python interpreter shutdown
atexit.register(csv_file.close)

# Cumulative avoidance counter
avoidance_events = 0
previous_mode = None

# Bumper events are not measured in the starter version
bumper_events = 0

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

    # TODO 4 - CSV DATA LOGGING (Φοιτητής Β)
    # Σκοπός:
    # Καταγραφή των δεδομένων λειτουργίας του ρομπότ.
    #
    # 1. Πάρτε τον χρόνο προσομοίωσης:
    #    robot.getTime()
    #
    # 2. Χρησιμοποιήστε τις μεταβλητές:
    #    front, left, right
    #    left_speed, right_speed, mode
    #    που θα υπολογίζονται στο TODO 3.
    #
    # 3. Αυξήστε τον μετρητή avoidance_events
    #    κάθε φορά που το ρομπότ εισέρχεται στην
    #    κατάσταση TURN από άλλη κατάσταση.
    #    Χρησιμοποιήστε τη μεταβλητή previous_mode.
    #
    # 4. Δημιουργήστε ένα dictionary με τις στήλες
    #    που ορίζονται στο CSV_COLUMNS.
    #
    # 5. Καταγράψτε μία γραμμή στο CSV με:
    #    csv_writer.writerow(...)
    #
    # 6. Αποθηκεύστε τις εγγραφές:
    #    csv_file.flush()
    #
    # Σημείωση:
    # Το bumper_events παραμένει 0, καθώς δεν
    # υλοποιείται μέτρηση των αισθητήρων επαφής.
    # Η τιμή αυτή ΔΕΝ σημαίνει μηδενικές συγκρούσεις.
    #
    # =========================================================

    pass
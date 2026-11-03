
"""ESDA Lab: Ανάλυση δεδομένων CSV από την προσομοίωση Webots."""

import csv
import sys
import math
from collections import Counter
from pathlib import Path

# TODO 6 - Φοιτητής Β:
# Μετά την εγκατάσταση του matplotlib, προσθέστε:
# import matplotlib.pyplot as plt


def analyze_file(filename):
    path = Path(filename)

    try:
        with path.open(newline="", encoding="utf-8") as fp:
            reader = csv.DictReader(fp)

            if reader.fieldnames is None:
                print(f"{filename}: Το αρχείο CSV είναι κενό.")
                return

            required = {"time_s", "front_m", "mode",
                        "avoidance_events", "bumper_events"}
            missing = required - set(reader.fieldnames)

            if missing:
                print(
                    f"{filename}: Λείπουν οι στήλες: "
                    + ", ".join(sorted(missing))
                )
                return

            rows = list(reader)

    except (OSError, UnicodeError, csv.Error) as error:
        print(f"{filename}: Σφάλμα ανάγνωσης CSV: {error}")
        return

    if not rows:
        print(
            f"{filename}: Δεν υπάρχουν μετρήσεις. "
            "Ολοκληρώστε πρώτα το TODO 4."
        )
        return

    # =====================================================
    # TODO 5 - MINIMUM LIDAR DISTANCE (Φοιτητής Β)
    # =====================================================
    #
    # 1. Διαβάστε τις τιμές της στήλης "front_m".
    # 2. Μετατρέψτε τις τιμές σε float.
    # 3. Αγνοήστε κενές, μη αριθμητικές τιμές,
    #    NaN, inf και μη θετικές αποστάσεις.
    # 4. Υπολογίστε την ελάχιστη έγκυρη απόσταση.
    # 5. Εμφανίστε το αποτέλεσμα σε μέτρα.
    #
    # Εάν δεν υπάρχουν έγκυρες μετρήσεις,
    # εμφανίστε "No valid LiDAR measurements".
    #
    # TODO: Συμπληρώστε τον κώδικα εδώ.

    last = rows[-1]

    print(f"\nΑρχείο: {filename}")
    print("Simulation time (s):", last["time_s"])
    print("Avoidance events:", last["avoidance_events"])
    print(
        "Bumper events (not measured in starter):",
        last["bumper_events"]
    )
    print("Samples in each state (not seconds):")
    print(dict(Counter(row["mode"] for row in rows)))

    # =====================================================
    # TODO 6 - LIDAR DISTANCE GRAPH (Φοιτητής Β)
    # =====================================================
    #
    # 1. Διαβάστε τις τιμές "time_s" και "front_m".
    # 2. Κρατήστε μόνο έγκυρα ζεύγη τιμών.
    # 3. Χρησιμοποιήστε matplotlib.pyplot.
    # 4. Δημιουργήστε γράφημα:
    #    X: χρόνος προσομοίωσης (s)
    #    Y: απόσταση LiDAR (m)
    # 5. Προσθέστε τίτλο και ονόματα αξόνων.
    # 6. Αποθηκεύστε το γράφημα ως PNG.
    #
    # TODO: Συμπληρώστε τον κώδικα εδώ.


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Χρήση: python create/tools/analyze_csv.py "
            "create/results/run_log.csv"
        )
        sys.exit(1)

    for filename in sys.argv[1:]:
        analyze_file(filename)

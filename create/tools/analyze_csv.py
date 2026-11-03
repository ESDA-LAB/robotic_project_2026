import csv
import sys
import math
from pathlib import Path

# Βιβλιοθήκη για το TODO 6 - Φοιτητής Β:
# Για τη δημιουργία γραφημάτων θα χρειαστεί
# η βιβλιοθήκη matplotlib.
#
# Αφού εγκατασταθεί, προσθέστε εδώ:
# import matplotlib.pyplot as plt

for filename in sys.argv[1:]:
    with Path(filename).open(newline='', encoding='utf-8') as fp:
        rows = list(csv.DictReader(fp))
    if not rows:
        print(filename, 'empty log'); continue

    # =====================================================
    # TODO 5 - MINIMUM LIDAR DISTANCE (Φοιτητής Β)
    # =====================================================
    #
    # Σκοπός:
    # Υπολογίστε την ελάχιστη έγκυρη απόσταση
    # που καταγράφηκε μπροστά από το ρομπότ.
    #
    # 1. Διαβάστε τη στήλη "front_m" από το CSV.
    # 2. Μετατρέψτε τις τιμές σε float.
    # 3. Αγνοήστε κενές, μη αριθμητικές τιμές,
    #    NaN, inf και μη θετικές αποστάσεις.
    # 4. Υπολογίστε την ελάχιστη απόσταση.
    # 5. Εμφανίστε το αποτέλεσμα σε μέτρα.
    #
    # Εάν δεν υπάρχουν έγκυρες μετρήσεις,
    # εμφανίστε "No valid LiDAR measurements".
    #
    # TODO: Συμπληρώστε τον κώδικα εδώ.

    last = rows[-1]
    print(filename)
    print('Simulation time (s):', last['time_s'])
    print('Avoidance events:', last['avoidance_events'])
    print('Bumper contact events:', last['bumper_events'])
    print('Time in each state (approx. sampled frames):')
    from collections import Counter
    print(dict(Counter(r['mode'] for r in rows)))

    # =====================================================
    # TODO 6 - LIDAR DISTANCE GRAPH (Φοιτητής Β)
    # =====================================================
    #
    # Σκοπός:
    # Δημιουργήστε γράφημα της απόστασης LiDAR
    # ως προς τον χρόνο προσομοίωσης.
    #
    # 1. Διαβάστε τη στήλη "time_s".
    # 2. Διαβάστε τη στήλη "front_m".
    # 3. Κρατήστε μόνο έγκυρα ζεύγη τιμών.
    # 4. Χρησιμοποιήστε matplotlib.pyplot.
    # 5. Στον οριζόντιο άξονα βάλτε τον χρόνο (s).
    # 6. Στον κατακόρυφο άξονα την απόσταση (m).
    # 7. Προσθέστε τίτλο και ονόματα αξόνων.
    # 8. Αποθηκεύστε το γράφημα ως PNG.
    #
    # TODO: Συμπληρώστε τον κώδικα εδώ.

import csv
import sys
from pathlib import Path
for filename in sys.argv[1:]:
    with Path(filename).open(newline='', encoding='utf-8') as fp:
        rows = list(csv.DictReader(fp))
    if not rows:
        print(filename, 'empty log'); continue
    last = rows[-1]
    print(filename)
    print('Simulation time (s):', last['time_s'])
    print('Avoidance events:', last['avoidance_events'])
    print('Bumper contact events:', last['bumper_events'])
    print('Time in each state (approx. sampled frames):')
    from collections import Counter
    print(dict(Counter(r['mode'] for r in rows)))

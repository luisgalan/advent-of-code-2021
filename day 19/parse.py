print(30)
for i in range(30):
    input()
    cur = input()
    beacons = []
    while len(cur) > 0:
        beacons.append(list(map(int, cur.split(','))))
        cur = input()
    print(len(beacons))
    for beacon in beacons:
        print(beacon[0], beacon[1], beacon[2])
    print("")


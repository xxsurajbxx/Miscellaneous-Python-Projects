while True:
    print('Enter Your Time')
    time = input('>>>')
    print('Enter The Distance')
    distance = input('>>>')
    print('Enter The Type of Measurement')
    print('y for yards')
    print('m for meters')
    measurement = input('>>>')
    if measurement.lower() != 'y' and measurement.lower() != 'm':
        print('Please Enter "Y" or "M"')
        continue
    if measurement.lower() == 'm':
        distance_in_yards = int(distance) * 1.09361
        rate = float(time) / distance_in_yards
        time_in_yards = rate * float(distance)
        print(f'Your time for {distance} yds is {time_in_yards} seconds')
    if measurement.lower() == 'y':
        distance_in_meters = int(distance) * 0.9144
        rate = float(time) / distance_in_meters
        time_in_meters = rate * float(distance)
        print(f'Your time for {distance} meters is {time_in_meters} seconds')
    print('Press Enter to Continue')
    leave = input('>>>')
    if leave != '':
        break

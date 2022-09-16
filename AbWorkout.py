import random


Custom = [
    ["Crunches", "High Crunches", "Sit-Ups", "Long-Arm Crunches", "Hundreds", "Knee Crunches"],
    ["Reverse Crunches", "Scissors", "Leg Raises", "Pulse-Ups", "Bicycle Crunches", "Crunch Kicks",
     "Raised Leg Circles"],
    ["Flutter Kicks", "Elbow Plank", "L-Sit", "Star Plank", "Hollow Hold", "V-Ups"],
    ["Sitting Twists", "Cross Crunches", "Side Jack-Knives", "Toe-Taps", "Sitting Punches", "Side Plank"],
    ["Knee To Elbow", "Sitting Knee To Elbow", "Dead Bug", "Plank Crunches", "Side Plank Crunches", "V With Rotations",
     "Raised Leg Hold"],
    ["Half Wipers", "Arm & Leg Raises", "Wipers", "Plank Rolls", "Knee-In Twists", "Climber Taps"]]
Athleanx = ['Leg Circles 60 seconds', 'Leg Circles 60 seconds(other direction)', 'Drunken Mtn Climbers for 60 seconds',
            'Rest for 30 seconds', 'Marching Planks for 60 seconds', 'Scissors for 60 seconds',
            'Starfish Crunches for 30 seconds', 'Rest for 30 seconds', 'Russian V-Tuck Twists for 30 seconds']
Thenx = ['High-Knee Taps', 'Russian Twists', 'Leg Raises', 'Hip Raises', 'Flutter Kicks','Planks Knees to Elbow',
         'Chair Sit-Ups', 'Seated In and Outs', 'Jumping Jacks','Do each exercise for 45 seconds',
         'Rest for 15 seconds after each exercise']
workouts = [Custom, Athleanx, Thenx]
if random.choice(workouts) == Thenx:
    for workout in Thenx:
        print(workout)
if random.choice(workouts) == Athleanx:
    for workout in Athleanx:
        print(workout)
if random.choice(workouts) == Custom:
    for Exercise in Custom:
        SpecificExercise = random.choice(Exercise)
        if SpecificExercise == 'Elbow Plank' or SpecificExercise == 'Star Plank' or SpecificExercise == 'Hollow Hold' \
                or SpecificExercise == 'Side Plank' or SpecificExercise == 'L-Sit'\
                or SpecificExercise == 'Raised Leg Hold':
            NumberOfReps = random.randint(45, 90)
            print(f'{SpecificExercise} for {NumberOfReps} seconds')
        else:
            NumberOfReps = random.choice(range(20, 40, 2))
            print(f"{NumberOfReps} {SpecificExercise}")
print("👍👌🔥Good Luck🔥👌👍")

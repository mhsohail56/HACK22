from structure import Station, Train, csv


# Function to write the CSV information for the given schedule
def write_csv(trains: list) -> None:

    with open("output.csv", "w") as output:
        writer = csv.writer(output, delimiter=",")
        
        writer.writerow([
            "TrainNum",
            "TrainType",
            "A_ArrivalTime",
            "A_AvailCap",
            "A_Boarding",
            "B_ArrivalTime",
            "B_AvailCap",
            "B_Boarding",
            "C_ArrivalTime",
            "C_AvailCap",
            "C_Boarding",
            "U_Arrival",
            "U_AvailCap",
            "U_Offloading"
        ])

        for i, train in enumerate(trains):
            writer.writerow([i + 1] + train.details)


# Everything after this is testing, here we need to find a way to optimize 'schedule'

# Our schedule has the format where the first number represents the train capacity (4 x 200; 12 x 400)
# and the second represents the departure time (minutes after 7AM)

# This schedule currently reflects the one provided in the Google Drive file from RailVision
schedule = [
    (200, 0),
    (400, 10),
    (400, 15),
    (400, 20),
    (400, 30),
    (400, 40),
    (400, 50),
    (400, 60),
    (400, 70),
    (400, 80),
    (400, 90),
    (400, 105),
    (400, 130),
    (200, 150),
    (200, 160),
    (200, 180),
]

trains = [Train(c, t) for c, t in schedule]
av = Train.run_schedule(trains)

# Writing the CSV of the schedule
write_csv(trains)

# For checking
print(av)
print(Train.total_passengers_collected)
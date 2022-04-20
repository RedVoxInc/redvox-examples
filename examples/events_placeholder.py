"""
Start from report page at:
https://redvox.io/#/reports/redvoxcore@12Apr22.02.48.36

Print movement and yamnet events from:
Time aligned and corrected data window

"""
import os
from redvox.common.data_window import DataWindow

print(__doc__)

# Change input dir to point to your data directory
input_dir = "/Users/mgarces/Documents/DATA_2022/WAMV_EXAMPLE"

# Name of the REdVox datawindow file you downloaded:
input_file = "dw_1647024780000029_2.pkl.lz4"


def main() -> None:
    # Load datawindow from report
    dw = DataWindow.deserialize(os.path.join(input_dir, input_file))

    print("\n All native timestamps are in microseconds since Unix epoch UTC")
    for station in dw.stations():
        print(station.event_data().get_stream_names())
        movement_events = station.event_data().get_stream('Movement')
        print("Length of Movement events:", len(movement_events.events))
        print(movement_events.events[0])
        print(movement_events.events[0].get_numeric_column('magnitude_max'))

        if 'yamnet' in station.event_data().get_stream_names():
            yamnet_events = station.event_data().get_stream('yamnet')
            print("Length of yamnet events:", len(yamnet_events.events))
            for event in yamnet_events.events:
                # TODO: Sort by score
                print(event.get_string_column('class'), event.get_numeric_column('score'))


if __name__ == "__main__":
    main()

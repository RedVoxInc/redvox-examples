"""
Start from report page at:
https://redvox.io/#/reports/redvoxcore@12Apr22.02.48.36

Must log into the webpage as `redvoxcore`.

Load audio waveform data from:
Time aligned and corrected data window

"""
import os
from matplotlib import pyplot as plt
from redvox.common.data_window import DataWindow

print(__doc__)

# CONSTANT: Convert from native microseconds to seconds
MICROS_TO_S = 1E-6

# Change input_dir to point to your data directory
# input_dir = "/Users/mgarces/Documents/DATA_2022/WAMV_EXAMPLE"
input_dir = '/Users/meritxell/Desktop'

# Name of the REdVox datawindow file you downloaded:
input_file = "dw_1647024780000029_2.pkl.lz4"


def main() -> None:
    # Load datawindow from report
    dw = DataWindow.deserialize(os.path.join(input_dir, input_file))

    print("\n All native timestamps are in microseconds since Unix epoch UTC")
    for station in dw.stations():
        print(f"Station {station.id()} Audio Sensor:\n"
              f"mic nominal sample rate in hz: {station.audio_sample_rate_nominal_hz()}\n"
              f"mic computed sample rate in hz: {station.audio_sensor().sample_rate_hz()}\n"
              f"is mic sample rate constant: {station.audio_sensor().is_sample_rate_fixed()}\n"
              f"mic sample interval in seconds: {station.audio_sensor().sample_interval_s()}\n"
              f"mic sample interval std dev: {station.audio_sensor().sample_interval_std_s()}\n"
              f"the first data timestamp: {station.audio_sensor().first_data_timestamp()}\n"
              f"the last data timestamp:  {station.audio_sensor().last_data_timestamp()}\n"
              f"the number of data samples: {station.audio_sensor().num_samples()}\n"
              f"the names of the dataframe columns: {station.audio_sensor().data_channels()}\n")

        # Plot the mic data
        audio_samples = station.audio_sensor().get_microphone_data()
        audio_time_micros = station.audio_sensor().data_timestamps() - station.audio_sensor().first_data_timestamp()
        audio_time_s = audio_time_micros*MICROS_TO_S

        plt.figure()
        plt.plot(audio_time_s, audio_samples)
        plt.title(f"RedVox Station ID {station.id()}")
        plt.xlabel(f"Seconds from {int(dw.start_date()*MICROS_TO_S)} Unix epoch UTC")
        plt.ylabel("Normalized amplitude")
    plt.show()


if __name__ == "__main__":
    main()

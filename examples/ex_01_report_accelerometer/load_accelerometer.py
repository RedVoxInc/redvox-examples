"""
Start from report page at:
https://redvox.io/#/reports/E328

Load accelerometer waveform data from:
Time aligned and corrected data window

"""
import os
from matplotlib import pyplot as plt
from redvox.common.data_window import DataWindow

print(__doc__)

# CONSTANT: Convert from native microseconds to seconds
MICROS_TO_S = 1E-6

# Change input_dir the path of your data directory
# input_dir = "/CHANGE/ME/DATA_2022/REDVOX_EXAMPLES"
# Example:
# input_dir = "/Users/mgarces/Documents/DATA_2022/REDVOX_EXAMPLES"

# Name of the RedVox datawindow file you downloaded:
INPUT_FILE = "dw_1648830257000498_2.pkl.lz4"


def main() -> None:
    # Load datawindow from report
    dw = DataWindow.deserialize(os.path.join(input_dir, INPUT_FILE))

    print("\n All native timestamps are in microseconds since Unix epoch UTC")
    for station in dw.stations():
        # Check that there is accelerometer data in the first place
        if station.has_accelerometer_data():

            print(f"Station {station.id()} Accelerometer Sensor:\n"
                  f"accelerometer computed sample rate in hz: {station.audio_sensor().sample_rate_hz()}\n"
                  f"accelerometer sample interval in seconds: {station.accelerometer_sensor().sample_interval_s()}\n"
                  f"accelerometer sample interval std dev: {station.accelerometer_sensor().sample_interval_std_s()}\n"
                  f"the first data timestamp: {station.accelerometer_sensor().first_data_timestamp()}\n"
                  f"the last data timestamp:  {station.accelerometer_sensor().last_data_timestamp()}\n"
                  f"the number of data samples: {station.accelerometer_sensor().num_samples()}\n"
                  f"the names of the dataframe columns: {station.accelerometer_sensor().data_channels()}\n")

        # Accelerometer has 3 channels - x, y and z
        accelerometer_x_samples = station.accelerometer_sensor().get_accelerometer_x_data()
        accelerometer_y_samples = station.accelerometer_sensor().get_accelerometer_y_data()
        accelerometer_z_samples = station.accelerometer_sensor().get_accelerometer_z_data()
        # The channels share the same timestamps
        accelerometer_time_micros = station.accelerometer_sensor().data_timestamps() - \
                            station.accelerometer_sensor().first_data_timestamp()
        accelerometer_time_s = accelerometer_time_micros*MICROS_TO_S

        # Plot the acceleration data - one subplot per channel
        fig, ax = plt.subplots(nrows=3, ncols=1, sharex='col')
        ax[0].plot(accelerometer_time_s, accelerometer_x_samples)
        ax[1].plot(accelerometer_time_s, accelerometer_y_samples)
        ax[2].plot(accelerometer_time_s, accelerometer_z_samples)

        # Set labels and subplot title
        ax[0].set_ylabel(r'Acc X [$m/s^2$]')
        ax[1].set_ylabel(r'Acc Y [$m/s^2$]')
        ax[2].set_ylabel(r'Acc Z [$m/s^2$]')
        ax[2].set_xlabel(f"Seconds from {int(dw.start_date()*MICROS_TO_S)} Unix epoch UTC")

        plt.suptitle(f"RedVox Station ID {station.id()}")

    plt.show()


if __name__ == "__main__":
    main()

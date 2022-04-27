"""
Start from report page at:
https://redvox.io/#/reports/redvoxcore@12Apr22.02.48.36

Must log into the webpage as `redvoxcore`.

Load other sensor waveform data from:
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
input_dir = "/Users/meritxell/Desktop"

# Name of the REdVox datawindow file you downloaded:
input_file = "dw_1647024780000029_2.pkl.lz4"


def main() -> None:
    # Load datawindow from report
    dw = DataWindow.deserialize(os.path.join(input_dir, input_file))

    print("\n All native timestamps are in microseconds since Unix epoch UTC")
    for station in dw.stations():
        print('Single channel sensors such as barometer load the same as audio')
        # Check that there is barometer data in the first place
        if station.has_barometer_data():

            print(f"Station {station.id()} Barometer Sensor:\n"
                  f"barometer computed sample rate in hz: {station.barometer_sensor().sample_rate_hz()}\n"
                  f"barometer sample interval in seconds: {station.barometer_sensor().sample_interval_s()}\n"
                  f"barometer sample interval std dev: {station.barometer_sensor().sample_interval_std_s()}\n"
                  f"the first data timestamp: {station.barometer_sensor().first_data_timestamp()}\n"
                  f"the last data timestamp:  {station.barometer_sensor().last_data_timestamp()}\n"
                  f"the number of data samples: {station.barometer_sensor().num_samples()}\n"
                  f"the names of the dataframe columns: {station.barometer_sensor().data_channels()}\n")

        # Get barometer data and timestamps
        barometer_samples = station.barometer_sensor().get_pressure_data()
        barometer_time_micros = station.barometer_sensor().data_timestamps() - \
                                station.barometer_sensor().first_data_timestamp()
        barometer_time_s = barometer_time_micros*MICROS_TO_S

        # Plot the barometer data

        plt.figure()
        plt.plot(barometer_time_s, barometer_samples)
        plt.title(f"RedVox Station ID {station.id()}")
        plt.xlabel(f"Seconds from {int(dw.start_date()*MICROS_TO_S)} Unix epoch UTC")
        plt.ylabel("Raw Pressure [kPa]")

        print('Multi-channel sensors such as gyroscope load the same as the accelerometer sensor')
        # Check that there is gyroscope data in the first place
        if station.has_gyroscope_data():

            print(f"Station {station.id()} Gyroscope Sensor:\n"
                  f"gyroscope computed sample rate in hz: {station.gyroscope_sensor().sample_rate_hz()}\n"
                  f"gyroscope sample interval in seconds: {station.gyroscope_sensor().sample_interval_s()}\n"
                  f"gyroscope sample interval std dev: {station.gyroscope_sensor().sample_interval_std_s()}\n"
                  f"the first data timestamp: {station.gyroscope_sensor().first_data_timestamp()}\n"
                  f"the last data timestamp:  {station.gyroscope_sensor().last_data_timestamp()}\n"
                  f"the number of data samples: {station.gyroscope_sensor().num_samples()}\n"
                  f"the names of the dataframe columns: {station.gyroscope_sensor().data_channels()}\n")

        # Gyroscope has 3 channels - x, y and z
        gyroscope_x_samples = station.gyroscope_sensor().get_gyroscope_x_data()
        gyroscope_y_samples = station.gyroscope_sensor().get_gyroscope_y_data()
        gyroscope_z_samples = station.gyroscope_sensor().get_gyroscope_z_data()
        # The channels share the same timestamps
        gyroscope_time_micros = station.gyroscope_sensor().data_timestamps() - \
                                    station.gyroscope_sensor().first_data_timestamp()
        gyroscope_time_s = gyroscope_time_micros*MICROS_TO_S

        # Plot the acceleration data - one subplot per channel
        fig, ax = plt.subplots(nrows=3, ncols=1, sharex='col')
        ax[0].plot(gyroscope_time_s, gyroscope_x_samples)
        ax[1].plot(gyroscope_time_s, gyroscope_y_samples)
        ax[2].plot(gyroscope_time_s, gyroscope_z_samples)

        # Set labels and subplot title
        ax[0].set_ylabel('Gyr X [m/s]')
        ax[1].set_ylabel('Gyr Y [m/s]')
        ax[2].set_ylabel('Gyr Z [m/s]')
        ax[2].set_xlabel(f"Seconds from {int(dw.start_date()*MICROS_TO_S)} Unix epoch UTC")

        plt.suptitle(f"RedVox Station ID {station.id()}")

    plt.show()

    print('Visit https://github.com/RedVoxInc/redvox-python-sdk/tree/master/docs/python_sdk/data_window/station#using-station'
          'for more information on sensors available')


if __name__ == "__main__":
    main()

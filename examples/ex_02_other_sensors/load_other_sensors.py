"""
Start from report page at:
https://redvox.io/#/reports/E328

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
input_dir = "/CHANGE/ME/DATA_2022/WAMV_EXAMPLE"

# Name of the REdVox datawindow file you downloaded:
INPUT_FILE = "dw_1648830257000498_2.pkl.lz4"


def main() -> None:
    # Load datawindow from report
    dw = DataWindow.deserialize(os.path.join(input_dir, INPUT_FILE))

    print("\nAll native timestamps are in microseconds since Unix epoch UTC")
    for station in dw.stations():
        print('\nSingle channel sensors such as barometer load the same as audio')
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

        print('\nMulti-channel sensors such as magnetometer load the same as the accelerometer sensor')
        # Check that there is magnetometer data in the first place
        
        if station.has_magnetometer_data():

            print(f"Station {station.id()} Magnetometer Sensor:\n"
                  f"magnetometer computed sample rate in hz: {station.magnetometer_sensor().sample_rate_hz()}\n"
                  f"magnetometer sample interval in seconds: {station.magnetometer_sensor().sample_interval_s()}\n"
                  f"magnetometer sample interval std dev: {station.magnetometer_sensor().sample_interval_std_s()}\n"
                  f"the first data timestamp: {station.magnetometer_sensor().first_data_timestamp()}\n"
                  f"the last data timestamp:  {station.magnetometer_sensor().last_data_timestamp()}\n"
                  f"the number of data samples: {station.magnetometer_sensor().num_samples()}\n"
                  f"the names of the dataframe columns: {station.magnetometer_sensor().data_channels()}\n")

        # Magnetometer has 3 channels - x, y and z
        magnetometer_x_samples = station.magnetometer_sensor().get_magnetometer_x_data()
        magnetometer_y_samples = station.magnetometer_sensor().get_magnetometer_y_data()
        magnetometer_z_samples = station.magnetometer_sensor().get_magnetometer_z_data()
        # The channels share the same timestamps
        magnetometer_time_micros = station.magnetometer_sensor().data_timestamps() - \
                                    station.magnetometer_sensor().first_data_timestamp()
        magnetometer_time_s = magnetometer_time_micros*MICROS_TO_S

        # Plot the acceleration data - one subplot per channel
        fig, ax = plt.subplots(nrows=3, ncols=1, sharex='col')
        ax[0].plot(magnetometer_time_s, magnetometer_x_samples)
        ax[1].plot(magnetometer_time_s, magnetometer_y_samples)
        ax[2].plot(magnetometer_time_s, magnetometer_z_samples)

        # Set labels and subplot title
        ax[0].set_ylabel('Mag X [m/s]')
        ax[1].set_ylabel('Mag Y [m/s]')
        ax[2].set_ylabel('Mag Z [m/s]')
        ax[2].set_xlabel(f"Seconds from {int(dw.start_date()*MICROS_TO_S)} Unix epoch UTC")

        plt.suptitle(f"RedVox Station ID {station.id()}")

    plt.show()

    print('Visit https://github.com/RedVoxInc/redvox-python-sdk/tree/master/docs/python_sdk/data_window/station#using-station'
          'for more information on sensors available')


if __name__ == "__main__":
    main()

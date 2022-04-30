"""
Start from report page at:
https://redvox.io/#/reports/E328

Load metadata and state of health data from:
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
input_file = "dw_1648830257000498_2.pkl.lz4"


def main() -> None:
    # Load datawindow from report
    dw = DataWindow.deserialize(os.path.join(input_dir, input_file))

    print("\nAll native timestamps are in microseconds since Unix epoch UTC")
    for station in dw.stations():
        # print some metadata
        print(f"Station {station.id()} Metadata:\n"
              f"station description: {station.metadata().station_description}\n"
              f"is station private: {station.metadata().is_private}\n"
              f"station make: {station.metadata().make}\n"
              f"station model: {station.metadata().model}\n"
              f"station os: {station.metadata().os}\n"
              f"station os version: {station.metadata().os_version}\n"
              f"redvox app version:  {station.metadata().app_version}\n"
              f"redvox packet duration in seconds: {station.metadata().packet_duration_s}\n")

        # Check that there is state of health data
        if station.has_health_sensor():
            print(f"Station {station.id()} Health Sensor:\n"
                  f"sample rate in hz: {station.health_sensor().sample_rate_hz()}\n"
                  f"sample interval in seconds: {station.health_sensor().sample_interval_s()}\n"
                  f"sample interval std dev: {station.health_sensor().sample_interval_std_s()}\n"
                  f"the first data timestamp: {station.health_sensor().first_data_timestamp()}\n"
                  f"the last data timestamp:  {station.health_sensor().last_data_timestamp()}\n"
                  f"the number of data samples: {station.health_sensor().num_samples()}\n"
                  f"the names of the dataframe columns: {station.health_sensor().data_channels()}\n")

            # Get some state of health data - example of what is available
            power_state = station.health_sensor().get_power_state_data()
            battery_charge_percentage = station.health_sensor().get_battery_charge_remaining_data()
            internal_temp_c = station.health_sensor().get_internal_temp_c_data()

            # The channels share the same timestamps
            health_time_micros = station.health_sensor().data_timestamps() - \
                                    station.health_sensor().first_data_timestamp()
            health_time_s = health_time_micros*MICROS_TO_S

            # Plot the state of health data - one subplot per channel
            fig, ax = plt.subplots(nrows=3, ncols=1, sharex='col')

            ax[0].plot(health_time_s, power_state)
            ax[1].plot(health_time_s, battery_charge_percentage)
            ax[2].plot(health_time_s, internal_temp_c)

            # Set labels and subplot title
            ax[0].set_ylabel('Power State')
            ax[1].set_ylabel('Batt. %')
            ax[2].set_ylabel('Int. temp. [C]')
            ax[2].set_xlabel(f"Seconds from {int(dw.start_date()*MICROS_TO_S)} Unix epoch UTC")
            plt.suptitle(f"RedVox Station ID {station.id()}")

    plt.show()


if __name__ == "__main__":
    main()

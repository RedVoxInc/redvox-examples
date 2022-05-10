"""
Start from report page at:
https://redvox.io/#/reports/E328

Plot report audio wiggles from:
Time aligned and corrected data window

For more information on plotting other sensors and options, visit the RedPandas Docs:
https://github.com/RedVoxInc/redpandas/blob/master/docs/redpandas/advance_use_redpandas.md#how-to-use-redpandas---advanced-data-manipulation

"""
import os
from matplotlib import pyplot as plt
from redvox.common.data_window import DataWindow
from redpandas.redpd_df import redpd_dataframe
from redpandas.redpd_plot.wiggles import plot_wiggles_pandas

print(__doc__)

# CONSTANT: Convert from native microseconds to seconds
MICROS_TO_S = 1E-6

# Change input_dir the path of your data directory
# input_dir = "/CHANGE/ME/DATA_2022/REDVOX_EXAMPLES"
# Example:
input_dir = "/Users/mgarces/Documents/DATA_2022/REDVOX_EXAMPLES"

# Name of the RedVox datawindow file you downloaded:
INPUT_FILE = "dw_1648830257000498_2.pkl.lz4"


def main() -> None:
    # First load datawindow from report
    dw = DataWindow.deserialize(os.path.join(input_dir, INPUT_FILE))

    # Make a pandas DataFrame, where crucial information from DataWindow is extracted
    # In this case, we are only extracting 'audio' from the DataWindow but other sensors such as 'barometer',
    # 'accelerometer', 'gyroscope', 'magnetometer', 'health', or 'location' are possible
    rp_df = redpd_dataframe(input_dw=dw,
                            sensor_labels=['audio'])
    print(f'Available columns in RedPandas:\n{rp_df.columns.values}')

    # Plot wiggles
    plot_wiggles_pandas(df=rp_df,  # the name of the redpandas dataframe, in this case rp_df
                        sig_wf_label='audio_wf',  # Column label with sensor data, in this case audio
                        sig_timestamps_label='audio_epoch_s',  # Column label with timestamps data
                        sig_id_label='station_id'  # name of column with the ID/names of stations.
                        # Important for setting the y_ticks
                        )

    plt.show()


if __name__ == "__main__":
    main()

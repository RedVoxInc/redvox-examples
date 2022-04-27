# Example 02: Other sensors in the RedVox report DataWindow

Load other sensors available in DataWindow such as barometer, gyroscope and magnetometer among others.
For more information on sensors available, visit the
[RedVox SDK Station Documentation](https://github.com/RedVoxInc/redvox-python-sdk/tree/master/docs/python_sdk/data_window/station#using-station).

Single channel sensors such as barometer load similar to audio (as seen in example ex_00_report_audio), multichannel 
sensors such as gyroscope or magnetometer load similar to the accelerometer sensors 
(as seen in example ex_01_report_accelerometer).

### Setup

See requirements.txt

### Obtaining Data

Start from report page at:
https://redvox.io/#/reports/redvoxcore@12Apr22.02.48.36

Must log into the webpage as `redvoxcore`.

Download:
Time aligned and corrected data window.
Place compressed, serialized dw.xxx.pkl.lz4 file in a folder outside the repository

### Running the Example

Change input_dir to point to your data directory
input_dir = "YOUR_DIRECTORY_PATH"

### Example Output

Link to figure(s)

# Example 00: Audio waveforms from RedVox report DataWindow

Load an audio waveform data from a time aligned and corrected data window in a RedVox Report

For more information on getting started with the RedVox SDK, visit the 
[RedVox SDK Manual](https://github.com/RedVoxInc/redvox-python-sdk/tree/master/docs/python_sdk#-redvox-python-sdk-manual).

### Setup

You will need the RedVox SDK to run this example. The SDK can be installed by running:
```shell
pip install redvox==3.1.13
```
in a terminal with python enabled.

For more instructions on installing the SDK, please visit 
[RedVox SDK Installation](https://github.com/RedVoxInc/redvox-python-sdk/blob/master/docs/python_sdk/installation.md#-redvox-sdk-installation).

You will also need the Matplotlib library to plot the graphs. You can find installation instructions in 
[Matplotlib Installation](https://matplotlib.org/stable/users/installing/index.html). 

### Obtaining Data

Start from report page at:
https://redvox.io/#/reports/E328

In Additional Products, click the `Time aligned and corrected data window` link.

<p align="center">
<img src="img/additional_products_img.png" width="650">
</p>

A file named `dw_1648830257000498_2.pkl.lz4` will start to download. 

### Running the Example

In load_audio.py, change input_dir (line 19) to the directory where the downloaded file 
`dw_1648830257000498_2.pkl.lz4` is located.

### Example Output

<p align="center">
<img src="img/fig_ex_00.png">
</p>




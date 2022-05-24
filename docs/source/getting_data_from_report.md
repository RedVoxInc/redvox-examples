# Getting Started

## Python setup

You will need the [RedVox SDK](https://github.com/RedVoxInc/redvox-python-sdk#redvox-python-sdk) to run this example. 
The SDK can be installed by running:
```shell
pip install redvox==3.2.0
```
in a terminal with Python enabled. 

You will also need the [RedPandas](https://github.com/RedVoxInc/redpandas#redpandas) library which can be installed with:
```shell
pip install redpandas==1.3.5
```
For more instructions on installing these libraries, please visit
[RedVox SDK Installation](https://github.com/RedVoxInc/redvox-python-sdk/blob/master/docs/python_sdk/installation.md#-redvox-sdk-installation)
and
[RedPandas Installation](https://github.com/RedVoxInc/redpandas/blob/master/docs/redpandas/installation.md#redpandas-installation).

You can confirm everything is installed correctly by running this Python script:
```python
import redvox
import redpandas

if __name__ == "__main__":
    print("Redvox version: ", redvox.version())
    print("RedPandas version: ", redpandas.version())
```
If there are no errors, you will see the version numbers printed to the screen.

## Obtaining Data

We will be using a dataset recorded during a SpaceX launch to showcase the examples. The data is located in the RedVox report:
[https://redvox.io/#/reports/E328](https://redvox.io/#/reports/E328)

In _Additional Products_, click the `Time aligned and corrected data window` link.

![](../img/additional_product_img.jpg)

A file named `dw_1648830257000498_2.pkl.lz4` will start to download.

> **_NOTE:_** All the examples in the following section (FROM A REDVOX REPORT, HOW TO...)
> use this dataset. 

We are done setting up! Now we can start [loading the audio data](00_audio_from_report.md) in the next section.





# Getting started

The first steps are to set up the Python requirements and obtain the test data.

## Setup

You will need the [RedVox SDK](https://github.com/RedVoxInc/redvox-python-sdk#redvox-python-sdk) to run this example. 
The SDK can be installed by running:
```shell
pip install redvox==3.2.0
```
in a terminal with Python enabled. For more instructions on installing the SDK, please visit
[RedVox SDK Installation](https://github.com/RedVoxInc/redvox-python-sdk/blob/master/docs/python_sdk/installation.md#-redvox-sdk-installation).

You will also need the [RedPandas](https://github.com/RedVoxInc/redpandas#redpandas) library which can be installed with:
```shell
pip install redpandas==1.3.5
```
For more instructions on installing RedPandas, please visit
[RedPandas Installation](https://github.com/RedVoxInc/redpandas/blob/master/docs/redpandas/installation.md#redpandas-installation).


## Obtaining Data

The data is located in a RedVox Report:
[https://redvox.io/#/reports/E328](https://redvox.io/#/reports/E328)

In _Additional Products_, click the `Time aligned and corrected data window` link.

![](../img/additional_products_img.png)

A file named `dw_1648830257000498_2.pkl.lz4` will start to download.

We are done setting up! Now we can start [loading the Audio data](00_audio_from_report.md) in the next section.





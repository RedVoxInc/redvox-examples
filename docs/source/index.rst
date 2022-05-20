.. RedVox Examples documentation master file, created by
   sphinx-quickstart on Thu May 19 09:59:17 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


RedVox Examples
===========================================

Welcome to RedVox Examples!

This is a space for examples of the `RedVox SDK <https://github.com/RedVoxInc/redvox-python-sdk>`_,
`RedPandas <https://github.com/RedVoxInc/redpandas>`_, and `redvox.io <https://redvox.io/#/home>`_, that aim to serve as
tutorials.

**Setup**

- :doc:`prereqs`
- :doc:`getting_data_from_report`


**Related to RedVox SDK**

- :doc:`00_audio_from_report`
- :doc:`01_accelerometer_from_report`
- :doc:`02_other_sensors_from_report`
- :doc:`03_metadata_soh_from_report`

**Related to RedPandas**

- :doc:`04_plot_wiggles`
- :doc:`05_plot_spectrogram`

**Related to redvox.io**

- :doc:`06_get_yamnet_classifications`
- :doc:`07_use_yamnet_csv`

Basic definitions
------------------

The following terms are common terminology used throughout this Documentation.


- **RedVox**: Not the NYC based rock band. RedVox refers to products developed by `RedVox, Inc. <http://nelha.hawaii.gov/our-clients/redvox/>`_.

- **RedVox Infrasound Recorder**: A smartphone app that can record audio and other stimuli such as pressure.
  Visit `RedVox Sound <https://www.redvoxsound.com>`_ to learn more about the app.

- **RedVox Python SDK**: A Software Development Kit (SDK) developed to read, create, edit, and write RedVox files
  (files ending in `.rdvxz` for `RedVox API 900 <https://bitbucket.org/redvoxhi/redvox-protobuf-api/src/master/>`_
  files and `.rdvxm` for `RedVox API 1000 <https://github.com/RedVoxInc/redvox-api-1000>`_ files). Visit
  `GitHub RedVox Python SDK <https://github.com/RedVoxInc/redvox-python-sdk>`_ to learn more about the SDK.

- **RedPandas**: short for `RedVox Pandas <https://pypi.org/project/redvox-pandas/>`_, a pipeline to process RedVox data
  based in the `Pandas library <https://pandas.pydata.org/>`_.

- **Station**: a device used to record data, e.g., a smartphone recording infrasound waves using the
  `RedVox Infrasound Recorder <https://www.redvoxsound.com/>`_ app. Also a Python class designed in the RedVox Python SDK to
  store station and sensor data. Visit
  `Station Documentation <https://github.com/RedVoxInc/redvox-python-sdk/tree/master/docs/python_sdk/data_window/station>`_
  for more information on the Station Python class. A station has sensors (see below).

- **Sensor**: a device that responds to a physical stimulus, e.g., barometer, accelerometer. The units for each available sensor can
  be found in `RedVox SDK Sensor Documentation <https://github.com/RedVoxInc/redvox-python-sdk/tree/master/docs/python_sdk/data_window/station#sensor-data-dataframe-access>`_.
  A station should always have audio sensor (and hence audio data).

- **Epoch** or **epoch time**: unix time (also referred to as the epoch time), the number of seconds since 1 January 1970.
  The RedPandas' native unit of time is UTC epoch time in seconds. For example the epoch time for Thursday, July 1, 2021 at 9:00:00 am
  UTC would be 1625130000.

.. toctree::
   :maxdepth: 2
   :caption: Before Starting...
   :hidden:

   prereqs
   getting_data_from_report

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: From a RedVox Report, How To...

   00_audio_from_report
   01_accelerometer_from_report
   02_other_sensors_from_report
   03_metadata_soh_from_report
   04_plot_wiggles
   05_plot_spectrogram

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: For redvox.io, How To...

   06_get_yamnet_classifications
   07_use_yamnet_csv

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: For more information:

   what_to_do_next



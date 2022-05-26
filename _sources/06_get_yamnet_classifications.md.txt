# Get YAMNet Classifications

The [RedVox webpage](https://redvox.io) provides facilities for both extracting edge computed ML with TensorFlow Lite and performing cloud computed ML with full TensorFlow.

## RedVox Account

In order to use these features, you must be using a RedVox account that has the `RedVox` tier and the `YamNet` feature enabled. 
Accounts that meet these requirements include `redvoxcore` and `redvoxtesting4`.

Contact [Redvox Support](mailto:support@redvox.io) to include these features in another account.

## Enabling Edge YAMNet

Once the Android or iOS app is installed, setup, and logged in with an appropriate account, it's possible to enable YAMNet.

Edge based YAMNet can be enabled at any audio sampling rate.

### Android

Select the settings dropdown.

![](../img/android_settings_0.png)

Select the Settings button.

![](../img/android_settings_1.png)

Scroll down to the YAMNet settings and click "Enable YAMNet".

![](../img/android_settings_2.png)

It's also a good idea to ensure the app has the latest model by selecting "YAMNet Model".

![](../img/android_settings_3.png)

To check that it's working, go back to the audio screen and start recording. Make some noises and you should see annotations appearing in the audio plot and specgtrogram.

![](../img/android_live.png)

### iOS

Select the settings icon.

![](../img/ios_settings_0.png)

Scroll down to the Machine Learning Settings and select "Enable YamNet".

![](../img/ios_settings_1.png)

To check that it's working, go back to the audio screen and start recording. Make some noises and you should see annotations appearing in the audio plot.

![](../img/ios_live.png)

## YAMNet on the edge and in the cloud

It's possible to view edge based predictions using the RedVox cloud interface.

First, log into the redvox.io webpage with the username you recorded data with. Navigate to the Dashboard, select the station(s) you want to extract the edge ML from, select a time window, and click "Generate Report for Selected".

![](../img/dashboard_select.png)

Once the report finishes building, navigate to it by clicking the report link.

![](../img/dashboard_report.png)

### Extracting edge predictions

Once a report is made, the edge based predictions can be extracted.

Click "Edit Report".

![](../img/edit_report.png)

Then select "Extract Edge ML".

![](../img/extract_edge_yamnet.png)

Wait for the augmentation to complete with the following message.

![](../img/augmentation_complete.png)

Finally, refresh the page. This will produce two new products. A CSV file containing the entire prediction timeline for each station and a figure that shows the top two predictions for each station.

![](../img/web_edge_products.png)

### Performing cloud predictions

Full tensorflow models can also be ran within the cloud environment. Since cloud ML is performed on the audio provided, it works best with 16 kHz audio, however, other sampling rates will be resampled to 16 kHz. Resampling may affect results.

To generate edge predictions, generate a report for the target stations and target time window as described in the previous section.

Once a report is made, the cloud based predictions can be added.

Click "Edit Report".

![](../img/edit_report.png)

Then select "YamNet ML".

![](../img/run_cloud_yamnet.png)

Wait for the augmentation to complete with the following message. This will generally take longer than just extracting edge results.

![](../img/augmentation_complete.png)

Finally, refresh the page. This will produce two new products. A CSV file containing the entire prediction timeline for 
each station and a figure that shows the top two predictions for each station.

![](../img/web_cloud_products.png)

Download the CSV file to your computer.

![](../img/location_csv.png)

Next, we will look at [an example that uses the CSV file to display some basic information about the YAMNet data](07_use_yamnet_csv.md).

# Road-Monitoring-Device

## `test`

This folder includes test programs which test only a specific functionality as specified within the test. **All tests are successful unless specified.**

### `python`

This subfolder includes Python-specific tests which act as tutorials. 

The purpose for this folder is to familiarise with Python, as the lead programmer has little Python experience and is unfamiliar with the language.

### `1_pydrive`

Uploads a file to Google Drive after program execution.

### `2_camera`

Initialises, configures, and takes a still picture using the camera. Also saves it using PIL.

### `3_time`

Obtains Unix epoch time from OS and converts to human-readable form.

### `4_serial_for_gps`

Prints out what is received from the serial port connected to the GPS module.

### `5_parser`

Parse NMEA GPS sentence.

### `6_mock_geotag` (FAILED)

Tries to geotag the .jpeg's exif, but fails due to encoding issues of the Pi camera images being saved. Just stuff the coords into the image filenames instead.

### `7_drive_folder`

Tries to create a folder on GDrive and upload a test file into the folder via PyDrive.

### `X_machine_vision`

Performs machine vision on pre-determined dataset as if Pi took the pictures.
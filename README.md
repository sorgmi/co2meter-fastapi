# CO2meter with FastAPI
Show a Dashboard with Co2 level and temperature readings from a USB Co2 Meter

This code is based on [https://github.com/vfilimonov/co2meter](https://github.com/vfilimonov/co2meter).
The Code is migrated to FastAPI (instead of Flask).


### Installation

	pip install -r requirements.txt

### Usage
First test if the co2 meter is connected and we can get measurements. If your device sends encrypted data set ```bypass_decrypt=False```

    python test_device_connection.py  

        {'vendor_id': 1241, 'product_id': 41042, 'path': b'\\\\?\\HID#VID_04D9&PID_A052#7&393b50b7&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}', 'manufacturer': 'Holtek', 'product_name': 'USB-zyTemp', 'serial_no': '2.00'}
                            co2    temp
        2022-12-27 17:59:46  857  20.225

If this works, start the web server with:

    python server.py  # add option -b if your device sends unencrypted data


![Screenshot - dash web-server](https://user-images.githubusercontent.com/1324881/36342020-0c2df1ac-13f8-11e8-978a-b1e3e92a3ea4.png)

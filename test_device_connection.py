'''
Test if the device is connected and read current co2 level and temperature
'''
import co2meter as co2
mon = co2.CO2monitor(bypass_decrypt=True)
print(mon.info)
print(mon.read_data())

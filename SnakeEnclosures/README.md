# Snake Enclosures
## Description:
Blueprints for automating a Snake Enclosure.  Using a smart plug to cycle on and off for heat, and smart plugs for lighting.

## Requirements:
- Climate integration (I use Versatile Thermostat)
  - Use the following presets:
    - "Comfort" - Day time temperature
    - "Eco" - Night time temperature
- Switches for lights, They'll be turned on and off at the beginning of day and beinning of night.
- Helpers:
  - Name: Day Start Time
     - Type: input_datetime (Date and/or time)
  - Name: Night Start Time
    - Type: input_datetime (Date and/or time)
  - Name: Day Start Time Tomorrow
    - Type: input_datetime (Date and/or time)
  - Name: Night Start Time Tomorrow
    - Type: input_datetime (Date and/or time)
  - Name: Natural Heat Schedule Enabled
    - Type: input_boolean (Toggle)
  - Name: Thermostat Bypass
    - Type: input_boolean (Toggle)
  - Name: Lights Bypass
    - Type: input_boolean (Toggle)
- Sun2 integration
  - Set this to the GPS coordinates you'd like your sun rise / sun set to pull from.

## Additional Info
There is a python script in the SnakeEnclosureHelperCreator directory that will generate the code to create all the helpers via config file (if you don't want to make them all manually through the UI) 

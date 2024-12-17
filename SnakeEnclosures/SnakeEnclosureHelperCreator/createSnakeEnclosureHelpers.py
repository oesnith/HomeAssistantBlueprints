import argparse


# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-s", "--SnakeName", action='append', help = "Snake Enclosure Name", nargs='+')

# Read arguments from command line
args = parser.parse_args()

#if args.SnakeName:
    #print("Displaying Output as: % s" % args.SnakeName)
if not args.SnakeName:
    print("Missing argument: -s \"Snake Name\"")
    quit()

print(f"""#####################################################################
# Add the following to the configuration.yaml file.  If there
# is already an input_datetime section, add them to that,
# otherwise create a new one.  Do the same with the input_boolean.
#####################################################################""")

print(f"######input_datetime Helpers:")
print(f"input_datetime:")

for name in args.SnakeName:
    nameLower = str(name[0]).replace(" ", "_").lower()
    nameNoSpace = str(name[0]).replace(" ", "_")

    print(f"""
  # {name[0]} - Day Start Time Tomorrow Helper
  {nameLower}_day_time_start_tomorrow:
    name: {name[0]} Day Time Start - Tomorrow
    has_date: false
    has_time: true

  # {name[0]} - Night Start Time Tomorrow Helper
  {nameLower}_night_time_start_tomorrow:
    name: {name[0]} Night Time Start - Tomorrow
    has_date: false
    has_time: true

  # {name[0]} - Day Start Time Helper
  {nameLower}_day_time_start:
    name: {name[0]} Day Time Start
    has_date: false
    has_time: true

  # {name[0]} - Night Start Time Helper
  {nameLower}_night_time_start:
    name: {name[0]} Night Time Start
    has_date: false
    has_time: true
""")

print(f"#####input_boolean Helpers:")
print(f"input_boolean:")
for name in args.SnakeName:
    nameLower = str(name[0]).replace(" ", "_").lower()
    nameNoSpace = str(name[0]).replace(" ", "_")

    print(f"""
  # {name[0]} - Natural Heat Schedule Enabled
  {nameLower}_natural_heat_schedule_enabled:
    name: {name[0]} Natural Heat Schedule Enabled

  
  # {name[0]} - Thermostat Bypass 
  {nameLower}_thermostat_bypass:
    name: {name[0]} Thermostat Bypass
    icon: mdi:alpha-x-box-outline

  # {name[0]} - Lights Bypass 
  {nameLower}_lights_bypass:
    name: {name[0]} Lights Bypass
    icon: mdi:alpha-x-box-outline

        """)

#Name: Day Start Time
#Type: input_datetime (Date and/or time)
#Name: Night Start Time
#Type: input_datetime (Date and/or time)
#Name: Day Start Time Tomorrow
#Type: input_datetime (Date and/or time)
#Name: Night Start Time Tomorrow
#Type: input_datetime (Date and/or time)
#Name: Natural Heat Schedule Enabled
#Type: input_boolean (Toggle)

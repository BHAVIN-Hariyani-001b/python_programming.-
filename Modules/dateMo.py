import datetime as date  # Importing datetime module (renamed as 'date' for convenience)

# ------------------------------
# Get Current Date and Time
# ------------------------------
# datetime.datetime.now() gives the current date & time
now = date.datetime.now()
print(now)  # Example output: 2025-08-14 10:45:23.123456

# ------------------------------
# Get Only Date or Only Time
# ------------------------------
print(now.date())  # Extract only date → 2025-08-14
print(now.time())  # Extract only time → 18:24:31.319056

# ------------------------------
# Custom Formatting using strftime()
# ------------------------------
# strftime() converts datetime object to a string in a given format
# Common format codes:
#   %Y → Year (2025)
#   %m → Month (08)
#   %d → Day (14)
#   %H → Hour (24-hour format)
#   %M → Minute
#   %S → Second
print(now.strftime("%Y-%m-%d"))         # Output: 2025-08-14
print(now.strftime("%d/%m/%Y %H:%M"))   # Output: 14/08/2025 18:24
print(date.datetime.now().strftime("%Y-%m-%d"))  # Direct call without storing in variable

# ------------------------------
# Date Arithmetic (Add/Subtract Days)
# ------------------------------
# timedelta is used to perform date/time calculations
tomorrow = now + date.timedelta(days=1)      # Add 1 day
yesterday = now - date.timedelta(days=1)     # Subtract 1 day
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)

# ------------------------------
# Get Today’s Date (Only Date, no time)
# ------------------------------
print(date.date.today())  # Output: 2025-08-14

# ------------------------------
# ISO 8601 Format
# ------------------------------
# isoformat() returns a string like 'YYYY-MM-DDTHH:MM:SS.ssssss'
print(now.isoformat())  # Example: 2025-08-14T18:24:31.319056

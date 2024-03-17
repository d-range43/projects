## Get hours minutes seconds function:

def getHoursMinutesSeconds(totalSeconds):
    """
    Converts time in seconds into Hours, Minutes, Seconds format.

    Args:
        totalSeconds (integer): number of seconds to convert.

    Returns:
        Time in Hours, Minutes, Seconds (str) : '0s', '4h 6m 2s', '1h 4m'

    """

    # If totalSeconds is 0 return "0s":
    if totalSeconds == 0:
        return "0s"
    
    # Set hours and minutes to 0 by default:
    hours = 0
    minutes = 0
    
    # Set hours to how many times 3600 can divide totalSeconds, 
    # then set totalSeconds as the remainder.
    if totalSeconds >= 3600:
        hours = totalSeconds // 3600
        totalSeconds = totalSeconds % 3600
    else:
        hours = 0
    # Set minutes to how many times 60 seconds can divide
    # totalSeconds. Then set totalSeconds to the remainder:
    if totalSeconds >= 60:
        minutes = totalSeconds // 60
        totalSeconds = totalSeconds % 60
    else:
        minutes = 0
    
    # Set seconds to the remaining totalSeconds value:
    seconds = totalSeconds

    # Create an hms list that contains the string hour/minute/second amounts:
    hms = []
    # If there are one or more hours, add the amount with an 'h' suffix:
    if hours > 0:
        hms.append(str(hours) + 'h')
    # If there are one or more minutes, add the amount with an 'm' suffix:
    if minutes > 0:
        hms.append(str(minutes) + 'm')
    # If there are one or more seconds, add the amount with an 's' suffix:
    if seconds > 0:
        hms.append(str(seconds) + 's')

    # Join the hour/minute/second strings with a space in between them:
    return ' '.join(hms)
   
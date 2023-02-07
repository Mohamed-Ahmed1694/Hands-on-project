import psutil
#check_disk_usage
def check_disk_usage(threshold):
    usage = psutil.disk_usage("/").percent
    if usage > threshold:
        return False
    return True

if not check_disk_usage(75):
    print("ERROR: Disk usage is above the threshold.")
else:
    print("Everything is normal.")

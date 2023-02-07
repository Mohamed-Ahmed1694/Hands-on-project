import shutil

def check_disk_usage(threshold):
    total, used, free = shutil.disk_usage("/")
    usage = (used / total) * 100
    if usage > threshold:
        return True
    return False

if check_disk_usage(75):
    print("ERROR: Disk usage is above the threshold.")
else:
    print("Everything is normal.")

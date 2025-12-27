import psutil

def cpu_health_check():
    threshold = int(input("Enter the Threshold for CPU usage:  "))
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU utilization is : {cpu_usage} % ")

    if threshold > cpu_usage:
        print("Everything is fine. \nNo Steps to take ")
    else:
        print("Generating Email Alert ......")

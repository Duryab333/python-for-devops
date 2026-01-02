import psutil  

def cpu_health_check():

    cpu_threshold = float(input("Enter the Threshold for CPU usage:  "))
    mem_threshold = float(input("Enter the Threshold for memory Alert :"))
    disk_threshold = float(input("Enter disk Threshold :"))
    
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    
    print("\n--- Current System Metrics ---")
    print(f"CPU Usage : {cpu_usage} % ")
    print(f"memory Usage : {mem_usage} % ")
    print(f"Disk Usage : {disk_usage}")

    print("\n--- Health Check Result ---")

  

    if cpu_usage > cpu_threshold:
        print("CPU usage is within limit ")  
    else:
        print("CPU usage is above threshold! \n  Generating Email ....")

    if mem_usage > mem_threshold:
        print("memory usage is within limit ")  
    else:
        print("memory usage is above threshold! \n  Generating Email ....")

    if disk_usage > disk_threshold:
        print("Disk usage is within limit ")  
    else:
        print("Disk usage is above threshold! \nGenerating Email ....")

cpu_health_check()

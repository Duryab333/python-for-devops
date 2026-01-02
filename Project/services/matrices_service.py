import psutil


def get_system_metics():
    """
    This API get System Metics (CPU, Memory, Disk, System Health)
    Based on CPU threshold i.e 10 (configurable)

    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent
    cpu_threshold= 10

    status = "High CPU" if cpu_percent > cpu_threshold else "Healthy"

    return {
        "cpu_percentage": cpu_percent,
        "memory_percent": memory_percent,
        "disk_percent": disk_percent,
        "cpu_threshold": cpu_threshold,
        "status": status


    }

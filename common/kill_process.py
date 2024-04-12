import subprocess
import os
import platform


def kill_process():
    os_item = platform.system()
    if os_item == "Windows":
        print("您的操作系统为 Windows")
        kill_process_windows()
    elif os_item == "Linux":
        print("您的操作系统为 Linux")
        kill_process_linux()
    elif os_item == "Darwin":
        print("您的操作系统为 Mac OS")
        kill_process_mac()
    else:
        print(f"Unknown OS: {os_item}")
        exit(1)


def kill_process_mac():
    # 查找特定的进程名称
    ps_command = "ps aux | grep Chromium | grep -v grep | awk '{print $2}'"
    out = subprocess.getoutput(ps_command)
    # 解析出进程ID
    pids = out.split("\n")
    for pid_str in pids:
        if pid_str:
            try:
                pid = int(pid_str)
                # 结束进程
                kill_command = f"kill {pid}"
                subprocess.run(kill_command, shell=True)
                print(f"Process {pid} killed")
            except ValueError:
                print(f"Invalid PID: {pid_str}")


def kill_process_linux():
    # 查找特定的进程名称
    cmd = "ps aux | grep chromium | grep -v grep | awk '{print $2}' | xargs kill -9"
    out = subprocess.getoutput(cmd)
    print(f"Process killed: {out}")


def kill_process_windows():
    # 执行任务列表命令获取进程信息
    out = subprocess.getoutput("tasklist /NH")
    # 解析出进程ID
    processes = out.split("\n")
    for process in processes:
        if "chromium" in process.lower() or "chrome" in process.lower():
            fields = process.split()
            if len(fields) >= 2:
                pid_str = fields[1]
                try:
                    pid = int(pid_str)
                    # 结束进程
                    subprocess.run(["taskkill", "/F", "/PID", str(pid)])
                    print(f"Process {pid} killed")
                except ValueError:
                    print(f"Invalid PID: {pid_str}")

# if __name__ == "__main__":
#     kill_process()

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

# 监控目录（修改为你的 Excel 文件夹路径）
watch_directory = "D:/工作/Jing/github-tasks"  # 改成你的文件夹路径


class ExcelSaveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # 当 Excel 文件被修改时，运行生成 MD 的 Python 脚本
        if event.src_path.endswith("tasks.xlsx"):
            print("Excel 文件更新，开始生成 MD 文件...")
            subprocess.run(["python", "D:/工作/Jing/github-tasks/excel_to_md.py"])  # 替换成你的脚本路径




if __name__ == "__main__":
    event_handler = ExcelSaveHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_directory, recursive=False)

    print("开始监控 Excel 文件夹...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
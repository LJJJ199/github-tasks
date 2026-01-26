import pandas as pd
from pathlib import Path

# ====== 1. 路径配置 ======
BASE_DIR = Path(__file__).parent
EXCEL_PATH = BASE_DIR / "tasks.xlsx"
MD_DIR = BASE_DIR / "md"
MD_DIR.mkdir(exist_ok=True)

# ====== 2. 读取 Excel ======
df = pd.read_excel(EXCEL_PATH).fillna("")

# ====== 3. 全量任务（原样镜像） ======
(df.to_markdown(index=False)
   and (MD_DIR / "tasks_all.md")
   .write_text(df.to_markdown(index=False), encoding="utf-8"))

# ====== 4. 待办任务（不是 已完成 且不是 已逾期）=====
todo_df = df[~df["系统判断状态"].isin(["已完成", "已逾期"])]
(MD_DIR / "tasks_todo.md").write_text(
    todo_df.to_markdown(index=False), encoding="utf-8"
)

# ====== 5. 已完成 ======
done_df = df[df["系统判断状态"] == "已完成"]
(MD_DIR / "tasks_done.md").write_text(
    done_df.to_markdown(index=False), encoding="utf-8"
)

# ====== 6. 已逾期 ======
overdue_df = df[df["系统判断状态"] == "已逾期"]
(MD_DIR / "tasks_overdue.md").write_text(
    overdue_df.to_markdown(index=False), encoding="utf-8"
)

# ====== 7. 控制台提示（仅用于人类确认导出结果） ======
print("✅ Markdown 已生成：")          # 总提示：导出流程已完成
print(" - tasks_all.md")               # 全量任务（完整数据库快照）
print(" - tasks_todo.md")              # 待办任务（Agent 主用）
print(" - tasks_done.md")              # 已完成任务（复盘 / 归档）
print(" - tasks_overdue.md")           # 已逾期任务（风险 / 提醒）

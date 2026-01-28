import subprocess
from pathlib import Path

# 仓库目录（就是你现在这个项目）
REPO_DIR = Path(r"D:\工作\Jing\github-tasks")

print("📥 正在从 GitHub 拉取最新内容...")

result = subprocess.run(
    ["git", "pull", "origin", "main"],
    cwd=REPO_DIR,
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.stderr)

print("✅ GitHub 同步完成")

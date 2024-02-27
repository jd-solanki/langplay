from pathlib import Path

downloads_dir = Path.home() / "Downloads"

curr_dir = Path(__file__).parent
repo_dir = curr_dir.parent
projects_dir = repo_dir.parent.parent

models_dir = downloads_dir / "models"


vuexy_vue_repo_dir = projects_dir / "clevision" / "vuexy" / "vue"
vuexy_vue_docs_dir = vuexy_vue_repo_dir / "docs"
vuexy_vue_ts_full_dir = projects_dir / "clevision" / "vuexy" / "vue" / "typescript-version" / "full-version"

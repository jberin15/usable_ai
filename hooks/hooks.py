import os
from bs4 import BeautifulSoup

def on_files(files, config):
    """
    Ensure all notebook files are processed and their Markdown versions include our header.
    """
    for file in files:
        if file.src_path.endswith(".ipynb"):
            notebook_path = file.src_path
            md_path = file.dest_path.replace(".ipynb", ".md")

            repo_url = "https://github.com/filipinascimento/usable_ai/blob/main/"
            colab_url = "https://colab.research.google.com/github/filipinascimento/usable_ai/blob/master/"
            
            colab_link = f"{colab_url}{notebook_path}"
            github_link = f"{repo_url}{notebook_path}"

            prepend_content = f"""
<table class="m01-notebook-buttons" align="left">
  <td>
    <a target="_blank" href="{colab_link}">
      <img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Run in Google Colab
    </a>
  </td>
  <td>
    <a href="{github_link}">
      <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />View on Github
    </a>
  </td>
</table>

<br clear="all">

"""

            # Modify the markdown output of notebooks
            full_md_path = os.path.join(config['site_dir'], md_path)

            print("Modifying", full_md_path)
            if os.path.exists(full_md_path):
                with open(full_md_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # the content needs to be added before the first <h1> tag
                    soup = BeautifulSoup(content, 'html.parser')
                    h1 = soup.find("h1")
                    if h1:
                        h1.insert_before(prepend_content)
                    else:
                        soup.insert(0, prepend_content)
                        

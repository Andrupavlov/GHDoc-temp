"""GIT Help Component for Grasshopper.
    
    This component helps manage documentation for Grasshopper files through Git.
    
    Inputs:
        OPEN_MAIN_BRANCH: Boolean - opens the main repository branch on GitHub
        OPEN_HELP_IN_GITHUB: Boolean - opens the documentation of the current file on GitHub
        OPEN_LOCAL_HELP: Boolean - opens the local .md documentation file in editor
    
    Output:
        md: String - content of the local .md documentation file
    
    Functionality:
    - Automatically finds Git repository
    - Creates .md documentation files in Doc/ folder
    - Opens documentation on GitHub or locally
    - Reads documentation content for display in Grasshopper"""

__author__ = "Andrii Pavlov"
__version__ = "2025.06.30"

import System
import webbrowser
import clr
import os

clr.AddReference("System.Net")
import System.Net

ghenv.Component.Message = "GIT Help v0.001"

REPO_URL = "https://github.com/Andrupavlov/GHDoc-temp"
RAW_URL = "https://raw.githubusercontent.com/Andrupavlov/GHDoc-temp"
SUBFOLDER_IN_REPO = "Doc"

def open_url_in_thread(url):
    def thread_func():
        webbrowser.open(url)
    t = System.Threading.Thread(System.Threading.ThreadStart(thread_func))
    t.IsBackground = True
    t.Start()

def get_gh_filename():
    doc = ghenv.Component.OnPingDocument()
    file_path = doc.FilePath
    if not file_path:
        print("File not saved")
        return None, None

    file_name = os.path.basename(file_path)
    name_without_ext = os.path.splitext(file_name)[0]
    folder = os.path.dirname(file_path)
    return name_without_ext, folder

def find_git_root(start_folder):
    current = start_folder
    while current and current != os.path.dirname(current):
        if os.path.isdir(os.path.join(current, ".git")):
            return current
        current = os.path.dirname(current)
    return None

def get_git_branch(git_root_folder):
    head_path = os.path.join(git_root_folder, ".git", "HEAD")
    if not os.path.exists(head_path):
        print(".git/HEAD does not exist")
        return None

    with open(head_path, "r") as f:
        content = f.read().strip()
        if content.startswith("ref: refs/heads/"):
            return content.replace("ref: refs/heads/", "")
        else:
            return None

def check_github_file_exists(branch, subfolder, filename_no_ext):
    raw_url = RAW_URL + "/" + branch + "/" + subfolder + "/" + filename_no_ext + ".md"
    try:
        req = System.Net.WebRequest.Create(raw_url)
        req.Method = "HEAD"
        resp = req.GetResponse()
        resp.Close()
        return True
    except System.Net.WebException as e:
        if e.Response:
            e.Response.Close()
        return False

def create_md_file_content(filename_no_ext):
    """Creates basic content for a markdown file"""
    return "# " + filename_no_ext + "\n\nDocumentation for " + filename_no_ext + ".gh\n"

def create_local_md_file(git_root, subfolder, filename_no_ext):
    doc_dir = os.path.join(git_root, subfolder)
    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

    md_path = os.path.join(doc_dir, filename_no_ext + ".md")
    if os.path.exists(md_path):
        print("The file already exists locally:", md_path)
        return

    with open(md_path, "w") as f:
        f.write(create_md_file_content(filename_no_ext))
    print("A local .md file has been created:", md_path)
    print("→ Don't forget to commit and push it to GitHub.")

def open_github_doc(base_repo_url, doc_subfolder="Doc"):
    file_name, file_folder = get_gh_filename()
    if not file_name or not file_folder:
        return

    git_root = find_git_root(file_folder)
    if not git_root:
        print("No .git found in directories above")
        return

    branch = get_git_branch(git_root)
    if not branch:
        return

    file_exists = check_github_file_exists(branch, doc_subfolder, file_name)
    if not file_exists:
        print("Markdown file not found on GitHub. Creating locally...")
        create_local_md_file(git_root, doc_subfolder, file_name)

    github_path = base_repo_url + "/blob/" + branch + "/" + doc_subfolder + "/" + file_name + ".md"
    open_url_in_thread(github_path)
    return github_path

def open_local_md_file(doc_subfolder="Doc"):
    file_name, file_folder = get_gh_filename()
    if not file_name or not file_folder:
        return

    git_root = find_git_root(file_folder)
    if not git_root:
        print("No .git found in directories above")
        return

    doc_dir = os.path.join(git_root, doc_subfolder)
    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

    md_path = os.path.join(doc_dir, file_name + ".md")
    if not os.path.exists(md_path):
        with open(md_path, "w") as f:
            f.write(create_md_file_content(file_name))
        print("✅ A local .md file has been created.:", md_path)
        print("→ Don't forget to commit it to git")

    # Open in system editor — IN A SEPARATE FLOW
    def thread_func():
        try:
            System.Diagnostics.Process.Start(md_path)
            print(" Local file opened:", md_path)
        except Exception as e:
            print("Unable to open file:", str(e))

    t = System.Threading.Thread(System.Threading.ThreadStart(thread_func))
    t.IsBackground = True
    t.Start()

def read_local_md_file(doc_subfolder="Doc"):
    file_name, file_folder = get_gh_filename()
    if not file_name or not file_folder:
        return "Error: File not saved"

    git_root = find_git_root(file_folder)
    if not git_root:
        return "Error: No .git directory found"

    doc_dir = os.path.join(git_root, doc_subfolder)
    md_path = os.path.join(doc_dir, file_name + ".md")

    if not os.path.exists(md_path):
        message = "File not found: " + md_path + "\n"
        message += "You need to create an .md file in the directory " + doc_subfolder + " with the name " + file_name + ".md"
        return message

    try:
        with open(md_path, "r") as f:
            content = f.read()
            return content
    except Exception as e:
        return "Error reading .md file: " + str(e)


if OPEN_MAIN_BRANCH:
    open_url_in_thread(REPO_URL)

if OPEN_HELP_IN_GITHUB:
    open_github_doc(REPO_URL, doc_subfolder=SUBFOLDER_IN_REPO)

if OPEN_LOCAL_HELP:
    open_local_md_file(SUBFOLDER_IN_REPO)

md = read_local_md_file(SUBFOLDER_IN_REPO)
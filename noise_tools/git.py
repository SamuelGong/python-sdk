# https://github.com/modelcontextprotocol/servers/tree/main/src/git
from mcp.types import (
    Tool,
)
from enum import Enum
import git
from pydantic import BaseModel


class GitStatus(BaseModel):
    repo_path: str


class GitDiffUnstaged(BaseModel):
    repo_path: str


class GitDiffStaged(BaseModel):
    repo_path: str


class GitDiff(BaseModel):
    repo_path: str
    target: str


class GitCommit(BaseModel):
    repo_path: str
    message: str


class GitAdd(BaseModel):
    repo_path: str
    files: list[str]


class GitReset(BaseModel):
    repo_path: str


class GitLog(BaseModel):
    repo_path: str
    max_count: int = 10


class GitCreateBranch(BaseModel):
    repo_path: str
    branch_name: str
    base_branch: str | None = None


class GitCheckout(BaseModel):
    repo_path: str
    branch_name: str


class GitShow(BaseModel):
    repo_path: str
    revision: str


class GitInit(BaseModel):
    repo_path: str


class GitTools(str, Enum):
    STATUS = "git_status"
    DIFF_UNSTAGED = "git_diff_unstaged"
    DIFF_STAGED = "git_diff_staged"
    DIFF = "git_diff"
    COMMIT = "git_commit"
    ADD = "git_add"
    RESET = "git_reset"
    LOG = "git_log"
    CREATE_BRANCH = "git_create_branch"
    CHECKOUT = "git_checkout"
    SHOW = "git_show"
    INIT = "git_init"


def git_status(repo: git.Repo) -> str:
    return repo.git.status()


def git_diff_unstaged(repo: git.Repo) -> str:
    return repo.git.diff()


def git_diff_staged(repo: git.Repo) -> str:
    return repo.git.diff("--cached")


def git_diff(repo: git.Repo, target: str) -> str:
    return repo.git.diff(target)


def git_commit(repo: git.Repo, message: str) -> str:
    commit = repo.index.commit(message)
    return f"Changes committed successfully with hash {commit.hexsha}"


def git_add(repo: git.Repo, files: list[str]) -> str:
    repo.index.add(files)
    return "Files staged successfully"


def git_reset(repo: git.Repo) -> str:
    repo.index.reset()
    return "All staged changes reset"


def git_log(repo: git.Repo, max_count: int = 10) -> list[str]:
    commits = list(repo.iter_commits(max_count=max_count))
    log = []
    for commit in commits:
        log.append(
            f"Commit: {commit.hexsha}\n"
            f"Author: {commit.author}\n"
            f"Date: {commit.authored_datetime}\n"
            f"Message: {commit.message}\n"
        )
    return log


def git_create_branch(repo: git.Repo, branch_name: str, base_branch: str | None = None) -> str:
    if base_branch:
        base = repo.refs[base_branch]
    else:
        base = repo.active_branch

    repo.create_head(branch_name, base)
    return f"Created branch '{branch_name}' from '{base.name}'"


def git_checkout(repo: git.Repo, branch_name: str) -> str:
    repo.git.checkout(branch_name)
    return f"Switched to branch '{branch_name}'"


def git_init(repo_path: str) -> str:
    try:
        repo = git.Repo.init(path=repo_path, mkdir=True)
        return f"Initialized empty Git repository in {repo.git_dir}"
    except Exception as e:
        return f"Error initializing repository: {str(e)}"


def git_show(repo: git.Repo, revision: str) -> str:
    commit = repo.commit(revision)
    output = [
        f"Commit: {commit.hexsha}\n"
        f"Author: {commit.author}\n"
        f"Date: {commit.authored_datetime}\n"
        f"Message: {commit.message}\n"
    ]
    if commit.parents:
        parent = commit.parents[0]
        diff = parent.diff(commit, create_patch=True)
    else:
        diff = commit.diff(git.NULL_TREE, create_patch=True)
    for d in diff:
        output.append(f"\n--- {d.a_path}\n+++ {d.b_path}\n")
        output.append(d.diff.decode('utf-8'))
    return "".join(output)


def list_tools() -> list[Tool]:
    return [
        Tool(
            name=GitTools.STATUS,
            description="Shows the working tree status",
            inputSchema=GitStatus.schema(),
        ),
        Tool(
            name=GitTools.DIFF_UNSTAGED,
            description="Shows changes in the working directory that are not yet staged",
            inputSchema=GitDiffUnstaged.schema(),
        ),
        Tool(
            name=GitTools.DIFF_STAGED,
            description="Shows changes that are staged for commit",
            inputSchema=GitDiffStaged.schema(),
        ),
        Tool(
            name=GitTools.DIFF,
            description="Shows differences between branches or commits",
            inputSchema=GitDiff.schema(),
        ),
        Tool(
            name=GitTools.COMMIT,
            description="Records changes to the repository",
            inputSchema=GitCommit.schema(),
        ),
        Tool(
            name=GitTools.ADD,
            description="Adds file contents to the staging area",
            inputSchema=GitAdd.schema(),
        ),
        Tool(
            name=GitTools.RESET,
            description="Unstages all staged changes",
            inputSchema=GitReset.schema(),
        ),
        Tool(
            name=GitTools.LOG,
            description="Shows the commit logs",
            inputSchema=GitLog.schema(),
        ),
        Tool(
            name=GitTools.CREATE_BRANCH,
            description="Creates a new branch from an optional base branch",
            inputSchema=GitCreateBranch.schema(),
        ),
        Tool(
            name=GitTools.CHECKOUT,
            description="Switches branches",
            inputSchema=GitCheckout.schema(),
        ),
        Tool(
            name=GitTools.SHOW,
            description="Shows the contents of a commit",
            inputSchema=GitShow.schema(),
        ),
        Tool(
            name=GitTools.INIT,
            description="Initialize a new Git repository",
            inputSchema=GitInit.schema(),
        )
    ]

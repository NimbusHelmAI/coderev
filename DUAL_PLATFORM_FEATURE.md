# Multi-Platform PR Reviewer (GitHub & GitLab)

This tool automates code reviews across GitHub Pull Requests and GitLab Merge Requests using local AI models via Ollama.

## Usage & CLI Flags

Run the reviewer interactively or pass flags to restrict target platforms:

```bash
# Review both GitHub and GitLab (Default)
./auto_pr_reviewer.py

# Review GitHub PRs only
./auto_pr_reviewer.py --github-only

# Review GitLab MRs only
./auto_pr_reviewer.py --gitlab-only

# Override model choice and timeout
./auto_pr_reviewer.py --model qwen2.5-coder:7b --timeout 300

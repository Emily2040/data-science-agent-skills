# Data Science Agent Skills Submission

This local repo stages the original submission as 25 independent branches, one skill per branch.

Each branch adds exactly one folder under `data-science-agent-skills/<skill-name>`.

To push later:

```powershell
git remote add origin https://github.com/OWNER/REPO.git
foreach ($branch in Get-Content .\BRANCHES.txt) { git push -u origin $branch }
```

Then open one PR per branch.

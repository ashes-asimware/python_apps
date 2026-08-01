# cleanup-branches.ps1
# Deletes all local branches that no longer exist on the remote (origin).
# Run this script from inside your Git repository folder.

# Get all local branches
$localBranches = git branch --format="%(refname:short)"

foreach ($branch in $localBranches) {
    # Skip the current branch to avoid deleting the one you're on
    $currentBranch = git rev-parse --abbrev-ref HEAD
    if ($branch -eq $currentBranch) {
        Write-Host "Skipping current branch: $branch"
        continue
    }

    # Check if branch exists on origin
    $existsOnOrigin = git ls-remote --heads origin $branch

    if (-not $existsOnOrigin) {
        Write-Host "Deleting local branch: $branch"
        git branch -D $branch
    } else {
        Write-Host "Keeping branch: $branch (exists on origin)"
    }
}

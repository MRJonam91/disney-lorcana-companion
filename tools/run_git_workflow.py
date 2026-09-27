import subprocess

def run(cmd):
    print("RUN:", cmd)
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=r'c:\Users\conta\OneDrive\Desktop\progetti\lorcana')
    print("STDOUT:", res.stdout.strip())
    if res.stderr:
        print("STDERR:", res.stderr.strip())
    return res.returncode

# Initialize git
run('git init -b master')
run('git config user.name "Illumineer Community"')
run('git config user.email "community@lorcana.local"')

# Stash all files first to work with clean commits
run('git add .gitignore LICENSE')
run('git commit -m "chore: initial repository setup with LICENSE and .gitignore"')

# We will commit on master the base, then for each language branch we commit the language files
langs = [
    ('it', 'Italian', 'guide/guida-lorcana-it.html', 'README.it.md'),
    ('en', 'English', 'guide/lorcana-guide-en.html', 'README.en.md'),
    ('fr', 'French', 'guide/lorcana-guide-fr.html', 'README.fr.md'),
    ('de', 'German', 'guide/lorcana-guide-de.html', 'README.de.md'),
    ('es', 'Spanish', 'guide/lorcana-guide-es.html', 'README.es.md'),
]

for code, name, guide_file, readme_file in langs:
    run(f'git checkout -b lang/{code} master')
    run(f'git add {guide_file} {readme_file} docs/*/*.{code}.md')
    run(f'git commit -m "feat({code}): add comprehensive {name} guide, rules, set history, strategy and deck"')

# Return to master and merge all branches
run('git checkout master')
for code, name, _, _ in langs:
    run(f'git merge lang/{code} --no-ff -m "merge: integrate {name} language branch (lang/{code})"')

# Add central hub and root README
run('git add index.html README.md')
run('git commit -m "feat: complete multilingual Disney Lorcana community hub with all merged language branches"')

print("\n--- GIT BRANCHES ---")
run('git branch -a')

print("\n--- GIT LOG SUMMARY ---")
run('git log --graph --oneline --decorate -n 20')

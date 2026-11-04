"""Read-only inspection of this checkout; never replays historical setup."""
from pathlib import Path
import subprocess


def main():
    root = Path(__file__).resolve().parents[1]
    for args in (
        ['git', 'status', '--short', '--branch'],
        ['git', 'branch', '-a'],
        ['git', 'log', '--graph', '--oneline', '--decorate', '-n', '12'],
    ):
        print('> ' + ' '.join(args), flush=True)
        result = subprocess.run(args, cwd=root, check=False)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

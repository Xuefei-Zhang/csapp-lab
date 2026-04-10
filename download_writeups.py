#!/usr/bin/env python3
"""
Download CSAPP lab writeups from the official website.

This script downloads the writeup PDF files for each CSAPP lab from
https://csapp.cs.cmu.edu/3e/labs.html and places them in the corresponding
lab directories.
"""

import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

# Base URL for CSAPP 3e labs
BASE_URL = "https://csapp.cs.cmu.edu/3e"

# Mapping of lab directories to their writeup URLs
# Based on the standard CSAPP lab structure from csapp.cs.cmu.edu/3e/labs.html
LAB_WRITEUPS = {
    "datalab-handout": f"{BASE_URL}/datalab.pdf",
    "bomb": f"{BASE_URL}/bomblab.pdf",
    "buflab32-handout": f"{BASE_URL}/buflab.pdf",
    "archlab-handout": f"{BASE_URL}/archlab.pdf",
    "archlab32-handout": f"{BASE_URL}/archlab32.pdf",
    "cachelab-handout": f"{BASE_URL}/cachelab.pdf",
    "perflab-handout": f"{BASE_URL}/perflab.pdf",
    "shlab-handout": f"{BASE_URL}/shlab.pdf",
    "malloclab-handout": f"{BASE_URL}/malloclab.pdf",
    "proxylab-handout": f"{BASE_URL}/proxylab.pdf",
}

def download_file(url, dest_path):
    """
    Download a file from URL to destination path.

    Args:
        url: Source URL
        dest_path: Destination file path

    Returns:
        True if successful, False otherwise
    """
    try:
        print(f"Downloading {url}...")
        with urllib.request.urlopen(url) as response:
            content = response.read()
            with open(dest_path, 'wb') as f:
                f.write(content)
        print(f"  ✓ Saved to {dest_path}")
        return True
    except urllib.error.HTTPError as e:
        print(f"  ✗ HTTP Error {e.code}: {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"  ✗ URL Error: {e.reason}")
        return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    """Main function to download all writeups."""
    script_dir = Path(__file__).parent
    success_count = 0
    fail_count = 0
    skip_count = 0

    print("CSAPP Lab Writeup Downloader")
    print("=" * 50)
    print()

    for lab_dir, writeup_url in LAB_WRITEUPS.items():
        lab_path = script_dir / lab_dir

        # Check if lab directory exists
        if not lab_path.exists():
            print(f"Skipping {lab_dir}: directory not found")
            skip_count += 1
            continue

        # Determine the output filename from the URL
        filename = os.path.basename(writeup_url)
        dest_path = lab_path / filename

        # Download the writeup
        if download_file(writeup_url, dest_path):
            success_count += 1
        else:
            fail_count += 1
        print()

    # Summary
    print("=" * 50)
    print("Summary:")
    print(f"  Successfully downloaded: {success_count}")
    print(f"  Failed: {fail_count}")
    print(f"  Skipped (directory not found): {skip_count}")
    print()

    if fail_count > 0:
        print("Some downloads failed. This may be due to:")
        print("  - Network connectivity issues")
        print("  - Changed URLs on the CSAPP website")
        print("  - Access restrictions")
        print()
        print("You may need to manually download the writeups from:")
        print("  https://csapp.cs.cmu.edu/3e/labs.html")
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()

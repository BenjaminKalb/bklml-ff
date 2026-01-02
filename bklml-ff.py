#!/usr/bin/env python3
"""
BenjaminKalb Localizations Markup Language File Finder
BKLML File Finder

Cross-platform script to scan folders for .bklml files.
Supports Linux, Windows, macOS.
"""

import os
import argparse
import sys
import re
from pathlib import Path

def extract_bklml_info(file_path):
    """
    Extract BKLML version and description from file.
    Version: @VERSION:{0.0.0}
    Description: @DESCRIPTION:{whoami example plugin integration fuck}
    """
    info = {"version": "Version not found", "description": "Description not found"}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract version
            version_match = re.search(r'@VERSION:\{([\d.]+)\}', content)
            if version_match:
                info["version"] = version_match.group(1)
            
            # Extract description
            desc_match = re.search(r'@DESCRIPTION:\{([^}]+)\}', content)
            if desc_match:
                info["description"] = desc_match.group(1).strip()
                
    except Exception as e:
        info["error"] = f"Error reading file: {str(e)}"
    
    return info

def find_bklml_files(directory, recursive=True):
    """
    Recursively scan directory for .bklml files.
    """
    directory = Path(directory)
    if not directory.exists():
        print(f"Error: Directory '{directory}' does not exist.", file=sys.stderr)
        return []
    
    if recursive:
        files = list(directory.rglob("*.bklml"))
    else:
        files = [f for f in directory.iterdir() if f.is_file() and f.suffix == ".bklml"]
    
    return files

def main():
    parser = argparse.ArgumentParser(
        description="BenjaminKalb Localizations Markup Language File Finder (BKLML File Finder)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  bklml_ff --help                        # Show full help
  bklml_ff /path/to/folder               # Scan recursively (file paths only)
  bklml_ff /path/to/folder --details     # Scan with version + description
  bklml_ff /path/to/folder --no-recursive -d  # Top level with details
  bklml_ff .                             # Current directory
        """
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to scan (default: current directory)"
    )
    parser.add_argument(
        "--details", "-d",
        action="store_true",
        help="Show detailed info: version and description for each file"
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="Do not scan subdirectories (default: recursive)"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.2"
    )
    
    args = parser.parse_args()
    
    files = find_bklml_files(args.directory, recursive=not args.no_recursive)
    
    if not files:
        print("Noo .bklml files found.")
        return
    
    print(f"Found {len(files)} .bklml file(s):")
    
    if args.details:
        print("\nFile path                           | Version  | Description")
        print("-" * 70)
        for file_path in sorted(files):
            info = extract_bklml_info(file_path)
            if "error" in info:
                print(f"{str(file_path):<35} | ERROR   | {info['error']}")
            else:
                print(f"{str(file_path):<35} | {info['version']:<7} | {info['description']}")
    else:
        print("\nFile paths:")
        for file_path in sorted(files):
            print(f"  {file_path}")

if __name__ == "__main__":
    main()

# File System Simulator

A simplified simulation of a hierarchical file system implemented using tree data structures in Python.

This project demonstrates how directory structures are represented internally using nodes and parent-child relationships.

---

## Project Overview

The file system is modeled as a tree:

- Each directory is represented as a `Node`
- Each node contains:
  - A name
  - A dictionary of child directories
- The root directory is `/`

The system supports:
- Directory creation (`mkdir`)
- Directory traversal and display (`ls`)

---

## Data Structure Used

Tree (N-ary Tree)

Each node contains:
- `name` → Directory name
- `children` → Dictionary of subdirectories

This mimics how real operating systems internally manage file hierarchies.

---

## File Structure

- file_system.py → Contains Node and FileSystem classes

---

## How It Works

### Creating Directories

The `mkdir(path)` function:

1. Splits the path into components
2. Traverses the tree
3. Creates missing directories dynamically

Example:

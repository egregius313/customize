# customize
A CLI utility to ease the editing of .rc files

```
customize - simple wrapper to aid in editing configuration and .rc files.

Usage:
    customize add <command> <rc_file>
    customize list
    customize set-editor <editor>
    customize which <command>...
    customize <command>
```

## Sample usage
```bash
$ customize set-editor emacs
$ customize add bash ~/.bashrc   # or ~/.bash_profile on Mac
$ customize bash                 # opens ~/.bashrc in Emacs
```

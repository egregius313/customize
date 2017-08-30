# customize
A CLI utility to ease the editing of .rc files

```
customize - simple wrapper to aid in editing configuration and .rc files.

Usage:
    customize add <command> <rc_file>
    customize list
    customize set-editor <editor>
    customize use-env-editor
    customize which <command>...
    customize <command>
```

## Sample usage
```bash
$ customize set-editor emacs
$ customize add bash ~/.bashrc   # or ~/.bash_profile on Mac
$ customize bash                 # opens ~/.bashrc in Emacs
```

## Commands
* `customize <command>` open the appropriate configuration file for `<command>`


| Command                   | Usage                                  |
|---------------------------|:--------------------------------------:|
| `add <command> <rc_file>` | associate `<rc_file>` with `<command>` |
| `list`                    | list (command, rc_file) pairs          |
| `set-editor <editor>`     | set the default editor to `<editor>` <br/>(__Note:__ if `use-env-editor` is set, the editor will default to `$EDITOR`) |
| `use-env-editor` | Set the default editor to `$EDITOR` |
| `which <command>...` | For each `<command>`, list the appropriate .rc file |

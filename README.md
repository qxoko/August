![](img/august.png)

August is _the_ Fountain package for Sublime Text.  It brings useful writing tools, offers a simple, customisable and distraction-free workflow, and leaves some of the more annoying "features" of other markup packages on the cutting room floor.

## Features at a Glance

August provides...

+ An easy to use multi-file screenplay workflow
+ PDF formatting and export via [Wrap](https://github.com/wraparound/wrap)
+ Bulk management for scene numbers

If you're a Fountainhead user, or have written themes for it, you'll be pleased to know August's syntax definition is fully compatible, with a [couple of additions](#syntax-reference).

#### ⚠️ WARNING

All features, including external ones such as Wrap support, are tested on macOS, Windows and Linux.

However, this package is considered **alpha** and does not yet have an official release.  There are bugs, there are issues and there are missing features.  Use at your own risk.

## Contents

+ [Command Reference](#command-reference)
+ [Split Merge](#splitmerge)
+ [Auto Formatting](#auto-formatting)
+ [Scope Reference](#scope-reference)
+ [Recommended Packages](#recommended-packages)
+ [Known Issues](#known-issues)

## Command Reference

##### `August: Merge Files`

Merges a list of files into a single master file.  (See [Split/Merge Workflow](#a-splitmerge-workflow)).

##### `August: Split Files`

Breaks a master file back down into its constituent files. (See [Split/Merge Workflow](#a-splitmerge-workflow)).

##### `August: Make PDF`

⚠️ Requires [Wrap](https://github.com/wraparound/wrap).  Saves a PDF from the focused file alongside it.  Can also be triggered with `ctrl+B` or `cmd+B` if the current build system is set to `August` (The build system should latch onto any open Fountain files by default).

The build system includes the `--production` flag by default to [avoid any confusion](https://github.com/Wraparound/wrap/wiki/FAQ#when-i-use-wrap-there-are-no-scene-numbers).

##### `August: Add Scene Numbers`

Adds `#1#` formatted scene numbers to every scene heading, *replacing any existing ones*.  This only provides integer numbering.

##### `August: Remove Scene Numbers`

Strips out any `#1#` scene numbers from the current file.  The removal command (and syntax highlighting) will catch all [valid scene numbers](https://fountain.io/syntax), such as `#1#`, `#1-A#`, `#1.A-A#`.

##### `August: List Scenes`

Creates a list of scene headings from the current file in a scratch buffer.  Useful for getting a topdown view of a long file.

##### `August: Show/Hide Boneyard`

Hides or reveals (by folding) all  `/* boneyard */` regions in the current file.

## Split/Merge

Based on [Mountain](https://github.com/mjrusso/mountain), Split/Merge brings multi-file screenplays to Sublime.  It provides a convenient method of writing Fountain screenplays in multiple files and directories, then merging them into a single file only when absolutely necessary.  It was designed to avoid some of the key pitfalls that most text editors, even Fountain-focused ones, fall into by expecting everyone to write their entire screenplay in a single, thousands-of-lines-long file.  Combined with source control, screenplay revisions, scene-locking and big-picture editing all become a piece of cake.

The workflow is controlled entirely with the use of two keywords, `include` and `reference`.  These are referred to as _directives_ by Mountain, and are explained in context in the next section.

#### A Split/Merge Workflow

Create a manifest file at the top level of your screenplay's directory.  You'll need to use a `.fountain` or `.ftn` file extension.  The following example references two scene files stored in folders `act1` and `act3` alongside the manifest.

```
title: Big Fish
author: John August

# ACT I

[[include: act1/introduction.fountain]]

# ACT II

# ACT III

[[include: act3/post_credits.fountain]]
```

With the manifest focused, open the command palette and use:

+ `August: Merge File`

You will be prompted for a filename.  This can be a full `~/path/to/file.fountain`, or just `file.fountain`.  The latter will be saved in the same directory as the manifest.  This will create one huge file with all the referenced scenes compiled into it.

That file will then be opened in Sublime as the active buffer.  You will see scene delimiters included, in the format:

```
[[reference: act1/introduction.fountain]]

/* scene content */

[[/reference]]
```

This allows the file to be split back into its original constituent parts using the command:

+ `August: Split File`

You will again be prompted for a name.  This will set the manifest filename.  Its scene files and folders, if any, will be created according to the structure laid out by the `reference` directives, meaning `[[reference: act1/introduction.fountain]]` will generate a folder `act1` containing a file `introduction.fountain`, as expected.

You can use this to update the original scene files with edits made in the master file, rebuild your project's writing workspace on another computer, or even convert an existing single-file project into more manageable chunks.

## Auto Formatting

Some syntax will be automatically capitalised and appropriate newlines inserted when pressing `return`.  These include:

+ Scene headings
+ Character names
+ Transitions

You can enable or disable them individually in your `User/August.sublime-settings` file.  All are enabled by default upon installation.

```json
"auto_cap_scenes": false,
"auto_cap_characters": false,
"auto_cap_transitions": false,
```

FYI: Some false positives may occur, where certain words will be undesirably capitalised.  These are always caused by the `auto_cap_characters` setting, and disabling it will fix the issue.  Chances are, you will never see one, as they are incredibly rare, but nearly impossible to completely eradicate due to restrictions in Sublime Text's macro engine.

## Scope Reference

August mirrors the scope conventions of Fountainhead, with a few additions.  Below is a comprehensive list of all scopes used, for reference when creating highlighting support.

##### Original Fountainhead

```
fountain:       text.fountain
action:         foreground
boneyard:       comment
dialogue:       dialogue
lyrics:         lyrics
character:      string
parenthetical:  entity.other.inherited-class
note:           variable.parameter
scene:          entity.name.function
section:        entity.name.filename
synopses:       meta.diff
pagebreak:      support.function
title_page:     constant.numeric
transition:     entity.name.tag
```
##### Added by August
```
scene_numbers:  entity.name.constant
center:         centered (foreground in FH)
note_keywords:  support.constant
emphasis_chars: markup.other
```

## Recommended Packages

##### Wrap

[GitHub](https://github.com/wraparound)

A command line tool for exporting screenplays to PDF and HTML.  August aims to support Wrap entirely.  See status here:

+ multi-language support
+ ~~build system~~
+ ~~scene. syntax~~
+ ~~additional title page tags~~

##### Mountain

[GitHub](https://github.com/mjrusso/mountain)

The original Mountain was designed as a command-line tool.  If you like the Mountain workflow and want it outside of Sublime, this is the place to get it.

##### Typewriter

[Package Control](https://packagecontrol.io/packages/Typewriter) | [GitHub](https://github.com/alehandrof/Typewriter)

Brings typewriter-style scrolling to your long writing sessions.  Use `"typewriter_mode_scrolling": true` in your `August.sublime-settings` file to enable it just for Fountain files, or toggle it from the command palette.

## Known Issues

+ markup syntax does not nest
+ markup will act on text even if there is no closing element [violating line-jumping rules](https://fountain.io/syntax#section-emphasis)
+ [character extensions](https://fountain.io/syntax#section-character) are not currently able to be lowercase and still highlight correctly.  Can still be used with the `@` force syntax
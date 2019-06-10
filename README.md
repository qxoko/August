![](img/august.png)

August is _the_ Fountain package for Sublime Text.  It brings useful writing tools, offers a simple, customisable and distraction-free workflow, and leaves some of the more annoying "features" of other markup packages on the cutting room floor.

If you're a Fountainhead user, or have written themes for it, you'll be pleased to know August's syntax definition is fully compatible, with a [couple of additions](#syntax-reference).

August's installation, syntax names and settings files all use the namespace `August`, to (mostly) prevent conflicts with other or older packages you might want to keep using.

#### ⚠️ WARNING

This package is considered **alpha** and does not yet have an official release.  There are bugs, there are issues and there are missing features.  Use at your own risk.

## Command Shortlist

+ `August: Merge Files`

  Merges a list of files into a single master file.  (See [Split/Merge Workflow](#a-splitmerge-workflow)).

+ `August: Split Files`

  Breaks a master file back down into its constituent files. (See [Split/Merge Workflow](#a-splitmerge-workflow)).

+ `August: Add Scene Numbers`

  Adds `#1#` formatted scene numbers to every scene heading, *replacing any existing ones*.  This only provides integer numbering.

+ `August: Remove Scene Numbers`

  Strips out any `#1#` scene numbers from the current file.  The removal command (and syntax highlighting) will catch all [valid scene numbers](https://fountain.io/syntax), such as `#1#`, `#1-A#`, `#1.A-A#`.

+ `August: List Scenes`

  Creates a list of scene headings from the current file in a scratch buffer.  Useful for getting a topdown view of a long file.

+ `August: Show/Hide Boneyard`

  Hides or reveals (by folding) all  `/* boneyard */` regions in the current file.

## Tools

#### Split/Merge

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

## Syntax Reference

August mirrors the scope conventions of Fountainhead, with a few additions.  Below is a comprehensive list of all scopes used, for reference when creating highlighting support.

##### Fountainhead

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
center:         foreground
transition:     entity.name.tag
```
##### Added by August
```
scene_numbers:  entity.name.constant
```
## Recommended Packages

##### Mountain

[GitHub](https://github.com/mjrusso/mountain)

The original Mountain was designed as a command-line tool.  If you like the Mountain workflow and want it outside of Sublime, this is the place to get it.

##### Typewriter

[Package Control](https://packagecontrol.io/packages/Typewriter) | [GitHub](https://github.com/alehandrof/Typewriter)

Brings typewriter-style scrolling to your long writing sessions.  Use `"typewriter_mode_scrolling": true` in your `August.sublime-settings` file to enable it just for Fountain files, or toggle it from the command palette.


## Todo

+ macros for auto-capitalisation

## Known Issues

+ ~~scene number highlighting~~
+ ~~parenthetical/dialogue scopes currently ommitted from syntax file~~
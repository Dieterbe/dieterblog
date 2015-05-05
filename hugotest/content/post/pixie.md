+++
title = "Pixie: simple photo management using directory layouts and tags."
date = "2013-12-30T14:46:32-04:00"
tags = ["arch", "golang", "photos"]
+++
that keeps a simple and elegant, yet flexible file/directory layout for portability and simplicity?

<!--more-->

<br/>

<br/>I couldn't find a tool that I liked, so I rolled my own: <a href="https://github.com/Dieterbe/pixie">Pixie</a>.

<br/>

It gives you vim-like keybindings to navigate pictures, create edits (stored in a "mirror directory") and add/remove tags to pictures.  (Because n:m tag relationships are basically a must for organizing things and don't work on any common filesystem)

To generate "album" directories, just define which tags they should(n't) match and run the script that synchronizes an export directory by symlinking (or resizing) the correct files into them.

Note the source directory stays unaltered so you can easily keep syncing with devices and/or people.

<br/>What used to be a pain in the butt for me is now a pretty pleasant experience.

<br/>Does this workflow make sense to you? Is this useful to you? Why (not) ?

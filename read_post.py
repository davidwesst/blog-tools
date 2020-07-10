#!/usr/bin/env python
"""Script to convert a blog post written for davidwesst.com to westerndevs.com"""

import frontmatter

# load the post
POST = frontmatter.load("test/sample-post.md")

# add frontmatter fields for westerndevs.com
POST["authorId"] = "'david_wesst'"
POST["layout"] = "post"

# output the file
WD_POST = open("test/sample-wd.md", "w")
WD_POST.write(frontmatter.dumps(POST))
WD_POST.write("\n")
WD_POST.close()

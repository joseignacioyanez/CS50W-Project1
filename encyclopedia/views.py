from django.shortcuts import render

from markdown2 import Markdown

from . import util


def index(request):
    

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryShow(request, entryName):
    # Check if Entry exists
    entrySearched = util.get_entry(entryName)
    if not entrySearched:
        return render(request, "encyclopedia/error.html")

    else:

        markdowner = Markdown()
        entryHTML = markdowner.convert(entrySearched)

        return render(request, "encyclopedia/entry.html", {
            # Render Markdown entry
            "entryName":entryName,
            "entryHTML":entryHTML
        })
# KGR-Resources

The KGR-Resources repository houses resources for the [Gotong Royong Chapel](https://kapelrsgotongroyong.com/).

The resources in here is in a mix of Bahasa Indonesia and English.
Copyright of the song lyrics and texts are held by the original authors.

**Currently, the repository contains:**

-   Song lyrics used for events in the chapel in the [OpenLyrics](https://docs.openlyrics.org/en/latest/) format.
-   Texts used for events in the chapel in the MDX format.

**The repository is structured as follows:**

-   `songs-data`: contains the song lyrics in OpenLyrics XML format.
-   `teks-misa`: contains the texts used for events in the chapel in MDX format.
-   `indexes`: contains the indexes for the song lyrics and texts. This is automatically generated by CI/CD using `generated-indexes.py`.
-   `teks-snippets`: contains snippets of text used for events in the chapel in MDX format.
-   `requirements.txt`: contains the Python dependencies for the script.

**Custom Syntax for MDX files:**
- `::song[song-file-name.xml]`: include a song lyric file. This is relative to the `songs-data` directory.
- `::snippet[snippet-file-name.mdx]`: include a snippet of text file. This is relative to the `teks-snippets` directory.
- `::hint[hint-text]`: include a hint for the text. Hints are displayed on the right side of the text.

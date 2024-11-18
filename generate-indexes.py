from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET
import frontmatter
import re
import json
import datetime
from zoneinfo import ZoneInfo


# Whitelisted characters: a-z, 0-9, -
# Replace all other characters with a dash
# Replace multiple dashes with a single dash
def sanitize(string: str) -> str:
    stripped = "".join(c.lower() if c.isalnum() or c in "-" else "-" for c in string)
    stripped = re.sub(r"[-]+", "-", stripped)
    return stripped


def generate_songs_index(directory: str):
    index_map = {}
    files = [f for f in listdir(directory) if isfile(join(directory, f))]

    for file in files:
        if file.endswith(".xml"):
            # print(f"Processing {file}")
            tree = ET.parse(join(directory, file))
            root = tree.getroot()

            properties = root.find(
                "{http://openlyrics.info/namespace/2009/song}properties"
            )
            titles = properties.find(
                "{http://openlyrics.info/namespace/2009/song}titles"
            )
            authors = properties.find(
                "{http://openlyrics.info/namespace/2009/song}authors"
            )
            first_title = titles.find(
                "{http://openlyrics.info/namespace/2009/song}title"
            ).text
            first_author = authors.find(
                "{http://openlyrics.info/namespace/2009/song}author"
            ).text

            merged_title = f"{first_title} - {first_author}"
            sanitized_title = sanitize(merged_title)

            # Test if the title is already in the index
            if sanitized_title in index_map:
                print(f"Skipping {sanitized_title} because it already exists")
                continue

            index_map[sanitized_title] = {
                "title": f"{first_title} ({first_author})",
                "originalFilename": file,
            }

    return index_map


songs_index = generate_songs_index("songs-data")
# Save index_map as JSON
with open("indexes/songs.json", "w") as f:
    json.dump(songs_index, f)

print(f"Processed {len(songs_index)} songs")


def generate_teks_misa_index(directory: str):
    index_map = {}
    files = [f for f in listdir(directory) if isfile(join(directory, f))]

    for file in files:
        if file.endswith(".mdx"):
            # Extract frontmatter data
            file_data = frontmatter.load(join(directory, file))

            # Extract title and date
            title = file_data["title"]
            date = file_data["date"]

            # Extract the filename without the extension
            filename = file.replace(".mdx", "")

            index_map[filename] = {
                "title": title,
                "date": date,
                "originalFilename": file,
            }
            
    return index_map

teks_misa_index = generate_teks_misa_index("teks-misa")
# Save index_map as JSON
with open("indexes/teks-misa.json", "w") as f:
    json.dump(teks_misa_index, f)

print(f"Processed {len(teks_misa_index)} teks misa")

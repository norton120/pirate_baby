import json
from pathlib import Path


class MakeBoat:


    def getdata(self, key, default=None):
        # stupid pandas indexes and I don't feel like re-converting again
        top = self.data.get(key, default)
        if top == default:
            return top
        return top.get("7", top.get("15"))

    def __init__(self, boatpath:Path):
        self.boatpath = boatpath
        self.body = ""
        self.data = json.loads((boatpath / "data.json").read_text())
        images, header_img = self._make_image_section()
        self.body += self.make_head(header_img)
        self.body += self.make_price()
        self.body += images
        self.body += self.make_description()
        self.body += self.base_specs()
        self.body += self.engine()
        self.body += self.writeups()
        self.body += self.visit_notes()
        index = self.boatpath / "index.md"
        index.write_text(self.body)

    def make_head(self, header_img:str):
        name = self.boatpath.name.split("-")[:2]
        name = " ".join(name).title()
        head = "---\n"
        head += f"title: {name}\n"
        head += "date: 2024-05-04\n"
        head += "tags: ['boats']\n"
        head += "draft: false\n"
        head += "showReadingTime: false\n"
        head += f"cover:\n  image: {header_img}\n  hidden: false\n  hiddenInList: false\n  hiddenInSingle: false\n"
        head += "---\n\n"
        return head

    def make_description(self):
        description = "## Description (from YachtWorld)\n\n"
        description += self.getdata("description").replace("\n", "\n\n").strip("Show More")
        description += "\n\n"
        return description

    def _make_image_section(self) -> tuple[str, str]:
        localbody = "<details>\n<summary style='color:yellow;font-weight:bold;'>📷 More Pictures!:</summary>\n"
        header_img = None
        for image in Path(f"/app/static/images/{self.boatpath.name}").iterdir():
            if image.suffix in [".jpg", ".png"]:
                src = f"/images/{self.boatpath.name}/{image.name}"
                if not header_img:
                    header_img = src
                localbody += f'<img src="{src}" alt="{image.stem}">\n'

        localbody += "</details>\n\n"
        return localbody, header_img

    def make_price(self):
        price = "### :money_mouth_face: Asking Price: "
        price += f'${round(self.getdata("price")):,}'
        return price + "\n"

    def base_specs(self):
        specs = "## Basic Specifications\n\n"
        for k,v in self.getdata("boat_specs").items():
            if not v:
                v = "Unknown"
            specs += f"- **{k}**: {v}\n"
        return specs

    def engine(self):
        engine = "## Engine Details\n\n"
        for k,v in self.getdata("propulsion").items():
            if not v:
                v = "Unknown"
            engine += f"- **{k}**: {v}\n"
        for key in ('engine',"engine_hours", "total_power",):
            value = self.getdata(key) or "Unknown"
            engine += f"- **{key.replace('_',' ')}**: {value}\n"
        return engine

    def writeups(self):
        name_kebab = "-".join(self.boatpath.name.split("-")[1:3])
        writeups = "## Writeups\n\n<ul>\n\n"
        for url, title in (
            (self.getdata('url'), "YachtWorld Listing"),
            (f"https://sailboatdata.com/sailboat/{name_kebab}/?units=imperial", "SailboatData"),
            (f"https://www.practical-sailor.com/sailboat-reviews/{name_kebab}", "Practical Sailor"),
        ):
            writeups += f"<li><a href='{url}' target='_BLANK'>{title}</a></li>\n"
        writeups += "</ul>\n\n"
        return writeups

    def visit_notes(self):
        if not (note_dates := self.getdata("visit_notes", [])):
            return ""
        notes = "## Visit Notes\n\n"
        for date in note_dates:
            notes += f"\n\n**{date['date']}:**\n\n"
            for note in date['notes']:
                notes += f"- {note}\n"
        return notes


if __name__ == "__main__":
    paths = Path("/app/content/boats").iterdir()
    for path in paths:
        if path.is_dir() and not path.name.startswith("_"):
            print("making boat: ", path)
            MakeBoat(path)
            print("done")
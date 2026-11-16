"""Build deck.apkg from cards.tsv (front<TAB>back<TAB>tags)."""
import csv, genanki, pathlib
here = pathlib.Path(__file__).parent
css = ".card{font-family:system-ui,sans-serif;font-size:19px;line-height:1.45;text-align:left;max-width:640px;margin:auto;padding:12px}code{font-size:.9em;background:rgba(127,127,127,.15);padding:1px 4px;border-radius:4px}i{opacity:.8}"
model = genanki.Model(1607392319, "CCA-F Basic", fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card 1", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}], css=css)
deck = genanki.Deck(2059400110, "Claude Architect – Foundations (high yield)")
for front, back, tags in csv.reader(open(here / "cards.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
    deck.add_note(genanki.Note(model=model, fields=[front, back], tags=tags.split()))
genanki.Package(deck).write_to_file(here / "deck.apkg")
print(len(deck.notes), "cards")

# Plain-text version for "paste text" import: front<TAB>back, one card per line, no HTML, no tags.
import html, re
def plain(s):
    s = re.sub(r"<br\s*/?>", " | ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).replace("\t", " ").strip()
with open(here / "paste.txt", "w") as f:
    for front, back, _ in csv.reader(open(here / "cards.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
        f.write(f"{plain(front)}\t{plain(back)}\n")
print("paste.txt written")

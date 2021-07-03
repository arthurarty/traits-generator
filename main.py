from traits import SKINS, EYES, MOUTH, ACCESSORIES, FOOTWARE, CROWNS
import random
from dataclasses import dataclass, asdict
from typing import Optional
import csv


@dataclass
class Toon():
    skin: str
    eyes: str
    mouth: str
    crown: str
    footware: Optional[str] = None
    accessories: Optional[str] = None


def _create_single_toon():
    """
    Create a toon by randomly selecting each one of the traits required.
    :return: Toon
    """
    return Toon(
        skin=SKINS[random.randint(0, len(SKINS) - 1)],
        eyes=EYES[random.randint(0, len(EYES) - 1)],
        mouth=MOUTH[random.randint(0, len(MOUTH) - 1)],
        crown=CROWNS[random.randint(0, len(CROWNS) - 1)],
        footware=FOOTWARE[random.randint(0, len(FOOTWARE) - 1)],
        accessories=ACCESSORIES[random.randint(0, len(ACCESSORIES) - 1)]
    )


def _create_toons():
    toons_created = []
    for ii in range(5010):
        new_toon = _create_single_toon()
        if new_toon in toons_created:
            print('skipping already existing toon')
            continue
        else:
            toons_created.append(new_toon)
        if len(toons_created) == 5000:
            break
    return toons_created


def run():
    with open('random_generated_traits.csv', mode='w') as csv_file:
        fieldnames = ['skin', 'eyes', 'mouth', 'crown', 'footware', 'accessories']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        print('Creating csv')
        for toon in _create_toons():
            writer.writerow(asdict(toon))


if __name__ == "__main__":
    run()

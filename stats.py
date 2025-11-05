def get_num_words(text: str) -> None:
    num_words = len(text.split())
    print(f"Found {num_words} total words")


def get_num_characters(text: str) -> dict[str, int]:
    results: dict[str, int] = {}
    for character in text:
        if not character.isalpha():
            continue
        character_lowercase = character.lower()
        if character_lowercase in results.keys():
            results[character.lower()] += 1
        else:
            results[character_lowercase] = 1

    return results


def sort_on(items: dict[str, int]) -> int:
    return items["num"]


def sort_num_characters(num_characters: dict[str, int]) -> list[dict[str, str | int]]:
    result = [{"char": k, "num": v} for k, v in num_characters.items()]
    result.sort(reverse=True, key=sort_on)
    return result

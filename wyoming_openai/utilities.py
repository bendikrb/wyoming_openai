from io import BytesIO


class NamedBytesIO(BytesIO):
    """
    A subclass of BytesIO that adds a 'name' attribute to the file-like object.
    """

    def __init__(self, *args, name="audio.wav", **kwargs):
        """
        Initialize a new NamedBytesIO instance.

        Args:
            *args: Variable length argument list passed to BytesIO constructor.
            name (str): The name or filename associated with this byte stream.
                        Default is 'audio.wav'.
            **kwargs: Arbitrary keyword arguments passed to BytesIO constructor.

        """
        super().__init__(*args, **kwargs)
        self._name = name

    @property
    def name(self):
        """
        Returns the name of the byte stream.

        Returns:
            str: The name or filename associated with this byte stream.
        """
        return self._name


def extract_instructions(text: str) -> tuple[str | None, str]:
    """
    Extracts instructions enclosed in square brackets from the beginning of text.
    """
    text = text.strip()

    if text.startswith("["):
        closing_bracket_index = text.find("]")
        if closing_bracket_index != -1:
            instructions = text[1:closing_bracket_index]
            remaining_text = text[closing_bracket_index + 1 :].lstrip()

            return instructions, remaining_text
    return None, text

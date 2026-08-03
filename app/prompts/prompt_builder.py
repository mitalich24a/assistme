class PromptBuilder:

    @staticmethod
    def build(
        system_prompt: str,
        user_prompt: str,
    ) -> tuple[str, str]:

        return (
            system_prompt.strip(),
            user_prompt.strip(),
        )
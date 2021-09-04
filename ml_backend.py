import openai

class ml_backend:
        
    openai.api_key = "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"

    def generate_explanation(self, userPrompt ="def remove_common_prefix(x, prefix, ws_prefix): \n    x[\"completion\"] = x[\"completion\"].str[len(prefix) :] \n    if ws_prefix: \n        # keep the single whitespace as prefix \n        x[\"completion\"] = \" \" + x[\"completion\"] \nreturn"):
        response = openai.Completion.create(
        engine="davinci-codex",
        prompt= "# Python 3 \n" + userPrompt + " \n\n# Explanation of what the code does\n\n#",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#"]
        )
        return response.get("choices")[0]['text']
        

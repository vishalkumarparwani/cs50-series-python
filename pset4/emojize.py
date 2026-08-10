import emoji

user_input = input("Input: ")

converted_emoji = emoji.emojize(user_input, language="alias")

print(f"Output: {converted_emoji}")

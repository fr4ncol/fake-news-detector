from mistralai import Mistral

model = "mistral-large-latest"

client = Mistral(api_key='LLyqibiPrFeMPvNQvdvlwr6lLGgzCrS2')

statement = """WASHINGTON (Reuters) - Democratic U.S. presidential hopeful Bernie Sanders brought his firebrand rhetoric back to the floor of the Senate on Tuesday to condemn a White House-backed bill on Puerto Rico’s financial crisis as “colonialism at its worst.” Sanders, a self-described democratic socialist who turned an unlikely presidential bid into a political movement to combat inequality, warned that legislation due for a crucial Senate vote on Wednesday would subject Puerto Rico to Republican trickle-down economics and favor “vulture capitalists” at the expense of the island’s increasingly impoverished population. An aide said it was the first time Sanders has spoken in the Senate since December. “Does that sound like the kind of morality that should be passed here in the United States Senate?” Sanders fumed during an eight-minute appearance to support an hours-long speech by Democratic Senator Robert Menendez of New Jersey, who opposes the bill. The Vermont senator used his appearance to rail against details of the legislation, which would put much of Puerto Rico’s management in the hands of a seven-member oversight board and require the island to pay $370 million over five years for the board’s administration costs even as it cuts funding for education, healthcare and pensions. In an exchange with Menendez, Sanders said, “How in God’s name do you run up an administrative cost of $370 million,” adding, “I know this sounds so absurd that people may think I’m misleading them.” “Would my friend from New Jersey agree that this is colonialism at its worst?” asked Sanders, who announced last week that he would vote for presumptive Democratic presidential nominee Hillary Clinton in her November election contest against Republican Donald Trump. “Oh absolutely,” replied Menendez. The Puerto Rico bill, which has already been passed by the Republican-controlled House of Representatives, faces opposition from both sides of the aisle in the Senate. Nevertheless, the Obama administration and Republican leaders are trying to get the bill passed before a July 1 deadline, when the island is scheduled to make a $1.9 billion payment on its $70 billion debt."""

zero_shot = """
Determine whether the following statement is "True" or "False":

Statement: {statement}
Label:
"""

zero_shot_cot = """
Determine whether the following statement is "True" or "False". 
Explain your reasoning step by step before giving the final answer.

Statement: {statement}
Reasoning:
Label:
"""

one_shot = """
Statement: "Reuters: The Pfizer vaccine was banned in Europe due to severe side effects in 2021."
Label: False

Now determine whether the following statement is "True" or "False":
Statement: {statement}
Label:
"""

one_shot_cot = """
Statement: "Reuters: The Pfizer vaccine was banned in Europe due to severe side effects in 2021."
Reasoning: The Pfizer vaccine was approved and widely used in Europe, with no ban reported.
Label: False

Now determine whether the following statement is "True" or "False":
Statement: {statement}
Reasoning:
Label:
"""

few_shot = """
Statement: In 2021, the United States officially recognized Taiwan as an independent country.
Label: False

Statement: "Fox News: The Paris Agreement requires all countries to reduce their carbon emissions by 50 percent by 2030."
Label: False

Statement: In 2021, Australia signed the AUKUS pact with the United States and the United Kingdom to enhance defense cooperation.
Label: True

Now determine whether the following statement is "True" or "False":
Statement: {statement}
Label:
"""

few_shot_cot = """
Statement: In 2021, the United States officially recognized Taiwan as an independent country.
Reasoning: While the U.S. supports Taiwan's self-defense, it has not officially recognized Taiwan as an independent country
Label: False

Statement: "Fox News: The Paris Agreement requires all countries to reduce their carbon emissions by 50 percent by 2030."
Reasoning: The Paris Agreement allows countries to set their own emission reduction targets, and there is no universal requirement for a 50 percent reduction by 2030
Label: False

Statement: In 2021, Australia signed the AUKUS pact with the United States and the United Kingdom to enhance defense cooperation.
Reasoning: Australia signed the AUKUS agreement in 2021 to strengthen its defense capabilities, particularly in the Indo-Pacific region, making this statement true 
Label: True

Now determine whether the following statement is "True" or "False":
Statement: {statement}
Reasoning: 
Label:
"""



zero_shot = zero_shot.format(statement=statement)
zero_shot_cot = zero_shot_cot.format(statement=statement)
few_shot = few_shot.format(statement=statement)
few_shot_cot = few_shot_cot.format(statement=statement)
one_shot = one_shot.format(statement=statement)
one_shot_cot = one_shot_cot.format(statement=statement)

# print(chat_response.choices[0].message)

zero_shot_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": zero_shot,
        },
    ]
)

zero_shot_cot_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": zero_shot_cot,
        },
    ]
)

few_shot_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": few_shot,
        },
    ]
)

few_shot_cot_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": few_shot_cot,
        },
    ]
)

one_shot_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": one_shot,
        },
    ]
)

one_shot_cot_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": one_shot_cot,
        },
    ]
)

print("===========================ZERO SHOT=============================")
print(zero_shot_response.choices[0].message.content)
print("=========================ZERO SHOT COT===========================")
print(zero_shot_cot_response.choices[0].message.content)
print("============================FEW SHOT=============================")
print(few_shot_response.choices[0].message.content)
print("===========================FEW SHOT COT==========================")
print(few_shot_cot_response.choices[0].message.content)
print("===========================ONE SHOT=============================")
print(one_shot_response.choices[0].message.content)
print("=========================ONE SHOT COT===========================")
print(one_shot_cot_response.choices[0].message.content)
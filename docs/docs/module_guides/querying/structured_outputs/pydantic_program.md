# Pydantic Program

A pydantic program is a generic abstraction that takes in an input string and converts it to a structured Pydantic object type.

Because this abstraction is so generic, it encompasses a broad range of LLM workflows. The programs are composable and be for more generic or specific use cases.

There's a few general types of Pydantic Programs:

- **LLM Text Completion Pydantic Programs**: These convert input text into a user-specified structured object through a text completion API + output parsing.
- **LLM Function Calling Pydantic Program**: These convert input text into a user-specified structured object through an LLM function calling API.
- **Prepackaged Pydantic Programs**: These convert input text into prespecified structured objects.

## LLM Text Completion Pydantic Programs

See the example notebook on [LLM Text Completion programs](../../../examples/output_parsing/llm_program.ipynb)

## LLM Function Calling Pydantic Programs

- [OpenAI Pydantic Program](../../../examples/output_parsing/openai_pydantic_program.ipynb)
- [Guidance Pydantic Program](../../../examples/output_parsing/guidance_pydantic_program.ipynb)
- [Guidance Sub-Question Generator](../../../examples/output_parsing/guidance_sub_question.ipynb)

## Prepackaged Pydantic Programs

- [DF Program](../../../examples/output_parsing/df_program.ipynb)
- [Evaporate Program](../../../examples/output_parsing/evaporate_program.ipynb)

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from models import InvoiceDetails


def process_invoice_text(text: str) -> InvoiceDetails:

    system_prompt = "Convert all numbers in the provided text that contain commas into a format without commas. For example, convert 6,790 to 6790. Ensure that all numbers with commas are correctly converted to their non-comma equivalents."

    parser = PydanticOutputParser(pydantic_object=InvoiceDetails)

    prompt = PromptTemplate(
        template="Answer the user query.\n{system_prompt}\n{query}\n{format_instructions}",
        input_variables=["query"],
        partial_variables={
            "system_prompt": system_prompt,
            "format_instructions": parser.get_format_instructions(),
        },
    )

    model = ChatGoogleGenerativeAI(
        model="gemini-pro", api_key="AIzaSyAMwe7WMzayXaZItIUf7FcasN1_ls8CGZU"
    )

    chain = prompt | model | parser

    prompt = f"Extract the customer details, items, and total amount from the following invoice text:\n\n{text}\n\n.Detect if the HSN code exceeds 8 digits and separate any merged values. The HSN code should be an 8-digit integer, and other values like rate, quantity, amount, etc., should be extracted accordingly. If it exceeds 8 digit the number after that belongs to rate. For example 7204219095.00, so here the number exceeds 8 digit so till 8 chars it belongs to HSN and after 8 chars it belongs to rate"

    result = chain.invoke({"query": prompt})

    return result

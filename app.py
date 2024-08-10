import click
from extract_text import extract_text_from_pdf
from llm import process_invoice_text
from utils import format_to_json

@click.command()
@click.option(
    "--file_path", type=click.Path(exists=True, dir_okay=False, readable=True)
)
def process_invoice(file_path: str):
    text = extract_text_from_pdf(file_path)

    try:
        invoice_details = process_invoice_text(text)
        json_format = format_to_json(invoice_details)
                
        click.echo(json_format)

    except Exception as e:
        click.echo(f"Error: {e}")


if __name__ == "__main__":
    process_invoice()

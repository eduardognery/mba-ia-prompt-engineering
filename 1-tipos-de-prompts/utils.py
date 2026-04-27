from rich.console import Console
from rich.text import Text

def print_llm_result(prompt, response):
    """
    Print LLM prompt, response and token usage with colored formatting
"""
    console = Console()
    
    # Print prompt
    console.print(Text("USER PROMPT:", style="bold green"))
    console.print(Text(prompt, style="bold blue"), end="\n\n")
    
    # Print response
    console.print(Text("LLM RESPONSE:", style="bold green"))
    console.print(Text(response.content, style="bold blue"), end="\n\n")
    
    # Print token usage (if available)
    # OpenAI format: response_metadata['token_usage']
    if hasattr(response, 'response_metadata') and response.response_metadata:
        usage = response.response_metadata['token_usage']
        console.print(f"[bold white]Input tokens:[/bold white] [bright_black]{usage.get('prompt_tokens', 'N/A')}[/bright_black]")
        console.print(f"[bold white]Output tokens:[/bold white] [bright_black]{usage.get('completion_tokens', 'N/A')}[/bright_black]")
        console.print(f"[bold white]Total tokens:[/bold white] [bright_black]{usage.get('total_tokens', 'N/A')}[/bright_black]")
    
    # Google Generative AI format: usage_metadata
    if hasattr(response, 'usage_metadata') and response.usage_metadata:
        usage = response.usage_metadata
        prompt_tokens = usage.get('prompt_tokens', usage.get('input_tokens', 'N/A'))
        output_tokens = usage.get('output_tokens', usage.get('completion_tokens', 'N/A'))
        console.print(f"[bold white]Input tokens:[/bold white] [bright_black]{prompt_tokens}[/bright_black]")
        console.print(f"[bold white]Output tokens:[/bold white] [bright_black]{output_tokens}[/bright_black]")
        console.print(f"[bold white]Total tokens:[/bold white] [bright_black]{prompt_tokens + output_tokens}[/bright_black]")

    console.print(f"[yellow]{'-'*50} [/yellow]")
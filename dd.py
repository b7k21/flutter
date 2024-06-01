import subprocess

def latex_to_word(latex_file, word_file):
    """
    Converts a LaTeX document to a Word file using Pandoc.

    :param latex_file: Path to the input LaTeX file.
    :param word_file: Path to the output Word file.
    """
    try:
        # Run the Pandoc command
        subprocess.run(['pandoc', latex_file, '-o', word_file], check=True)
        print(f'Successfully converted {latex_file} to {word_file}')
    except subprocess.CalledProcessError as e:
        print(f'Error during conversion: {e}')
    except FileNotFoundError as fnf_error:
        print(f'Pandoc not found: {fnf_error}')

# Example usage
latex_file = r'C:\Users\b7k56\Downloads\Converted_Math_Questions_Answers.tex'  # Full path to your LaTeX file
word_file = r'C:\Users\b7k56\Downloads\Converted_Math_Questions_Answers.docx'  # Full path to your desired Word file
latex_to_word(latex_file, word_file)

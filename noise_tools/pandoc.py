# https://github.com/vivekVells/mcp-pandoc
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="convert-contents",
            description=(
                "Converts content between different formats. Transforms input content from any supported format "
                "into the specified output format.\n\n"
                "🚨 CRITICAL REQUIREMENTS - PLEASE READ:\n"
                "1. PDF Conversion:\n"
                "   * You MUST install TeX Live BEFORE attempting PDF conversion:\n"
                "   * Ubuntu/Debian: `sudo apt-get install texlive-xetex`\n"
                "   * macOS: `brew install texlive`\n"
                "   * Windows: Install MiKTeX or TeX Live from https://miktex.org/ or https://tug.org/texlive/\n"
                "   * PDF conversion will FAIL without this installation\n\n"
                "2. File Paths - EXPLICIT REQUIREMENTS:\n"
                "   * When asked to save or convert to a file, you MUST provide:\n"
                "     - Complete directory path\n"
                "     - Filename\n"
                "     - File extension\n"
                "   * Example request: 'Write a story and save as PDF'\n"
                "   * You MUST specify: '/path/to/story.pdf' or 'C:\\Documents\\story.pdf'\n"
                "   * The tool will NOT automatically generate filenames or extensions\n\n"
                "3. File Location After Conversion:\n"
                "   * After successful conversion, the tool will display the exact path where the file is saved\n"
                "   * Look for message: 'Content successfully converted and saved to: [file_path]'\n"
                "   * You can find your converted file at the specified location\n"
                "   * If no path is specified, files may be saved in system temp directory (/tmp/ on Unix systems)\n"
                "   * For better control, always provide explicit output file paths\n\n"
                "Supported formats:\n"
                "- Basic formats: txt, html, markdown\n"
                "- Advanced formats (REQUIRE complete file paths): pdf, docx, rst, latex, epub\n\n"
                "✅ CORRECT Usage Examples:\n"
                "1. 'Convert this text to HTML' (basic conversion)\n"
                "   - Tool will show converted content\n\n"
                "2. 'Save this text as PDF at /documents/story.pdf'\n"
                "   - Correct: specifies path + filename + extension\n"
                "   - Tool will show: 'Content successfully converted and saved to: /documents/story.pdf'\n\n"
                "❌ INCORRECT Usage Examples:\n"
                "1. 'Save this as PDF in /documents/'\n"
                "   - Missing filename and extension\n"
                "2. 'Convert to PDF'\n"
                "   - Missing complete file path\n\n"
                "When requesting conversion, ALWAYS specify:\n"
                "1. The content or input file\n"
                "2. The desired output format\n"
                "3. For advanced formats: complete output path + filename + extension\n"
                "Example: 'Convert this markdown to PDF and save as /path/to/output.pdf'\n\n"
                "Note: After conversion, always check the success message for the exact file location."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "contents": {
                        "type": "string",
                        "description": "The content to be converted (required if input_file not provided)"
                    },
                    "input_file": {
                        "type": "string",
                        "description": "Complete path to input file including filename and extension (e.g., '/path/to/input.md')"
                    },
                    "input_format": {
                        "type": "string",
                        "description": "Source format of the content (defaults to markdown)",
                        "default": "markdown",
                        "enum": ["markdown", "html", "pdf", "docx", "rst", "latex", "epub", "txt"]
                    },
                    "output_format": {
                        "type": "string",
                        "description": "Desired output format (defaults to markdown)",
                        "default": "markdown",
                        "enum": ["markdown", "html", "pdf", "docx", "rst", "latex", "epub", "txt"]
                    },
                    "output_file": {
                        "type": "string",
                        "description": "Complete path where to save the output including filename and extension (required for pdf, docx, rst, latex, epub formats)"
                    }
                },
                "oneOf": [
                    {"required": ["contents"]},
                    {"required": ["input_file"]}
                ],
                "allOf": [
                    {
                        "if": {
                            "properties": {
                                "output_format": {
                                    "enum": ["pdf", "docx", "rst", "latex", "epub"]
                                }
                            }
                        },
                        "then": {
                            "required": ["output_file"]
                        }
                    }
                ]
            },
        )
    ]

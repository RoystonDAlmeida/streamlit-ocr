import pytesseract
from PIL import Image
import io

def get_ocr_result(item):
    """
    @Args: item - object containing the item (PDF/Image)
    @Description: This method uses Pytesseract to extract text from PDF/Image.
    @Returns: result - Result of text extraction,
              json_output - JSON object containing extracted text.
    """

    # Initialize an empty string for text extraction
    extracted_text = ""

    try:
        # Check if the item is a list (assuming it contains images from a PDF)
        if isinstance(item, list):
            for img in item:
                # Ensure each item is a PIL Image
                if isinstance(img, Image.Image):
                    extracted_text += pytesseract.image_to_string(img) + "\n"
                else:
                    raise ValueError("Each item in the list must be a PIL Image.")

        else:
            # Convert input to PIL Image if it's not already
            if isinstance(item, bytes):
                img = Image.open(io.BytesIO(item))
                extracted_text = pytesseract.image_to_string(img)
            elif isinstance(item, Image.Image):
                extracted_text = pytesseract.image_to_string(item)
            else:
                raise TypeError("Input must be a bytes object or a PIL Image.")

    except Exception as e:
        # Handle exceptions and return an error message
        return None, {"error": str(e)}

    # Prepare JSON output (using a simple dictionary)
    json_output = {"extracted_text": extracted_text}

    return extracted_text, json_output
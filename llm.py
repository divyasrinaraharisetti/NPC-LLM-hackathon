from ocr import getText
import openai, ast

openai.api_key = "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"

def getLLMCoordinates(matrix):
    messages = []
    message = "Please provide a Minesweeper grid represented as a matrix (rows separated by ,) where each cell consists of either the letter X (denoting unopened boxes) or numbers from 0 to 9 (indicating the number of mines around that cell). My task is to identify and return the index [row, column] of a cell containing 'X' (unopened cell) that is least likely to contain a mine. If all cells containing 'X' have equal probability, I will return just the index of one random cell containing 'X' in [row, column] format. If there are no unopened cells, I do not return anything. I will provide the [row, column] of cells with 'X' and avoid providing the [row, column] of cells with numbers (0 to 9). I will give just the output of index of cell in format [row,column] without any explanation"
    messages.append({"role": "system", "content": message}) 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    messages.append({"role": "user", "content": matrix})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    return ast.literal_eval(reply)

def get_new_coordinates(screenshot):
    screenshot.save("matrixss.png")
    matrix = getText("matrixss.png")
    coordinates = getLLMCoordinates(matrix)
    print("Coordinates from chatgpt LLM: ", coordinates)
    return coordinates
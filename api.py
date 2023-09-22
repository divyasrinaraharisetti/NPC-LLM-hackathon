def get_setted_up_model(openai):
    messages = []
    #messages.append({"role": "system", "content": "hackathon"})

    #print("Your new assistant is ready!")
    message = "Please provide a Minesweeper grid represented as a matrix (rows separated by ,) where each cell consists of either the letter U (denoting unopened boxes) or numbers from 0 to 9 (indicating the number of mines around that cell). My task is to identify and return the index [row, column] of a cell containing 'U' (unopened cell) that is least likely to contain a mine. If all cells containing 'U' have equal probability, I will return just the index of one random cell containing 'U' in [row, column] format. If there are no unopened cells, I do not return anything. I will provide the [row, column] of cells with 'U' and avoid providing the [row, column] of cells with numbers (0 to 9). I will give just the output of index of cell in format [row,column] without any explanation"
    messages.append({"role": "system", "content": message}) 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    return messages
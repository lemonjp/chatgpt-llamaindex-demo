from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
import os
import config

os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY

question = ' '

if __name__ == "__main__":
    question = input("Do you want to recreate the index ? (y/n)")
    if question == 'y':
        loader = SimpleDirectoryReader('./data')
        documents = loader.load_data()
        index = GPTSimpleVectorIndex(documents)
        index.save_to_disk('index.json')
    else:
        index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while question:
        question = input("Type a question :")
        if question != '':
            response = index.query(question)
            print(response)
        else:
            break

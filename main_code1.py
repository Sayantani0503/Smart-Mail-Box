from transformers import BertTokenizer, BertForQuestionAnswering
import torch

tokenizer = BertTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = BertForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

def get_answer(context, question):

    inputs = tokenizer(question, context, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)

    start_index = torch.argmax(outputs.start_logits)
    end_index = torch.argmax(outputs.end_logits)

    all_tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
    answer = tokenizer.convert_tokens_to_string(all_tokens[start_index:end_index+1])
    return answer

from transformers import AutoTokenizer, AutoModel
import torch

class TextEncoder():
    def __init__(self, model_name):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

    def mean_pooling(self, token_embeddings, attention_mask):
        """
        Applies mean pooling to the token embeddings, considering the attention mask.

        Args:
            token_embeddings (torch.Tensor): The hidden states from the model (batch_size, seq_len, hidden_size).
            attention_mask (torch.Tensor): The attention mask indicating valid tokens (batch_size, seq_len).

        Returns:
            torch.Tensor: Sentence-level embeddings after mean pooling (batch_size, hidden_size).
        """
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size())

        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, dim=1)
        sum_mask = input_mask_expanded.sum(dim=1)
        sentence_embeddings = sum_embeddings / sum_mask
        
        return sentence_embeddings


    def encode(self, text):
        """
        Encodes the input text into sentence-level embeddings.

        Args:
            text (str): The input text to encode.

        Returns:
            torch.Tensor: Sentence embeddings.
        """
        inputs = self.tokenizer(text, return_tensors="pt")
        inputs.to(self.device)
        
        with torch.no_grad():
            model_output = self.model(**inputs)

        token_embeddings = model_output.last_hidden_state

        return self.mean_pooling(token_embeddings, inputs['attention_mask'])
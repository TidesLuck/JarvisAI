import sentencepiece as spm

class Tokenizer:
    def __init__(self, model_path):
        self.sp = spm.SentencePieceProcessor()
        self.sp.load(model_path)

    @property
    def vocab_size(self):
        return self.sp.get_piece_size()

    def encode(self, text):
        return torch.tensor(self.sp.encode_as_ids(text))

    def decode(self, ids):
        return self.sp.decode_ids(ids.tolist())

import torch
from pytorch_transformers import BertTokenizer, BertForQuestionAnswering

class qaptnet():
    def __init__(self,
                 data_source = 'https://github.com/nunorc/squad-v1.1-pt/raw/master',
                 source = 'model-pretrained',
                 base = 'bert-base-multilingual-cased',
                 do_lower_case = False):
        self.data_source = data_source
        self.source = source
        self.base = base
        self.do_lower_case = do_lower_case

        # init tokenizer and model
        self._build_tokenizer()
        self._build_model()

    def _build_tokenizer(self):
        print('Building tokenizer:', self.base)
        self.tokenizer = BertTokenizer.from_pretrained(self.base, do_lower_case=self.do_lower_case)


    def _build_model(self):
        print('Building model from:', self.source)
        self.model = BertForQuestionAnswering.from_pretrained(self.source)

    def query(self, context=None, question=None):
        string = f"[CLS] {question} [SEP] {context} [SEP]"
        
        starts, ends = self.model(torch.tensor(self.tokenizer.encode(string)).unsqueeze(0))

        s, e = torch.argmax(starts[0]), torch.argmax(ends[0])

        return self.tokenizer.decode(self.tokenizer.encode(string)[s:e+1])


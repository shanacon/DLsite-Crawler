from dataclasses import dataclass, fields
import warnings
import json
@dataclass
class Price:
    JPY : str
    USD : str
    EUR : str
    GBP : str
    TWD : str
    CNY : str
    KRW : str
    IDR : str
    VND : str
    THB : str
    SEK : str
    HKD : str
    SGD : str
    CAD : str
    MYR : str
    BRL : str
    AUD : str
    PHP : str
    MXN : str
    NZD : str
    INR : str
    
    @classmethod
    def from_dict(cls, price_dict: dict[str, float]) -> 'Price':
        valid_keys = {field.name for field in fields(cls)}
        
        extra_keys = set(price_dict) - valid_keys
        if extra_keys:
            warnings.warn(f'Extra keys found: {extra_keys}. They will be ignored.', UserWarning)
        
        missing_keys = valid_keys - set(price_dict)
        if missing_keys:
            warnings.warn(f'Missing keys: {missing_keys}. They will be set to default value 0.0.', UserWarning)
        
        filtered_dict = {key: price_dict.get(key, -1.0) for key in valid_keys}
        
        return cls(**filtered_dict)
    # def __repr__(self):
    #     '''Display all prices.'''
    #     return '\n'.join(f'{currency.value}: {amount:.2f}' for currency, amount in self.prices.items())
    
    def __str__(self):
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)
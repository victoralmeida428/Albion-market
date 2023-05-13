import pandas as pd

class Mercado:
    def __init__(self):
        itens = pd.read_json('https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json')
        localized = pd.json_normalize(itens.LocalizedNames)
        itens = pd.concat([itens, localized], axis=1)
        self.itens= itens[['UniqueName', 'PT-BR']]
    
    def pegar_itens(self):
        return self.itens['PT-BR'].unique()
    
    def pegar_preco(self, **kwargs):
        if kwargs['qualidade']:
            qualidade = ','.join(kwargs['qualidade'])
        else:
            qualidade = ','.join([str(i) for i in range(1,11)])

        itens_key = [list(self.itens.loc[self.itens['PT-BR']==item, 'UniqueName'].values) for item in kwargs['item']]
        itens_key = [item for sublist in itens_key for item in sublist]
        itens_key = ','.join(itens_key)
        
        url = f'https://west.albion-online-data.com/api/v2/stats/prices/{itens_key}?locations=4,7,8,301,1002,1006,1012,1301,2002,2004,2301,3002,3003,3005,3008,3301,4002,4006,4300,4301,5003&qualities={qualidade}'      
        df = pd.read_json(url)
        df = df.loc[df.sell_price_min>0].sort_values(['quality', 'sell_price_min'], ascending=[False, True])
        return df


            

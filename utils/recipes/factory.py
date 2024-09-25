from random import random


def make_recipe():
    return {
        'id': int(round(random() * 100)),
        'title': 'Suco de laraja',
        'description': 'Suco de laranja com hortelã e açucar',
        'preparation_time': 25,
        'preparation_time_unit': 'Minutos',
        'servings': 6,
        'servings_unit': 'Porção',
        'preparation_steps': 'O suco de laranja é uma bebida clássica e refrescante que oferece uma explosão de sabor cítrico e revitalizante. Com sua simplicidade e frescor, o suco de laranja é apreciado em todo o mundo por sua capacidade de fornecer uma dose saudável de vitamina C e um sabor delicioso. Ao espremer laranjas frescas, um limão e servir o suco gelado, você cria uma opção nutritiva e revigorante que pode ser apreciada a qualquer hora do dia. Além de seu sabor vibrante, o suco de laranja é conhecido por seus benefícios para a saúde, contribuindo para a imunidade, saúde da pele e saúde geral do corpo. Com o processo de preparo simples e acessível, é possível incorporar o suco de laranja em sua rotina diária, permitindo que você desfrute de uma bebida nutritiva e saborosa sempre que desejar. Descubra o prazer de preparar e saborear o suco de laranja e permita-se desfrutar dos benefícios refrescantes e revitalizantes desta bebida clássica. Aproveite os momentos de relaxamento e bem-estar em torno deste suco nutritivo e saboroso, e experimente a energia natural que a laranja pode oferecer.',
        'created_at': '26/04/2017 as 22:45',
        'author': {
            'first_name': 'Jonas',
            'last_name': 'Ribeiro',
        },
        'category': {
            'name': 'Liquidos'
        },
        'cover': {
            'url': 'https://loremflickr.com/g/650/420/food,cook',
        }
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
def suggest_outfit(weather):
    if weather == 'cold':
        return {
            'top': 'Sweater',
            'bottom': 'Jeans',
            'shoes': 'Boots',
            'jacket': 'Puffer Jacket'
        }
    elif weather == 'warm':
        return {
            'top': 'T-shirt',
            'bottom': 'Chinos',
            'shoes': 'Sneakers',
            'jacket': 'Light Jacket'
        }
    elif weather == 'hot':
        return {
            'top': 'Tank Top',
            'bottom': 'Shorts',
            'shoes': 'Sandals',
            'jacket': 'No Jacket'
        }
    elif weather == 'rainy':
        return {
            'top': 'Long Sleeve Shirt',
            'bottom': 'Jeans',
            'shoes': 'Waterproof Boots',
            'jacket': 'Raincoat'
        }
    else:
        return {
            'top': 'T-shirt',
            'bottom': 'Jeans',
            'shoes': 'Sneakers',
            'jacket': 'Hoodie'
        }

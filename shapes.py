def shape_sides(shape):
    match shape:
        case 'triangle':
            return 'It has 3 sides'
        case 'square':
            return 'It has 4 sides'
        case 'circle':
                return 'It has 0 sides'
        case _:
            return 'unknown shape'

if __name__=='__main__':
    shape=input('Type a shape: ').lower()
    print(shape_sides(shape))

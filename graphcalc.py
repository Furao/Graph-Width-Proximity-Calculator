

def walk(graph):
    """Walk the matrix."""
    for i, row in enumerate(graph):
        for j, column in enumerate(row):
            if column == 1:
                print 'V%i connects V%i' % (i+1, j+1)

if __name__ == '__main__':
    
    g = [ \
        [0, 1, 0, 1], \
        [1, 0, 1, 1], \
        [0, 1, 0, 0], \
        [1, 1, 0, 0]  \
        ]

    # for row in g:
    #     print row

    expected_width = 2
    expected_prox = 1

    walk(g)
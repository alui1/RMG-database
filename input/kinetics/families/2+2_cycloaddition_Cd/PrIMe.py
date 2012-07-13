#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 24,
    label = "r00010716",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S}
3 *4 C 0 {1,S} {5,S}
4    C 0 {1,S}
5 *3 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1 *4 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.4e+15,"s^-1"),
        n = (0.0,""),
        Ea = (258580.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Zalotai, L.", "Berces, T.", "Marta, F."],
        title = u'Kinetics and energy transfer in the thermal decomposition of 2-methyloxetane and 3-methyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "86",
        pages = """21""",
        year = "1990",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010716/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010716/rk00000001.xml
""",
    history = [('Tue May 17 14:34:40 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010716/rk00000001.xml')],
)

entry(
    index = 25,
    label = "r00010716",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S}
3 *4 C 0 {1,S} {5,S}
4    C 0 {1,S}
5 *3 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1 *4 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.4e+15,"s^-1"),
        n = (0.0,""),
        Ea = (258580.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Zalotai, L.", "Berces, T.", "Marta, F."],
        title = u'Collisional energy transfer in the decomposition of 2-methyloxetane and 3-methyloxetane, I. Gas/gas collisions',
        journal = "React. Kinet. Catal. Lett.",
        volume = "42",
        pages = """79""",
        year = "1990",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010716/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010716/rk00000002.xml
""",
    history = [('Tue May 17 14:34:40 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010716/rk00000002.xml')],
)

entry(
    index = 34,
    label = "r00011611",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {5,S}
2 *1 C 0 {1,S} {4,S}
3 *4 C 0 {1,S} {4,S}
4 *3 C 0 {2,S} {3,S}
5    C 0 {1,S} {6,D}
6    O 0 {5,D}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3 *1 C 0 {1,D}
4    O 0 {2,D}
""",
    product2 = 
"""
1 *4 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2.7e+14,"s^-1"),
        n = (0.0,""),
        Ea = (222828.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Roquitte, B.C.", "Walters, W.D."],
        title = u'The thermal decomposition of cyclobutanecarboxaldehyde',
        journal = "J. Am. Chem. Soc.",
        volume = "84",
        pages = """4049-4052""",
        year = "1962",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011611/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011611/rk00000001.xml
""",
    history = [('Tue May 17 14:34:48 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011611/rk00000001.xml')],
)

entry(
    index = 35,
    label = "r00011630",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {6,S}
2 *1 C 0 {1,S} {4,S}
3 *4 C 0 {1,S} {4,S}
4 *3 C 0 {2,S} {3,S}
5    C 0 {6,S}
6    C 0 {1,S} {5,S} {7,D}
7    C 0 {6,D}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {4,D}
3 *2 C 0 {2,S} {5,D}
4    C 0 {2,D}
5 *1 C 0 {3,D}
""",
    product2 = 
"""
1 *4 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.37e+14,"s^-1"),
        n = (0.0,""),
        Ea = (213682.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Ellis, R.J.", "Frey, H.M."],
        title = u'Thermal unimolecular decomposition of isopropenylcyclobutane',
        journal = "Trans. Faraday Soc.",
        volume = "59",
        pages = """2076-2079""",
        year = "1963",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011630/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011630/rk00000001.xml
""",
    history = [('Tue May 17 14:34:49 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011630/rk00000001.xml')],
)

entry(
    index = 36,
    label = "r00011630",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {6,S}
2 *1 C 0 {1,S} {4,S}
3 *4 C 0 {1,S} {4,S}
4 *3 C 0 {2,S} {3,S}
5    C 0 {6,S}
6    C 0 {1,S} {5,S} {7,D}
7    C 0 {6,D}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {4,D}
3 *2 C 0 {2,S} {5,D}
4    C 0 {2,D}
5 *1 C 0 {3,D}
""",
    product2 = 
"""
1 *4 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.66e+15,"s^-1"),
        n = (0.0,""),
        Ea = (218671.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Frey, H.M.", "Pottinger, R."],
        title = u'Thermal unimolecular reactions of vinylcyclobutane and isopropenylcyclobutane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "74",
        pages = """1827""",
        year = "1978",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011630/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011630/rk00000002.xml
""",
    history = [('Tue May 17 14:34:49 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011630/rk00000002.xml')],
)

entry(
    index = 50,
    label = "r00015648",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S} {5,S}
2 *4 C 0 {1,S} {4,S} {6,S}
3 *1 C 0 {1,S} {4,S}
4 *2 C 0 {2,S} {3,S}
5    C 0 {1,S}
6    C 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *4 C 0 {1,S} {4,D}
4 *3 C 0 {2,S} {3,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.7e+15,"s^-1"),
        n = (0.0,""),
        Ea = (263569.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Gerberich, H.R.", "Walters, W.D."],
        title = u'The thermal decomposition of cis-1,2-dimethylcyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """3935-3939""",
        year = "1961",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015648/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015648/rk00000001.xml
""",
    history = [('Tue May 17 14:35:25 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015648/rk00000001.xml')],
)

entry(
    index = 51,
    label = "r00015649",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {5,S}
2 *4 C 0 {1,S} {4,S} {6,S}
3 *1 C 0 {1,S} {4,S}
4 *3 C 0 {2,S} {3,S}
5    C 0 {1,S}
6    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3e+15,"s^-1"),
        n = (0.0,""),
        Ea = (252760.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Gerberich, H.R.", "Walters, W.D."],
        title = u'The thermal decomposition of cis-1,2-dimethylcyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """3935-3939""",
        year = "1961",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015649/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015649/rk00000001.xml
""",
    history = [('Tue May 17 14:35:25 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015649/rk00000001.xml')],
)

entry(
    index = 52,
    label = "r00015651",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S} {5,S}
2 *4 C 0 {1,S} {4,S} {6,S}
3 *1 C 0 {1,S} {4,S}
4 *2 C 0 {2,S} {3,S}
5    C 0 {1,S}
6    C 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *4 C 0 {1,S} {4,D}
4 *3 C 0 {2,S} {3,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.9e+15,"s^-1"),
        n = (0.0,""),
        Ea = (265232.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Gerberich, H.R.", "Walters, W.D."],
        title = u'The thermal decomposition of trans-1,2-dimethylcyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """4884-4888""",
        year = "1961",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015651/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015651/rk00000001.xml
""",
    history = [('Tue May 17 14:35:25 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015651/rk00000001.xml')],
)

entry(
    index = 53,
    label = "r00015652",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {5,S}
2 *4 C 0 {1,S} {4,S} {6,S}
3 *1 C 0 {1,S} {4,S}
4 *3 C 0 {2,S} {3,S}
5    C 0 {1,S}
6    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.8e+15,"s^-1"),
        n = (0.0,""),
        Ea = (257749.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Gerberich, H.R.", "Walters, W.D."],
        title = u'The thermal decomposition of trans-1,2-dimethylcyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """4884-4888""",
        year = "1961",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015652/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015652/rk00000001.xml
""",
    history = [('Tue May 17 14:35:25 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015652/rk00000001.xml')],
)

entry(
    index = 54,
    label = "r00016155",
    reactant1 = 
"""
1 *2 C 0 {3,S} {4,S} {5,S} {6,S}
2 *3 C 0 {3,S} {4,S} {7,S} {8,S}
3 *1 C 0 {1,S} {2,S}
4 *4 C 0 {1,S} {2,S}
5    C 0 {1,S}
6    C 0 {1,S}
7    C 0 {2,S}
8    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *1 C 0 {3,D}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *3 C 0 {1,S} {2,S} {4,D}
4 *4 C 0 {3,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.04e+16,"s^-1"),
        n = (0.0,""),
        Ea = (272715.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Cocks, A.T.", "Frey, H.M."],
        title = u'Thermal unimolecular decomposition of 1,1,3,3-tetramethylcyclobutane',
        journal = "J. Chem. Soc. A",
        pages = """1671-1673""",
        year = "1969",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016155/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016155/rk00000001.xml
""",
    history = [('Tue May 17 14:35:38 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016155/rk00000001.xml')],
)

entry(
    index = 55,
    label = "r00016231",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2 *2 C 0 {1,S} {5,S} {6,S}
3 *3 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *4 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *2 C 0 {1,S} {4,D}
4 *1 C 0 {2,S} {3,D}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *4 O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.09e+15,"s^-1"),
        n = (0.0,""),
        Ea = (266063.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016231/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016231/rk00000001.xml
""",
    history = [('Tue May 17 14:35:40 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016231/rk00000001.xml')],
)

entry(
    index = 56,
    label = "r00016232",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S} {5,S} {6,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *3 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.13e+15,"s^-1"),
        n = (0.0,""),
        Ea = (270220.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016232/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016232/rk00000001.xml
""",
    history = [('Tue May 17 14:35:40 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016232/rk00000001.xml')],
)

entry(
    index = 57,
    label = "r00016297",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2 *2 C 0 {1,S} {5,S} {6,S}
3 *3 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *4 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *2 C 0 {1,S} {4,D}
4 *1 C 0 {2,S} {3,D}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *4 O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.74e+15,"s^-1"),
        n = (0.0,""),
        Ea = (261074.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016297/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016297/rk00000001.xml
""",
    history = [('Tue May 17 14:35:42 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016297/rk00000001.xml')],
)

entry(
    index = 58,
    label = "r00016298",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S} {5,S} {6,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *3 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = (0.0,""),
        Ea = (264400.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016298/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016298/rk00000001.xml
""",
    history = [('Tue May 17 14:35:42 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016298/rk00000001.xml')],
)

entry(
    index = 60,
    label = "r00016300",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {5,S} {6,S}
2 *4 C 0 {1,S} {4,S} {7,S}
3 *1 C 0 {1,S} {4,S}
4 *3 C 0 {2,S} {3,S}
5    C 0 {1,S}
6    C 0 {1,S}
7    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *1 C 0 {3,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.62e+15,"s^-1"),
        n = (0.0,""),
        Ea = (251929.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Cocks, A.T.", "Frey, H.M."],
        title = u'The Thermal Unimolecular Decomposition of 1,1,2-Trimethylcyclobutane',
        journal = "J. Phys. Chem.",
        volume = "75",
        pages = """1437""",
        year = "1971",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016300/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016300/rk00000001.xml
""",
    history = [('Tue May 17 14:35:42 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016300/rk00000001.xml')],
)

entry(
    index = 62,
    label = "r00016567",
    reactant1 = 
"""
1 *2 C 0 {2,S} {4,S} {5,S} {8,S}
2 *1 C 0 {1,S} {3,S} {6,S}
3 *3 C 0 {2,S} {7,S} {8,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {3,S}
8 *4 O 0 {1,S} {3,S}
""",
    product1 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {5,S}
4 *2 C 0 {1,S} {2,S} {5,D}
5 *1 C 0 {3,S} {4,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *4 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+14,"s^-1"),
        n = (0.0,""),
        Ea = (236962.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A.", "Carless, H.A.J."],
        title = u'Thermolyses of cis- and trans-2,2,3,4-tetramethyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """691""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016567/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016567/rk00000001.xml
""",
    history = [('Tue May 17 14:35:49 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016567/rk00000001.xml')],
)

entry(
    index = 63,
    label = "r00016568",
    reactant1 = 
"""
1 *2 C 0 {2,S} {4,S} {5,S} {8,S}
2 *1 C 0 {1,S} {3,S} {6,S}
3 *3 C 0 {2,S} {7,S} {8,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {3,S}
8 *4 O 0 {1,S} {3,S}
""",
    product1 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {5,S}
4 *2 C 0 {1,S} {2,S} {5,D}
5 *1 C 0 {3,S} {4,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *4 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+13,"s^-1"),
        n = (0.0,""),
        Ea = (228648.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A.", "Carless, H.A.J."],
        title = u'Thermolyses of cis- and trans-2,2,3,4-tetramethyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """691""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016568/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016568/rk00000001.xml
""",
    history = [('Tue May 17 14:35:50 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016568/rk00000001.xml')],
)

entry(
    index = 64,
    label = "r00016669",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {6,S}
2 *1 C 0 {1,S} {4,S} {8,S}
3 *4 C 0 {1,S} {5,S} {8,S}
4    C 0 {2,S}
5    C 0 {3,S}
6    C 0 {1,S} {7,D}
7    C 0 {6,D}
8 *3 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 0 {2,D} {4,S}
4    C 0 {3,S} {5,D}
5    C 0 {4,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.63e+13,"s^-1"),
        n = (0.0,""),
        Ea = (200379.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Carless, H.A.J.", "Maitra, A.K.", "Pottinger, R.", "Frey, H.M."],
        title = u'Thermal decomposition of cis-2,4-dimethyl-trans-3-vinyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "76",
        pages = """1849""",
        year = "1980",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016669/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016669/rk00000001.xml
""",
    history = [('Tue May 17 14:35:52 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016669/rk00000001.xml')],
)
